# works on systems with built in camera
# "speak" button closes the app

import tkinter
import cv2
from PIL import Image
from PIL import ImageTk
import time


class Video_App:

    def __init__(self, master, master_title, video_source=0):
        self.master = master
        master.title = master_title
        self.master.attributes('-fullscreen', True)

        self.master.update()

        self.width = self.master.winfo_width()
        self.height = self.master.winfo_height()

        print(self.width, self.height)


        # open video source
        self.vid = MyVideoCapture(self.width, self.height, video_source)

        # create and place frame to hold UI elements
        self.frame = tkinter.Frame(
            self.master,
            bg="orange",
            width=self.width,
            height=self.height
        )

        self.frame.grid()

        
        # create and place Frame to hold the video
        self.video_canvas = tkinter.Canvas(
            self.frame,
            bg="black",
            width=self.width,
            height=self.height,
            bd=0,
            highlightthickness=0
        )

        self.video_canvas.grid(
            row=0,
            column=0,
            rowspan=10,
            columnspan=3
        )


        # create and place play button
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

        # create and place stop button
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

        # After it is called once, the update method will be automatically called every delay millpip install Pillowiseconds
        self.delay = 15
        self.update()

        self.master.mainloop()

    
    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
            self.video_canvas.create_image(self.width/2, self.height/2, image = self.photo, anchor=tkinter.CENTER)

        self.master.after(self.delay, self.update)


class MyVideoCapture:

    def __init__(self, width, height, video_source = 0):
        # open video source
        self.vid = cv2.VideoCapture(video_source)
        # check for error opening video source
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
        self.vid.set(3, width)
        self.vid.set(4, height)



    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return(ret, None)
        else:
            return(ret, None)


    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


Video_App(tkinter.Tk(), "Test Tkinter and OpenCV")