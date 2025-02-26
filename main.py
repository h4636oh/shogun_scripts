import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PySide6.QtCore import Qt, QCoreApplication
from ui_functions.homepage import HomePage
import ui.resources_rc
from PySide6.QtWidgets import QStyleFactory
from ui.theme_manager import ThemeManager
from ui_functions.style_watcher import StylesheetWatcher
import os
from PySide6.QtGui import QIcon

# Set OpenGL attribute before creating QApplication
QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

# Create application instance
app = QApplication(sys.argv)

# Set application info
app.setApplicationName("Shogun Scripts")
app.setApplicationDisplayName("Shogun Scripts")
app.setOrganizationName("h4636oh")  # Optional
app.setOrganizationDomain("github.com/h4636oh")  # Optional

# Set application icon
icon_path = os.path.join("ui", "icons", "app", "app.png")
if os.path.exists(icon_path):
    app.setWindowIcon(QIcon(icon_path))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shogun Scripts")
        
        # Set window icon
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        
        # Create stacked widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Add HomePage to stacked widget
        self.homepage = HomePage()
        self.stacked_widget.addWidget(self.homepage)

def main():
    # Apply theme
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
