import os
import sys

sys.path.append(os.getcwd())

from modules.ui.MainUI import App

def main():
    ui = App()
    ui.mainloop()
    ui.close()

if __name__ == "__main__":
    main()