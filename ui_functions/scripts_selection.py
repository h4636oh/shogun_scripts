from PySide6.QtWidgets import QWidget, QFileSystemModel, QVBoxLayout, QAbstractItemView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QDir, Qt, QItemSelectionModel
import os
import re
import ui.resources_rc

class ScriptsSelection(QWidget):
    def __init__(self, folder_path):
        super().__init__()

        # Store folder path
        self.folder_path = folder_path

        # Define supported script extensions
        self.script_extensions = ["*.sh", "*.bash", "*.py", "*.pl", "*.rb", "*.js", "*.php", "*.ps1"]

        # Create main layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Load UI
        ui_path = os.path.join(os.path.dirname(__file__), "../ui", "scripts_selection.ui")
        loader = QUiLoader()
        self.ui = loader.load(ui_path)
        
        # Add UI to layout and set size policy
        layout.addWidget(self.ui)
        self.ui.setSizePolicy(self.ui.sizePolicy())
        
        # Make sure the widget expands properly
        self.setLayout(layout)
        self.setAttribute(Qt.WA_StyledBackground, True)

        # Setup model for QListView
        self.model = QFileSystemModel()
        self.model.setRootPath(folder_path)
        self.model.setFilter(QDir.Files)  # Show only files, not folders
        self.model.setNameFilterDisables(False)  # Hide files instead of disabling them
        self.model.setNameFilters(self.script_extensions)  # Show only script files

        # Configure the list view
        self.ui.scripts_view.setModel(self.model)
        self.ui.scripts_view.setRootIndex(self.model.index(folder_path))
        
        # Enable multiple selection
        self.ui.scripts_view.setSelectionMode(QAbstractItemView.MultiSelection)
        
        # Connect buttons
        self.ui.back_btn.clicked.connect(self.go_back)
        self.ui.select_all_btn.toggled.connect(self.select_all_files)
        self.ui.search_btn.clicked.connect(self.search_files)
        self.ui.search_field.returnPressed.connect(self.search_files)
        self.ui.regex_btn.toggled.connect(self.search_files)
        self.ui.continue_btn.clicked.connect(self.continue_to_progress)

    def search_files(self):
        """Search files based on the search field text"""
        search_text = self.ui.search_field.text().strip()
        
        if not search_text:
            # If search is empty, show all script files
            self.model.setNameFilters(self.script_extensions)
            return
            
        if self.ui.regex_btn.isChecked():
            try:
                # Use regex pattern
                pattern = re.compile(search_text)
                # Get all script files in directory
                files = []
                for ext in self.script_extensions:
                    ext = ext.replace('*', '')  # Remove wildcard
                    files.extend([f for f in os.listdir(self.folder_path) if f.endswith(ext)])
                # Filter files that match the pattern
                matching_files = [f for f in files if pattern.search(f)]
                # Set name filters to show only matching files
                self.model.setNameFilters(matching_files if matching_files else [""])
            except re.error:
                # Invalid regex pattern - show no files
                self.model.setNameFilters([""])
        else:
            # Simple text search with wildcards for all script types
            filters = [f"*{search_text}*{ext[1:]}" for ext in self.script_extensions]
            self.model.setNameFilters(filters)

    def select_all_files(self, checked):
        """Select or deselect all files based on button state"""
        root_index = self.ui.scripts_view.rootIndex()
        row_count = self.model.rowCount(root_index)
        
        selection_flag = QItemSelectionModel.Select if checked else QItemSelectionModel.Deselect
        self.ui.select_all_btn.setText("Deselect All" if checked else "Select All")
        
        for row in range(row_count):
            index = self.model.index(row, 0, root_index)
            self.ui.scripts_view.selectionModel().select(
                index, 
                selection_flag
            )

    def go_back(self):
        main_window = self.window()
        if hasattr(main_window, 'stacked_widget'):
            current_index = main_window.stacked_widget.currentIndex()
            if current_index > 0:
                main_window.stacked_widget.setCurrentIndex(current_index - 1)
                main_window.stacked_widget.removeWidget(self)

    def get_selected_files(self):
        """Returns a list of selected file paths"""
        selected_indexes = self.ui.scripts_view.selectedIndexes()
        return [self.model.filePath(index) for index in selected_indexes]

    def continue_to_progress(self):
        """Move to progress bar screen with selected files"""
        selected_files = self.get_selected_files()
        if not selected_files:
            return  # Don't proceed if no files are selected
            
        main_window = self.window()
        if hasattr(main_window, 'stacked_widget'):
            from ui_functions.progress_bar import ProgressBar
            progress_screen = ProgressBar(selected_files)
            main_window.stacked_widget.addWidget(progress_screen)
            main_window.stacked_widget.setCurrentWidget(progress_screen)