from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QTimer
import os
import subprocess
import datetime
import ui.resources_rc

class ProgressBar(QWidget):
    def __init__(self, selected_files):
        super().__init__()

        # Store selected files
        self.selected_files = selected_files
        self.current_index = 0
        self.total_files = len(selected_files)
        self.current_process = None
        self.is_processing = True

        # Define interpreters for different file extensions
        self.interpreters = {
            '.sh': '/bin/bash',
            '.bash': '/bin/bash',
            '.py': 'python3',
            '.rb': 'ruby',
            '.pl': 'perl',
            '.php': 'php',
            '.js': 'node',
            '.ps1': 'pwsh'  # 'powershell' on Windows, 'pwsh' on Linux/cross-platform
        }

        # Create log directory
        self.setup_log_directory()

        # Create main layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Load UI
        ui_path = os.path.join(os.path.dirname(__file__), "../ui", "progress_bar.ui")
        loader = QUiLoader()
        self.ui = loader.load(ui_path)
        
        # Add UI to layout and set size policy
        layout.addWidget(self.ui)
        self.ui.setSizePolicy(self.ui.sizePolicy())
        
        # Make sure the widget expands properly
        self.setLayout(layout)
        self.setAttribute(Qt.WA_StyledBackground, True)

        # Initialize progress bar
        self.ui.progress_bar.setMinimum(0)
        self.ui.progress_bar.setMaximum(self.total_files)
        self.ui.progress_bar.setValue(0)

        # Connect stop button
        self.ui.stop_btn.clicked.connect(self.stop_processing)

        # Start processing files
        QTimer.singleShot(0, self.process_next_file)

    def setup_log_directory(self):
        """Create timestamped log directory"""
        # Get base folder path from the first file's location
        base_folder = os.path.dirname(self.selected_files[0])
        
        # Create logs folder if it doesn't exist
        logs_path = os.path.join(base_folder, "logs")
        if not os.path.exists(logs_path):
            os.makedirs(logs_path)
            
        # Create timestamped folder for this run
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_dir = os.path.join(logs_path, f"shogun_scripts_{timestamp}")
        os.makedirs(self.log_dir)

    def get_interpreter(self, file_path):
        """Get the interpreter based on file extension"""
        _, ext = os.path.splitext(file_path)
        return self.interpreters.get(ext.lower(), '/bin/bash')  # Default to bash if extension not found

    def stop_processing(self):
        """Stop the current script execution and return to selection screen"""
        self.is_processing = False
        
        # Terminate current process if it exists
        if self.current_process and self.current_process.poll() is None:
            self.current_process.terminate()
            
        # Return to scripts selection screen
        main_window = self.window()
        if hasattr(main_window, 'stacked_widget'):
            current_index = main_window.stacked_widget.currentIndex()
            if current_index > 0:
                main_window.stacked_widget.setCurrentIndex(current_index - 1)
                main_window.stacked_widget.removeWidget(self)

    def move_to_output_screen(self):
        """Switch to the scripts output screen"""
        main_window = self.window()
        if hasattr(main_window, 'stacked_widget'):
            from ui_functions.scripts_output import ScriptsOutput
            output_screen = ScriptsOutput(self.log_dir)
            main_window.stacked_widget.addWidget(output_screen)
            main_window.stacked_widget.setCurrentWidget(output_screen)
            # Remove this progress screen
            main_window.stacked_widget.removeWidget(self)

    def process_next_file(self):
        """Process the next file in the queue"""
        if not self.is_processing or self.current_index >= self.total_files:
            if self.is_processing:
                self.ui.filename_lbl.setText("All files processed!")
                # Move to output screen after a short delay
                QTimer.singleShot(1000, self.move_to_output_screen)
            return

        current_file = self.selected_files[self.current_index]
        filename = os.path.basename(current_file)
        filename_without_ext = os.path.splitext(filename)[0]  # Remove extension
        self.ui.filename_lbl.setText(f"Processing: {filename_without_ext}")
        
        try:
            # Make the file executable
            os.chmod(current_file, 0o755)
            
            # Get interpreter based on file extension
            interpreter = self.get_interpreter(current_file)
            
            # Create log file path
            log_file = os.path.join(self.log_dir, f"{filename_without_ext}.log")
            
            # Execute the script with the appropriate interpreter and capture output
            with open(log_file, 'w') as f:
                self.current_process = subprocess.Popen(
                    [interpreter, current_file],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    universal_newlines=True,
                    bufsize=1
                )
                
                # Write output to log file in real-time
                for line in self.current_process.stdout:
                    f.write(line)
                    f.flush()
                
                self.current_process.wait()  # Wait for the process to complete

            # Update progress
            self.current_index += 1
            self.ui.progress_bar.setValue(self.current_index)
            
            # Process next file
            if self.is_processing:
                QTimer.singleShot(0, self.process_next_file)

        except Exception as e:
            self.ui.filename_lbl.setText(f"Error processing {filename_without_ext}: {str(e)}")
            # Log the error
            log_file = os.path.join(self.log_dir, f"{filename_without_ext}_error.log")
            with open(log_file, 'w') as f:
                f.write(str(e))
