__author__ = 'Ingenius Work'
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.button import Button

from gaze_tracking import GazeTracking
import cv2

import pyglet

class CamApp(App):

    def build(self):
        self.sound = pyglet.media.load("hola.m4a",streaming=False)
        

        self.count=0
        self.gaze = GazeTracking()

        self.img1=Image()
        self.button = Button(text="mode")
        self.img2 = Image(source="imagen/pictogramas/Caballo v.2.png")
        layout = BoxLayout()
        layout.add_widget(self.img1)
        layout.add_widget(self.button)
        layout.add_widget(self.img2)


        #opencv2 stuffs
        self.capture = cv2.VideoCapture(0)
        #cv2.namedWindow("CV2 Image")
        Clock.schedule_interval(self.update, 1.0/33.0)
        return layout


    def update(self, dt):
        #print("aqui")
        # display image from cam in opencv window
        ret, frame = self.capture.read()
        #cv2.imshow("CV2 Image", frame)
        # convert it to texture
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr') 
        #if working on RASPBERRY PI, use colorfmt='rgba' here instead, but stick with "bgr" in blit_buffer. 
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.img1.texture = texture1
        self.button.text=str(self.count)
        self.count= self.count+1

        if self.count ==30:
            self.img2.source="imagen/pictogramas/Chancho v.2.png"
        self.reconocimiento_ojos(frame)

        

    def reconocimiento_ojos(self,frame):
        #Reconocimiento de ojos
        text=""
        self.gaze.refresh(frame)
        if self.gaze.is_blinking():
            text = "Blinking"
            self.sound.play()
        elif self.gaze.is_right():
            text = "Looking right"
        elif self.gaze.is_left():
            text = "Looking left"
        elif self.gaze.is_up():
            text = "Looking up"
        elif self.gaze.is_down():
            text = "Looking down"
        elif self.gaze.is_center():
            text = "Looking center"

        print(text)


if __name__ == '__main__':
    CamApp().run()
    cv2.destroyAllWindows()