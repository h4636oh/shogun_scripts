import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from ui_functions.homepage import HomePage
from PySide6.QtCore import Qt
import ui.resources_rc
from PySide6.QtWidgets import QStyleFactory
from ui.theme_manager import ThemeManager
from ui_functions.style_watcher import StylesheetWatcher
import os

# Ensure resources are loaded before creating QApplication
QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shogun Scripts")
        
        # Create stacked widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Add HomePage to stacked widget
        self.homepage = HomePage()
        self.stacked_widget.addWidget(self.homepage)

def main():
    app = QApplication(sys.argv)
    
    # Apply dark theme
    ThemeManager.apply_dark_theme(app)
    
    # Setup style watcher
    stylesheet_path = os.path.join(os.path.dirname(__file__), "ui", "style.qss")
    watcher = StylesheetWatcher(app, stylesheet_path)
    
    # Rest of your application code...
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
