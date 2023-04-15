import tkinter as tk
import ctypes

import main_menu as MainM

class Root_Window():
    def __init__(self):
        self.root= tk.Tk()
        self.root.title("Z3R0N1")
        self.user32 = ctypes.windll.user32
        self.width= int(self.user32.GetSystemMetrics(0)*65/100)
        self.height= int(self.user32.GetSystemMetrics(1)*55/100)
        self.x_pos= int(self.user32.GetSystemMetrics(0)*15/100)
        self.y_pos= int(self.user32.GetSystemMetrics(1)*15/100)
        self.root.geometry(str(str(self.width)+'x'+str(self.height)+'+'+str(self.x_pos)+'+'+str(self.y_pos)))
        self.root.resizable(False, False)
        self.root.overrideredirect(False)

        # invisible frame
        self.invisible_window= tk.Frame()
        self.invisible_window.config(
            width= self.width,
            height= self.height,
            bg= 'white'
            )
        self.invisible_window.place(
            anchor= 'center',
            relx= 0.5,
            rely= 0.5,
            )
        
        # main menu
        main_menu= MainM.main_menu(self.invisible_window, self.root)

        self.root.mainloop()

