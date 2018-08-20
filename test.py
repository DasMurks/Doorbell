from tkinter import *


root = Tk()
root.title("Doorbell")
root.attributes("-fullscreen", True)

root.update()

frame = Frame(
            root,
            bg = "black",
            width = root.winfo_width(),
            height = root.winfo_height()
            )

frame.grid()

video_frame = Frame(
                frame,
                bg = "",
                width = root.winfo_width(),
                height = root.winfo_height()
                )

video_frame.grid(
                row = 0,
                column = 0,
                rowspan = 10,
                columnspan = 3,
                sticky = N+S+E+W
                )

button_camera_on = Button(
                        frame,
                        text = "Camera On",
                        font = ("Arial", int(root.winfo_height()/20)),
                        bg = "green",
                        activebackground = "lightgreen",
                        fg = "black"
                        )

button_camera_on.grid(
                    row = 9,
                    column = 0,
                    sticky = S
                    )

button_camera_off = Button(
                        frame,
                        text = "Camera Off",
                        font = ("Arial", int(root.winfo_height()/20)),
                        bg = "darkred",
                        activebackground = "red",
                        fg = "black"
                        )
button_camera_off.grid(
                    row = 9,
                    column = 1,
                    sticky = S
                    )

button_speak = Button(
                    frame,
                    text = "Speak",
                    font = ("Arial", int(root.winfo_height()/20)),
                    bg = "blue",
                    activebackground = "lightblue",
                    fg = "white",
                    command = root.destroy
                    )

button_speak.grid(
                row = 9,
                column = 2,
                sticky = S
                )


root.mainloop()