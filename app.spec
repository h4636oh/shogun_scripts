# -*- mode: python ; coding: utf-8 -*-
import os
import platform

block_cipher = None

# Determine icon file based on platform
if platform.system() == "Windows":
    icon_file = os.path.join('ui', 'icons', 'app', 'app.ico')
else:  # Linux
    icon_file = os.path.join('ui', 'icons', 'app', 'app.png')

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('ui/*.ui', 'ui'),                  # UI files
        ('ui/*.qss', 'ui'),                 # Style files
        ('ui/icons/*.svg', 'ui/icons'),     # SVG icons
        ('ui/icons/app/*', 'ui/icons/app'), # App icons
        ('ui_functions/*.py', 'ui_functions'), # UI function modules
        ('ui/style.qss', 'ui'),            # Explicit style.qss inclusion
    ],
    hiddenimports=[
        # PySide6 core components
        'PySide6.QtCore',
        'PySide6.QtGui',
        'PySide6.QtWidgets',
        'PySide6.QtUiTools',
        'PySide6.QtXml',
        'PySide6.QtSvg',
        
        # Project modules
        'ui.resources_rc',
        'ui.theme_manager',
        'ui_functions.style_watcher',
        'ui_functions.homepage',
        'ui_functions.scripts_selection',
        'ui_functions.progress_bar',
        'ui_functions.scripts_output',
        
        # Standard library modules used
        'os',
        'sys',
        're',
        'datetime',
        'subprocess',
        'platform',
        
        # External dependencies
        'fpdf',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ShogunScripts',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon=icon_file if os.path.exists(icon_file) else None
)

# For Linux, create .desktop file
if platform.system() == "Linux":
    import shutil
    desktop_file = """[Desktop Entry]
Name=Shogun Scripts
Exec=ShogunScripts
Icon=/usr/share/icons/hicolor/256x256/apps/shogunscripts.png
Type=Application
Categories=Utility;
"""
    with open('shogunscripts.desktop', 'w') as f:
        f.write(desktop_file) 