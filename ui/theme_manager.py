from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
import os

class ThemeManager:
    @staticmethod
    def apply_dark_theme(app: QApplication):
        dark_palette = QPalette()
        
        # Define Material Design colors
        surface = QColor(18, 18, 18)      # Main background
        primary = QColor(30, 30, 30)      # Elevated surfaces
        on_surface = QColor(255, 255, 255) # Text color
        
        # Set colors
        # Set the main window background color
        dark_palette.setColor(QPalette.Window, surface)
        # Set the color of text that appears on Window backgrounds
        dark_palette.setColor(QPalette.WindowText, on_surface)
        # Set the background color of text entry widgets and views
        dark_palette.setColor(QPalette.Base, primary)
        # Set the alternate background color for views with alternating row colors
        dark_palette.setColor(QPalette.AlternateBase, surface)
        # Set the color of text in text entry widgets
        dark_palette.setColor(QPalette.Text, on_surface)
        # Set the background color of buttons
        dark_palette.setColor(QPalette.Button, primary)
        # Set the color of text that appears on buttons
        dark_palette.setColor(QPalette.ButtonText, on_surface)
        
        app.setPalette(dark_palette)
        
        # Load stylesheet from file
        stylesheet_path = os.path.join(os.path.dirname(__file__), "style.qss")
        with open(stylesheet_path, 'r') as file:
            app.setStyleSheet(file.read())
        
        