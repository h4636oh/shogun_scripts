from PySide6.QtWidgets import QWidget, QVBoxLayout, QHeaderView, QFileDialog, QAbstractItemView, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtGui import QStandardItemModel, QStandardItem
import os
import re
import datetime
import ui.resources_rc
from fpdf import FPDF  # Using FPDF instead of reportlab

class ScriptsOutput(QWidget):
    def __init__(self, log_dir):
        super().__init__()

        # Store log directory
        self.log_dir = log_dir

        # Create main layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Load UI
        ui_path = os.path.join(os.path.dirname(__file__), "../ui", "scripts_output.ui")
        loader = QUiLoader()
        self.ui = loader.load(ui_path)
        
        # Add UI to layout and set size policy
        layout.addWidget(self.ui)
        self.setLayout(layout)
        self.setAttribute(Qt.WA_StyledBackground, True)

        # Configure the tree view
        self.model = QStandardItemModel()
        
        # Set model to tree view
        self.ui.logs_view.setModel(self.model)
        
        # Make tree view non-editable
        self.ui.logs_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        # Disable horizontal scrollbar
        self.ui.logs_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        # Configure header
        header = self.ui.logs_view.header()
        
        # Create root item with two columns
        root = self.model.invisibleRootItem()
        self.model.setColumnCount(2)
        
        # Set header labels
        self.model.setHorizontalHeaderLabels(["Script", "Status"])
        
        # Set column widths after model is populated
        self.ui.logs_view.setColumnWidth(0, 500)
        self.ui.logs_view.setColumnWidth(1, 100)
        
        # Load log files
        self.load_logs()

        # Connect buttons and signals
        self.ui.back_btn.clicked.connect(self.go_back)
        self.ui.search_btn.clicked.connect(self.search_files)
        self.ui.search_field.returnPressed.connect(self.search_files)
        self.ui.regex_btn.toggled.connect(self.search_files)
        self.ui.logs_view.expanded.connect(self.on_item_expanded)
        self.ui.select_all_btn.clicked.connect(self.toggle_select_all)
        self.ui.save_btn.clicked.connect(self.save_to_pdf)
        
        # Initialize select all button state
        self.all_expanded = False
        self.ui.select_all_btn.setText("Expand All")

    def load_logs(self):
        """Load all log files into the tree view"""
        self.model.clear()
        
        # Get all log files
        log_files = [f for f in os.listdir(self.log_dir) if f.endswith('.log')]
        
        for log_file in sorted(log_files):
            if log_file.endswith('_error.log'):
                continue  # Skip error logs as they're handled with main logs
                
            # Create item for the script
            script_name = os.path.splitext(log_file)[0]
            name_item = QStandardItem(script_name)
            
            # Check if there's an error log
            error_log = f"{script_name}_error.log"
            status_item = QStandardItem()
            if os.path.exists(os.path.join(self.log_dir, error_log)):
                status_item.setText("Error")
                status_item.setForeground(Qt.red)
            else:
                status_item.setText("Success")
                status_item.setForeground(Qt.green)
            
            # Add a placeholder child item
            placeholder = QStandardItem("")
            name_item.appendRow([placeholder])
            
            # Add items to model
            self.model.appendRow([name_item, status_item])

    def on_item_expanded(self, index):
        """Load and show log content when item is expanded"""
        item = self.model.itemFromIndex(index)
        if item and item.rowCount() == 1 and item.child(0).text() == "":
            # Clear the placeholder
            item.removeRow(0)
            
            # Get log content
            script_name = item.text()
            log_file = os.path.join(self.log_dir, f"{script_name}.log")
            error_log = os.path.join(self.log_dir, f"{script_name}_error.log")
            
            try:
                # Add output content
                with open(log_file, 'r') as f:
                    content = f.read().strip()
                    if content:
                        output_item = QStandardItem(content)
                        item.appendRow([output_item])
                
                # Add error content if exists
                if os.path.exists(error_log):
                    with open(error_log, 'r') as f:
                        error_content = f.read().strip()
                        if error_content:
                            error_item = QStandardItem(f"Error: {error_content}")
                            error_item.setForeground(Qt.red)
                            item.appendRow([error_item])
            
            except Exception as e:
                error_item = QStandardItem(f"Error reading log: {str(e)}")
                error_item.setForeground(Qt.red)
                item.appendRow([error_item])

    def search_files(self):
        """Search through script names"""
        search_text = self.ui.search_field.text().strip()
        
        for row in range(self.model.rowCount()):
            item = self.model.item(row, 0)
            if not item:
                continue
                
            if not search_text:
                # Show all items if search is empty
                self.ui.logs_view.setRowHidden(row, QModelIndex(), False)
                continue
                
            if self.ui.regex_btn.isChecked():
                try:
                    pattern = re.compile(search_text)
                    self.ui.logs_view.setRowHidden(
                        row, 
                        QModelIndex(), 
                        not bool(pattern.search(item.text()))
                    )
                except re.error:
                    # Hide all items on invalid regex
                    self.ui.logs_view.setRowHidden(row, QModelIndex(), True)
            else:
                # Simple text search
                self.ui.logs_view.setRowHidden(
                    row,
                    QModelIndex(),
                    search_text.lower() not in item.text().lower()
                )

    def go_back(self):
        """Return to scripts selection screen"""
        main_window = self.window()
        if hasattr(main_window, 'stacked_widget'):
            current_index = main_window.stacked_widget.currentIndex()
            if current_index > 0:
                main_window.stacked_widget.setCurrentIndex(current_index - 1)
                main_window.stacked_widget.removeWidget(self)

    def toggle_select_all(self):
        """Toggle between expanding and collapsing all items"""
        if not self.all_expanded:
            # Expand all items
            self.expand_all_items()
            self.ui.select_all_btn.setText("Collapse All")
            self.all_expanded = True
        else:
            # Collapse all items
            self.collapse_all_items()
            self.ui.select_all_btn.setText("Expand All")
            self.all_expanded = False

    def expand_all_items(self):
        """Expand all items and load their content"""
        for row in range(self.model.rowCount()):
            index = self.model.index(row, 0)
            item = self.model.itemFromIndex(index)
            if not self.ui.logs_view.isExpanded(index):
                self.ui.logs_view.expand(index)
                self.on_item_expanded(index)

    def collapse_all_items(self):
        """Collapse all items"""
        for row in range(self.model.rowCount()):
            index = self.model.index(row, 0)
            self.ui.logs_view.collapse(index)

    def save_to_pdf(self):
        """Save all script outputs to a PDF file"""
        # Get save location from user
        file_name = f"script_outputs_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save PDF Report",
            file_name,
            "PDF Files (*.pdf)"
        )
        
        if not file_path:
            return  # User cancelled

        try:
            # Create PDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=16)
            
            # Add title
            pdf.cell(200, 10, txt="Script Execution Report", ln=1, align='C')
            pdf.set_font("Arial", size=10)
            pdf.cell(200, 10, txt=f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=1, align='C')
            pdf.ln(10)

            # Add summary table
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(100, 10, "Script", 1)
            pdf.cell(90, 10, "Status", 1)
            pdf.ln()
            
            pdf.set_font("Arial", size=10)
            for row in range(self.model.rowCount()):
                script_name = self.model.item(row, 0).text()
                status = self.model.item(row, 1).text()
                pdf.cell(100, 10, script_name, 1)
                pdf.cell(90, 10, status, 1)
                pdf.ln()

            pdf.ln(10)
            
            # Add detailed output for each script
            pdf.set_font("Arial", 'B', 12)
            for row in range(self.model.rowCount()):
                script_name = self.model.item(row, 0).text()
                status = self.model.item(row, 1).text()
                
                # Add script header
                pdf.cell(200, 10, f"Script: {script_name} ({status})", ln=1)
                pdf.set_font("Courier", size=9)
                
                # Get script output
                log_file = os.path.join(self.log_dir, f"{script_name}.log")
                error_log = os.path.join(self.log_dir, f"{script_name}_error.log")
                
                # Add output content
                try:
                    if os.path.exists(log_file):
                        with open(log_file, 'r') as f:
                            output = f.read().strip()
                            if output:
                                pdf.multi_cell(0, 5, output)
                                pdf.ln(5)
                    
                    if os.path.exists(error_log):
                        with open(error_log, 'r') as f:
                            error = f.read().strip()
                            if error:
                                pdf.set_text_color(255, 0, 0)  # Red for errors
                                pdf.multi_cell(0, 5, f"Error: {error}")
                                pdf.set_text_color(0, 0, 0)  # Reset to black
                                pdf.ln(5)
                except Exception as e:
                    pdf.set_text_color(255, 0, 0)
                    pdf.multi_cell(0, 5, f"Error reading log: {str(e)}")
                    pdf.set_text_color(0, 0, 0)

                pdf.ln(10)
                pdf.set_font("Arial", 'B', 12)

            # Save PDF
            pdf.output(file_path)
            QMessageBox.information(self, "Success", "PDF report generated successfully!")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to generate PDF: {str(e)}")
