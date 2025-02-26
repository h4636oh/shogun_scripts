#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Print colored status messages
print_status() {
    echo -e "${GREEN}[*] $1${NC}"
}

print_error() {
    echo -e "${RED}[!] Error: $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}[!] Warning: $1${NC}"
}

# Function to build Linux version
build_linux() {
    print_status "Starting Linux build..."
    
    # Install required packages for Linux
    print_status "Installing Linux requirements..."
    pip install -r requirements.txt || {
        print_error "Failed to install Linux requirements"
        return 1
    }
    
    # Build Linux executable
    print_status "Building Linux executable..."
    pyinstaller app.spec || {
        print_error "Failed to build Linux executable"
        return 1
    }
    
    # Create desktop file
    print_status "Creating desktop entry..."
    cat > shogunscripts.desktop << EOL
[Desktop Entry]
Name=Shogun Scripts
Exec=ShogunScripts
Icon=/usr/share/icons/hicolor/256x256/apps/shogunscripts.png
Type=Application
Categories=Utility;
EOL
    
    # Create installation package in dist folder
    print_status "Creating Linux distribution package..."
    cd dist
    tar -czf "ShogunScripts-linux.tar.gz" "ShogunScripts" "../dist/shogunscripts.desktop" || {
        print_error "Failed to create Linux package"
        cd ..
        return 1
    }
    cd ..
    
    print_status "Linux build complete! Package created: dist/ShogunScripts-linux.tar.gz"
}

# Function to build Windows version
build_windows() {
    print_status "Starting Windows build..."
    
    # Check if Wine is installed
    if ! command -v wine &> /dev/null; then
        print_error "Wine is not installed. Please install wine first."
        return 1
    fi
    
    # Set up Wine environment
    export WINEPREFIX=~/.wine
    export WINEARCH=win64
    
    # Python version to install
    PYTHON_VERSION="3.9.0"
    PYTHON_INSTALLER="python-${PYTHON_VERSION}-amd64.exe"
    PYTHON_URL="https://www.python.org/ftp/python/${PYTHON_VERSION}/${PYTHON_INSTALLER}"
    
    # Download Python installer if not exists
    if [ ! -f "$PYTHON_INSTALLER" ]; then
        print_status "Downloading Python ${PYTHON_VERSION} for Windows..."
        wget "$PYTHON_URL" || {
            print_error "Failed to download Python installer"
            return 1
        }
    fi
    
    # Install Python if not already installed
    if ! wine python --version &> /dev/null; then
        print_status "Installing Python ${PYTHON_VERSION}..."
        wine "$PYTHON_INSTALLER" /quiet InstallAllUsers=1 PrependPath=1 || {
            print_error "Failed to install Python"
            return 1
        }
        sleep 5
    else
        print_warning "Python already installed in Wine"
    fi
    
    # Install required packages
    print_status "Installing Windows requirements..."
    wine python -m pip install --upgrade pip
    wine python -m pip install pyinstaller
    wine python -m pip install -r requirements.txt || {
        print_error "Failed to install Windows requirements"
        return 1
    }
    
    # Build Windows executable
    print_status "Building Windows executable..."
    wine python -m PyInstaller app.spec || {
        print_error "Failed to build Windows executable"
        return 1
    }
    
    # Create Windows distribution in dist folder
    print_status "Creating Windows distribution package..."
    cd dist
    mv ShogunScripts ShogunScripts-win # Rename to avoid conflicts with Linux build
    zip -r "ShogunScripts-windows.zip" "ShogunScripts-win" || {
        print_error "Failed to create Windows package"
        cd ..
        return 1
    }
    cd ..
    
    # Clean up
    print_status "Cleaning up Windows build files..."
    rm -f "$PYTHON_INSTALLER"
    
    print_status "Windows build complete! Package created: dist/ShogunScripts-windows.zip"
}

# Function to clean dist directory
clean_dist() {
    print_status "Cleaning dist directory..."
    rm -rf dist build
    mkdir -p dist
}

# Main script
print_status "ShogunScripts Build Script"
echo "------------------------"
echo "1. Build for Linux"
echo "2. Build for Windows"
echo "3. Build for both platforms"
echo "4. Clean and exit"
echo "------------------------"
read -p "Select an option (1-4): " choice

case $choice in
    1)
        clean_dist
        build_linux
        ;;
    2)
        clean_dist
        build_windows
        ;;
    3)
        print_status "Building for both platforms..."
        clean_dist
        build_linux
        build_windows
        ;;
    4)
        clean_dist
        print_status "Cleaned up and exiting..."
        exit 0
        ;;
    *)
        print_error "Invalid option"
        exit 1
        ;;
esac

print_status "Build process completed! Distribution packages are in the dist folder:"
if [ -f "dist/ShogunScripts-linux.tar.gz" ]; then
    print_status "- Linux package: dist/ShogunScripts-linux.tar.gz"
fi
if [ -f "dist/ShogunScripts-windows.zip" ]; then
    print_status "- Windows package: dist/ShogunScripts-windows.zip"
fi
print_warning "Remember to test the builds thoroughly before distribution!" 