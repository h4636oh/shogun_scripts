# Shogun Scripts

A powerful script management and execution tool that allows you to run multiple scripts simultaneously while monitoring their progress and output.

## Features

- 🔍 **Script Discovery**: Easily browse and select scripts from any folder
- 🔄 **Batch Execution**: Run multiple scripts simultaneously
- 📊 **Progress Monitoring**: Track execution progress in real-time
- 📝 **Output Management**: View and save script outputs
- 🔍 **Search Functionality**: Quick script search with regex support
- 📄 **PDF Export**: Export script outputs to PDF format
- 🎨 **Dark Theme**: Easy on the eyes with modern dark theme

## Supported Script Types

- Python (.py)
- Shell Scripts (.sh, .bash)
- Perl (.pl)
- Ruby (.rb)
- JavaScript (.js)
- PHP (.php)

## Installation

### Linux

#### Option 1: Using .deb package (Recommended for Debian/Ubuntu)

Download the latest .deb package:
wget <https://github.com/h4636oh/shogun_scripts/releases/latest/download/shogunscripts_1.0-1.deb>

Install the package:
sudo dpkg -i shogunscripts_1.0-1.deb
sudo apt-get install -f  # Install any missing dependencies

#### Option 2: Manual Installation

1. Clone the repository:
   git clone <https://github.com/h4636oh/shogun_scripts.git>
   cd shogun_scripts

2. Install dependencies:
   pip install -r requirements.txt

3. Build the application:
   pyinstaller app.spec

4. Install the application:
   sudo chmod +x install.sh
   sudo ./install.sh

After installation, you can:

- Launch from your applications menu
- Run from terminal: `ShogunScripts`

### Windows

#### Option 1: Using Installer (Recommended)

1. Download the latest installer from the releases page
2. Run the installer (ShogunScripts-Setup.exe)
3. Follow the installation wizard

#### Option 2: Portable Version

1. Download the latest zip file from releases
2. Extract the zip file
3. Run ShogunScripts.exe from the extracted folder

## Usage

1. **Select Scripts Folder**
   - Click "Select Folder" button
   - Choose a folder containing your scripts

2. **Select Scripts**
   - Browse through your scripts
   - Use search to filter scripts
   - Toggle regex search for advanced filtering
   - Select multiple scripts to run

3. **Run Scripts**
   - Click "Run Selected" to execute scripts
   - Monitor progress in real-time
   - View outputs as they are generated

4. **View Results**
   - Check script execution status
   - Expand script entries to view full output
   - Export results to PDF if needed

## Uninstallation

### Linux Uninstallation

If installed via .deb package:
sudo dpkg -r shogunscripts

If installed manually:
sudo rm -f /usr/local/bin/ShogunScripts
sudo rm -f /usr/share/applications/shogunscripts.desktop
sudo rm -f /usr/share/icons/hicolor/256x256/apps/shogunscripts.png

### Windows Uninstallation

- Use Windows Settings > Apps > Apps & features
- Or use Control Panel > Programs > Uninstall a program

## Requirements

- Python 3.6 or higher
- PySide6 >= 6.8.2
- FPDF >= 1.7.2

## Development

To set up the development environment:

1. Clone the repository:
   git clone <https://github.com/h4636oh/shogun_scripts.git>

2. Install development dependencies:
   pip install -r requirements.txt

3. Run the application:
   python main.py

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions:

- Open an issue on GitHub
- Contact: <mailto:h4636oh@tuta.io>
