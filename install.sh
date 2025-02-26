#!/bin/bash
# Copy application
sudo cp dist/ShogunScripts /usr/local/bin/
# Copy desktop file
sudo cp dist/shogunscripts.desktop /usr/share/applications/
# Copy icon
sudo mkdir -p /usr/share/icons/hicolor/256x256/apps/
sudo cp ui/icons/app/app.png /usr/share/icons/hicolor/256x256/apps/shogunscripts.png 