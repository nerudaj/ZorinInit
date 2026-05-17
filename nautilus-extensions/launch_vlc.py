#!/usr/bin/env python3

import subprocess
from gi.repository import Nautilus, GObject

class VlcProvider(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass
    
    def get_file_items(self, files):
        item = Nautilus.MenuItem(
            name="VLC::open",
            label="Open in VLC",
            tip="Open file/folder in VLC",
        )
        
        if len(files) == 1:
            item.connect("activate", self.open_folder_in_vlc, files[0])
        else:
            item.connect("activate", self.open_in_vlc, files)
        return [item]
    
    # Handle right-click on background (empty space)
    def get_background_items(self, current_folder):
        item = Nautilus.MenuItem(
            name="VLC::open",
            label="Open in VLC",
            tip="Open files/folder in VLC",
        )
        
        item.connect("activate", self.open_folder_in_vlc, current_folder)
        return [item]
    
    def open_in_vlc(self, menu, items):
        args = ["flatpak", "run", "org.videolan.VLC"]
        for item in items:
            args.append(item.get_location().get_path())
        subprocess.Popen(args)

    def open_folder_in_vlc(self, menu, folder):
        subprocess.Popen(["flatpak", "run", "org.videolan.VLC", folder.get_location().get_path()])
