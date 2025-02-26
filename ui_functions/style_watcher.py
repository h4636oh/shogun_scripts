from PySide6.QtCore import QFileSystemWatcher
import os

class StylesheetWatcher:
    def __init__(self, app, stylesheet_path):
        self.app = app
        self.stylesheet_path = stylesheet_path
        
        # Create file watcher
        self.watcher = QFileSystemWatcher([stylesheet_path])
        self.watcher.fileChanged.connect(self.reload_stylesheet)
        
    def reload_stylesheet(self):
        """Reload the stylesheet when the file changes"""
        if os.path.exists(self.stylesheet_path):
            with open(self.stylesheet_path, 'r') as file:
                self.app.setStyleSheet(file.read()) 