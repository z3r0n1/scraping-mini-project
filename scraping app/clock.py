from tkinter import Label
from time import strftime

class Clock():
    def __init__(self, master, width, height):
        self.clock= Label(master)
        self.clock.config(
            width= width,
            height= height,
            bg= "black",
            fg= "white",
            text= "",
            bd= 1,
            relief= "ridge",
        )
        self.clock.place(
            relx= 0.5,
            rely= 0.5,
            anchor= "center",
        )
        self.clock.propagate(False)

        def time():
            current_time= strftime("%H:%M:%S")
            self.clock.config(text= current_time)
            self.clock.after(500, time)
        time()