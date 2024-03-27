import tkinter

import customtkinter
import customtkinter as ctk

from functools import partial

"""
class SidebarFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class SplashScreen(customtkinter.CTkFrame):
    loadDirectoryButton: customtkinter.CTkButton

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(row=0, column=0, sticky="nsew")
        self.content()

    def _loadDirectory(self):
        print("Loading directory...")
        self.removeView()

    def content(self):
        loadDirectoryButton = customtkinter.CTkButton(self, text="Load directory",  command=self._loadDirectory)
        loadDirectoryButton.grid(row=0, column=0)

    def removeView(self):
        self.pack_forget()
"""

class App(ctk.CTk):
    views = {}
    currentView = None

    def __init__(self):
        super().__init__()

        self.title("Hello world")
        self.geometry(f"{1100}x{740}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create our views
        self.createSplashScreen()
        self.createLoadDataset()

        self.loadViewWithID("splashScreen")

    def createSplashScreen(self):
        frame = customtkinter.CTkFrame(self)
        frame.grid(row=0, column=0, sticky="nsw")
        frame.grid_rowconfigure(0, weight=0)
        frame.grid_rowconfigure(1, weight=1)

        # adding my button to the grid
        button = customtkinter.CTkButton(master=frame, text="Load dataset", command=partial(self.loadViewWithID, "loadDataset"))
        button.grid(row=0, column=0, sticky="nswe")

        button = customtkinter.CTkButton(master=frame, text="Load dataset", command=partial(self.loadViewWithID, "loadDataset"))
        button.grid(row=1, column=0, sticky="w")

        # Adding view to the views obj
        App.views['splashScreen'] = frame

    def createLoadDataset(self):
        frame = customtkinter.CTkFrame(self)

        # adding other button
        button = customtkinter.CTkButton(master=frame, text="Hello world from load dataset", command=partial(self.loadViewWithID, "splashScreen"))
        button.grid(row=0, column=0)

        App.views['loadDataset'] = frame

    def loadViewWithID(self, viewID):
        if App.currentView is not None:
            App.currentView.pack_forget()

        App.currentView = App.views[viewID]
        App.currentView.pack(expand=True)

