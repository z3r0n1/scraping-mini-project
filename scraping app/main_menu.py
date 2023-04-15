import tkinter as tk
import ctypes

import clock as CK
import buttons as BTNS
import buttons_frames as BTNSF

class main_menu():
    def __init__(self, master, root):
        # config
        self.user32 = ctypes.windll.user32
        self.width= int(self.user32.GetSystemMetrics(0)*65/100)
        self.height= int(self.user32.GetSystemMetrics(1)*55/100)
        self.widgets_color= 'black'

        # main frame
        self.main_frame= tk.Frame(master)
        self.main_frame.config(
            width= self.width,
            height= self.height,
            bg= self.widgets_color,
            )
        self.main_frame.place(
            anchor= 'center',
            relx= 0.5,
            rely= 0.5,
            )

        # menu frame
        self.menu_frame= tk.Frame(root)
        self.menu_frame.config(
            width= (self.width*20/100)-10,
            height= self.height-15,
            bg= self.widgets_color,
            bd= 2,
            relief= "raised",
            )
        self.menu_frame.place(
            anchor= 'w',
            relx= 0.005,
            rely= 0.5,
            )
        self.menu_frame.propagate(False) # Don't want the frame to adapt with the content

        # buttons frame
        root.update_idletasks() # Useful when you need to use winfo, it returns 1 other way
        self.buttons_frame= tk.Frame(self.menu_frame)
        self.buttons_frame.config(
            width= self.menu_frame.winfo_width()*98/100,
            height= self.menu_frame.winfo_height()*10/100,
            bg= self.widgets_color,
            bd= 1,
            relief= 'ridge',
        )
        self.buttons_frame.place(
            anchor= 'n',
            relx= 0.495,
            rely= 0.002,
        )

        # clock
        root.update_idletasks()
        self.clock= CK.Clock(self.buttons_frame, int(self.buttons_frame.winfo_width()*4/100), int(self.buttons_frame.winfo_height()*4/100))

        # menu options
        root.update_idletasks()
        self.menu_options= tk.Frame(self.menu_frame)
        self.menu_options.config(
            width= self.menu_frame.winfo_width()*98/100,
            height= self.menu_frame.winfo_height()*88/100,
            bg= self.widgets_color,
            bd= 1,
            relief= 'ridge',
        )
        self.menu_options.place(
            anchor= 's',
            relx= 0.495,
            rely= 0.995,
        )
        self.menu_options.propagate(False)
        root.update_idletasks()
        buttons_list= []
        text= 'Button '
        n=1
        rely_var= 0.01

        # generating buttons in a loop
        for i in range(3):
            i= tk.Button(self.menu_options)
            buttons_list.append(i)
            i.config(
                width= 24,
                height= 2,
                #padx= 60,
                #pady= 5,
                bg= self.widgets_color,
                fg= 'white',
                bd= 1,
                relief= 'ridge',
            )
            i.place(
                anchor= 'n',
                relx= 0.5,
            )
        # naming buttons in a loop
        for i in buttons_list:
            i.config(
                text= text+str(n),
            )
            i.place(
                rely= rely_var,
            )
            n+= 1
            rely_var+= 0.11

        # renaming buttons
        for i in buttons_list:
            i_config= list(i.config('text'))
            if i_config[-1] == "Button 1":
                i.config(text= "Scraping")
            if i_config[-1] == "Button 2":
                i.config(text= "Dataframe")
            if i_config[-1] == "Button 3":
                i.config(text= "...")

        # visualization frame
        self.visualization_frame= tk.Frame(self.main_frame)
        self.visualization_frame.config(
            width= (self.width*79/100)+5,
            height= self.height-15,
            bg= self.widgets_color,
            bd= 2,
            relief= "raised",
            )
        self.visualization_frame.place(
            anchor= 'e',
            relx= 0.995,
            rely= 0.496,
            )
        
        # buttons commands
        buttons= BTNSF.Buttons_frames(self.visualization_frame)
        def button_1_command():
            for children in self.visualization_frame.winfo_children():
                children.destroy()
            buttons.button1_frame()
        def button_2_command():
            try:
                for children in self.visualization_frame.winfo_children():
                    children.destroy()
                buttons.button2_frame()
            except AttributeError:
                print("Aún no se creó el DataFrame necesario para que se genere el Frame de Button_2_FrameF")
        for i in buttons_list:
            i_config= list(i.config('text'))
            if i_config[-1] == 'Scraping':
                i.config(
                    command= button_1_command
                )
            if i_config[-1] == 'Dataframe':
                i.config(
                    command= button_2_command
                )

        self.clean_button= BTNS.Buttons.clean_button(self.buttons_frame, self.visualization_frame)