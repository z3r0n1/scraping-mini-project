import tkinter as tk

class Buttons():
    def __init__(self, master):
        self.master= master
    def clean_button(master, frame_to_clean):
        def clean_children():
            for children in frame_to_clean.winfo_children():
                children.destroy()
        clean_button= tk.Button(master)
        clean_button.config(
            width= 2,
            height= 1,
            bg= 'black',
            fg= 'yellow',
            text= '[C]',
            bd= 1,
            relief= "ridge",
            command= clean_children,
        )
        clean_button.place(
            anchor='w',
            relx=0.015,
            rely=0.5,
        )
