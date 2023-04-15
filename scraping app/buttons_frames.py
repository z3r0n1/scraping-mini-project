import tkinter as tk
from tkinter import ttk
import time
from threading import Thread
from PIL import Image, ImageTk

import scraping

class Buttons_frames():
    def __init__(self, master):
        self.master = master

    def button1_frame(self):
        global kyokulogo
        global kyokulogo2

        self.Button_1_FrameF= tk.Frame(self.master)
        self.Button_1_FrameF.config(
            width= self.master.winfo_width()*99/100,
            height= self.master.winfo_height()*99/100,
            bg= 'black',
            bd= 2,
            relief= 'raised'
            )
        
        def kyokulogo_button_command():
            # ctrl_text_var
            self.ctrl_text_var= tk.StringVar(value= "[Load description]")

            # ctrl_float_var
            self.ctrl_float_var= tk.DoubleVar(value= 0.0)

            # Label
            self.progress_label= tk.Label(self.Button_1_FrameF)
            self.progress_label.config(
                textvariable= self.ctrl_text_var,
                justify="left",
                fg= "white",
                bg= "black",
            )
            self.progress_label.place(
                anchor= "w",
                relx= 0.385,
                rely= 0.80,
            )
            # Progress Bar
            self.progress_bar= ttk.Progressbar(self.Button_1_FrameF)
            self.progress_bar.config(
                variable= self.ctrl_float_var,
                orient= "horizontal",
                length= 250,
            )
            self.progress_bar.place(
                anchor= "center",
                relx= 0.5,
                rely= 0.85,
            )

            def do_progressive_scraping():
                img_url= scraping.do_scraping.step1_request()
                scraping.do_scraping.step2_download(img_url)
                DataFrame= scraping.do_scraping.step3_dataframe()

                text= ["Starting the scraping work: request","Starting the scraping work: creating soup","Starting the scraping work: getting URL","Downloading the image you requested","Creating the DataFrame"]

                def change_progress_bar_text():
                    for i in text:
                        self.ctrl_text_var.set(i)
                        time.sleep(2)

                y= Thread(target=change_progress_bar_text)
                y.start()

                def change_progress_bar_val():
                    for i in range(100):
                        self.ctrl_float_var.set(i)
                        time.sleep(0.1)
                    done_label= tk.Label(self.Button_1_FrameF, text="Done", fg="white", bg="black")
                    done_label.place(anchor= "center", relx= 0.65, rely=0.85)

                x= Thread(target=change_progress_bar_val)
                x.start()
                return DataFrame
            
            self.DataFrame= do_progressive_scraping()

        kyokulogo = Image.open(r"D:/PYTHON FILES/Web Scraping/img/Kanku_Kyokushin.png")
        kyokulogo = kyokulogo.resize((150, 150))
        kyokulogo = ImageTk.PhotoImage(kyokulogo)
        self.kyokulogo_button = tk.Button(self.Button_1_FrameF)
        self.kyokulogo_button.config(
            width= 150,
            height= 150,
            bg= "black",
            activebackground= "black",
            image= kyokulogo,
            borderwidth= 0,
            command= kyokulogo_button_command,
        )

        kyokulogo2 = Image.open(r"D:/PYTHON FILES/Web Scraping/img/Kanji_Kyokushin.png")
        kyokulogo2 = kyokulogo2.resize((185, 225))
        kyokulogo2 = ImageTk.PhotoImage(kyokulogo2)
        self.kyokulogo2_label = tk.Label(self.Button_1_FrameF)
        self.kyokulogo2_label.config(
            width= 55,
            height= 225,
            bg= "black",
            image= kyokulogo2,
            borderwidth= 0,
        )

        self.kyokulogo2_label.place(
            anchor= "n",
            relx= 0.5,
            rely= 0.32,
        )

        self.kyokulogo_button.place(
            anchor= "n",
            relx= 0.5,
            rely= 0.05,
        )

        self.Button_1_FrameF.place(
            anchor= 'center',
            rely= 0.497,
            relx= 0.498,
            )
    
    def button2_frame(self):
        try:
            DataFrame= self.DataFrame
            self.Button_2_FrameF= tk.Frame(self.master)
            self.Button_2_FrameF.config(
                width= self.master.winfo_width()*99/100,
                height= self.master.winfo_height()*99/100,
                bg= 'black',
                bd= 2,
                relief= 'raised'
                )

            # 13 elementos en cada fila. 52 en total, 56 con los títulos.
            # COL1 posicion
            self.col1frame= tk.Frame(self.Button_2_FrameF)
            self.col1frame.config(
                width= 175,
                height= 450,
                bg= "white",
            )
            title1= tk.Label(self.Button_2_FrameF)
            title1.config(
                text= "Posición",
                font= ('Helvetica 14 bold'),
                fg= "white",
                bg= "black",
            )
            title1.place(
                anchor= "center",
                relx= 0.2,
                rely= 0.15,
            )

            for i in range(13):
                button= tk.Button(self.col1frame)
                button.config(
                    width= 20,
                    height= 1,
                    text= self.DataFrame.iloc[i,0],
                    fg= "white",
                    bg= "black",
                )
                button.grid(row=i, column=0, sticky="ew", pady= 0)

            self.col1frame.place(
                anchor= "center",
                relx= 0.2,
                rely= 0.5,
            )

            # COL2 nombre
            self.col2frame= tk.Frame(self.Button_2_FrameF)
            self.col2frame.config(
                width= 175,
                height= 450,
                bg= "white",
            )

            title2= tk.Label(self.Button_2_FrameF)
            title2.config(
                text= "Nombre",
                font= ('Helvetica 14 bold'),
                fg= "white",
                bg= "black",
            )
            title2.place(
                anchor= "center",
                relx= 0.4,
                rely= 0.15,
            )

            for i in range(13):
                button= tk.Button(self.col2frame)
                button.config(
                    width= 20,
                    height= 1,
                    text= self.DataFrame.iloc[i,1],
                    fg= "white",
                    bg= "black",
                )
                button.grid(row=i, column=0, sticky="ew", pady= 0)

            self.col2frame.place(
                anchor= "center",
                relx= 0.4,
                rely= 0.5,
            )

            # COL3 sexo
            self.col3frame= tk.Frame(self.Button_2_FrameF)
            self.col3frame.config(
                width= 175,
                height= 450,
                bg= "white",
            )

            title3= tk.Label(self.Button_2_FrameF)
            title3.config(
                text= "Sexo",
                font= ('Helvetica 14 bold'),
                fg= "white",
                bg= "black",
            )
            title3.place(
                anchor= "center",
                relx= 0.6,
                rely= 0.15,
            )

            for i in range(13):
                button= tk.Button(self.col3frame)
                button.config(
                    width= 20,
                    height= 1,
                    text= self.DataFrame.iloc[i,2],
                    fg= "white",
                    bg= "black",
                )
                button.grid(row=i, column=0, sticky="ew", pady= 0)

            self.col3frame.place(
                anchor= "center",
                relx= 0.6,
                rely= 0.5,
            )

            # COL4 cargo
            self.col4frame= tk.Frame(self.Button_2_FrameF)
            self.col4frame.config(
                width= 175,
                height= 450,
                bg= "white",
            )

            title4= tk.Label(self.Button_2_FrameF)
            title4.config(
                text= "Cargo",
                font= ('Helvetica 14 bold'),
                fg= "white",
                bg= "black",
            )
            title4.place(
                anchor= "center",
                relx= 0.8,
                rely= 0.15,
            )

            for i in range(13):
                button= tk.Button(self.col4frame)
                button.config(
                    width= 20,
                    height= 1,
                    text= self.DataFrame.iloc[i,3],
                    fg= "white",
                    bg= "black",
                )
                button.grid(row=i, column=0, sticky="ew", pady= 0)

            self.col4frame.place(
                anchor= "center",
                relx= 0.8,
                rely= 0.5,
            )

        except AttributeError:
            error_label= tk.Label(self.master)
            error_label.config(
                text= "[ You have to obtain the DataFrame from Scraping first ]",
                font= ('Helvetica 20 bold'),
                fg= "white",
                bg= "black",
            )
            error_label.place(
                anchor="center",
                relx=0.5,
                rely=0.5,
            )

        self.Button_2_FrameF.place(
            anchor= 'center',
            rely= 0.497,
            relx= 0.498,
            )