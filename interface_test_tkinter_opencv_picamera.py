import tkinter

class Interface:

    def __init__(self, master, master_title):

        self.master = master
        master.title = master_title
        self.master.attributes('-fullscreen', True)

        self.master.update()

        self.frame = tkinter.Frame(self.master, bg="orange", width=self.master.winfo_width(), height=self.master.winfo_height())

        self.frame.grid()

        self.canvas = tkinter.Canvas(self.frame, bg ="black", width=self.master.winfo_width(), height=self.master.winfo_height(), bd=0, highlightthickness=0)

        self.canvas.grid(row=0, column=0, rowspan=10, columnspan=3)


        self.button_camera_on = tkinter.Button(
            self.frame,
            text="Camera On",
            bg="green",
            activebackground="lightgreen",
            fg="black"
        )

        self.button_camera_on.grid(
            row=9,
            column=0,
            sticky=tkinter.S
        )


        self.button_camera_off = tkinter.Button(
            self.frame,
            text="Camera Off",
            bg="darkred",
            activebackground="red",
            fg="black"
        )


        self.button_camera_off.grid(
            row=9,
            column=1,
            sticky=tkinter.S
        )

        # create and place speak button
        self.button_speak = tkinter.Button(
            self.frame,
            text="Speak",
            bg="blue",
            activebackground="lightblue",
            fg="white",
            command=self.master.destroy
        )

        self.button_speak.grid(
            row=9,
            column=2,
            sticky=tkinter.S
        )

        self.master.mainloop()

Interface(tkinter.Tk(), "Interface")