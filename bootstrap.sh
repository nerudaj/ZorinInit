#!/bin/bash

# Install packages
apt install tiled code
snap install gimp
flatpak install org.videolan.VLC
flatpak install io.github.shiftey.Desktop
flatpak install org.gimp.Gimp

# Set up Nautilus context menu extensions
mkdir -p ~/.local/share/nautilus-python/extensions

cp ./nautilus-extensions/* ~/.local/share/nautilus-python/extensions
chmod +x ~/.local/share/nautilus-python/extensions/*

nautilus -q

# Install custom theme
cp -r ./themes/ZorinLight-Green ~/.themes

# Install keyboard
cp ./keyboard/cz_custom /usr/share/X11/xkb/symbols/cz_custom
cp -f ./keyboard/evdev.xml /usr/share/X11/xkb/rules/evdev.xml

# Install onedriver service
cp ./services/onedriver.service /etc/systemd/system/onedriver.service
# TODO: register
