import customtkinter
from functools import partial
from enum import Enum, auto

class ViewEnum(Enum):
    SPLASH_SCREEN = 1
    NEW_DATASET = 2
    LOAD_DIRECTORY = 3

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Hello world")
        self.geometry(f"{1100}x{740}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.views = {}

        splashScreenFrame = SplashScreen(self)
        splashScreenFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.views[ViewEnum.SPLASH_SCREEN] = splashScreenFrame

        loadDirectoryFrame = LoadDirectory(self)
        loadDirectoryFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.views[ViewEnum.LOAD_DIRECTORY] = loadDirectoryFrame

        self.showView(ViewEnum.SPLASH_SCREEN)

    def showView(self, view: ViewEnum):
        if view in self.views:
            frame = self.views[view]
            frame.tkraise()

class SplashScreen(customtkinter.CTkFrame):
    def __init__(self, app):
        super().__init__(app)

        self.createDataset = customtkinter.CTkButton(self, text="Create dataset", command=partial(app.showView, ViewEnum.NEW_DATASET))
        self.createDataset.grid(row=0, column=0, padx=5, sticky="ew")

        self.loadDirectory = customtkinter.CTkButton(self, text="Load directory", command=partial(app.showView, ViewEnum.LOAD_DIRECTORY))
        self.loadDirectory.grid(row=0, column=1, padx=5, sticky="ew")

class LoadDirectory(customtkinter.CTkFrame):
    def __init__(self, app):
        super().__init__(app)
        #self.grid_columnconfigure(0, weight=1)

        self.directoryPath = customtkinter.StringVar()

        # Directory path Input
        self.directoryPathLabel = customtkinter.CTkLabel(self, text="Directory Path:")
        self.directoryPathLabel.grid(row=0, column=0)
        self.entry = customtkinter.CTkEntry(self, textvariable=self.directoryPath)
        self.entry.grid(row=1, column=0, sticky="ew")

        # Submit button
        self.submitButton = customtkinter.CTkButton(self, text="Submit", command=self.submit)
        self.submitButton.grid(row=2, column=0)

    def submit(self):
        print(self.directoryPath.get())

"""
import tkinter

import customtkinter
import customtkinter as ctk

from functools import partial


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

"""