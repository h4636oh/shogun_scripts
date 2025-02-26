from PySide6.QtWidgets import QWidget, QFileDialog, QStackedWidget, QVBoxLayout
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt
import os
from ui_functions.scripts_selection import ScriptsSelection
import ui.resources_rc

class HomePage(QWidget):
    def __init__(self):
        super().__init__()

        # Create main layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Load UI
        ui_path = os.path.join(os.path.dirname(__file__), "../ui", "homepage.ui")
        loader = QUiLoader()
        self.ui = loader.load(ui_path)
        
        # Add UI to layout and set size policy
        layout.addWidget(self.ui)
        self.ui.setSizePolicy(self.ui.sizePolicy())
        
        # Make sure the widget expands properly
        self.setLayout(layout)
        self.setAttribute(Qt.WA_StyledBackground, True)

        # Connect button
        self.ui.select_folder_btn.clicked.connect(self.select_folder)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            # Create the scripts selection widget
            scripts_selection = ScriptsSelection(folder)
            
            # Find the MainWindow's stacked widget
            main_window = self.window()  # This gets the top-level window
            if hasattr(main_window, 'stacked_widget'):
                # Add the new widget and switch to it
                main_window.stacked_widget.addWidget(scripts_selection)
                main_window.stacked_widget.setCurrentWidget(scripts_selection)
