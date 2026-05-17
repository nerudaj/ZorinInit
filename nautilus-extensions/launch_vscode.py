#!/usr/bin/env python3

import subprocess
from gi.repository import Nautilus, GObject

class VSCodeProvier(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass
    
    def get_file_items(self, files):
        if len(files) != 1:
            return []
        
        item = Nautilus.MenuItem(
            name="VSCode::open_workspace",
            label="Open in VS Code",
            tip="Open file/folder in Visual Studio Code",
        )
        
        item.connect("activate", self.open_in_vscode, files[0])
        return [item]
    
    # Handle right-click on background (empty space)
    def get_background_items(self, current_folder):
        item = Nautilus.MenuItem(
            name="VSCode::open_workspace",
            label="Open in VS Code",
            tip="Open file/folder in Visual Studio Code",
        )
        
        item.connect("activate", self.open_in_vscode, current_folder)
        return [item]
    
    def open_in_vscode(self, menu, item):
        subprocess.Popen(["code", item.get_location().get_path()])

