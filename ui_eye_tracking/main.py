from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.image import Image 
from kivy.uix.widget import Widget 
from kivy.uix.boxlayout import BoxLayout

class TestApp(App):
    def build(self):

        self.superBox        = BoxLayout(orientation='vertical')

        self.horizontalBox   = BoxLayout(orientation='horizontal')

        #img1 =Image(source ='/Users/juanpi/Documents/IngeniusFolder/ui_eye_tracking/imagen/pictogramas/Caballo v.2.png') 
        self.button1= Button(background_normal = '/Users/juanpi/Documents/IngeniusFolder/ui_eye_tracking/imagen/pictogramas/Naranja v.2.png',size_hint = (.5, .5))
        
        #img2 =Image(source ='/Users/juanpi/Documents/IngeniusFolder/ui_eye_tracking/imagen/pictogramas/Gato v.2.png') 
        self.button2= Button(background_normal = '/Users/juanpi/Documents/IngeniusFolder/ui_eye_tracking/imagen/pictogramas/Gato v.2.png',size_hint = (.5, .5))
        
        #img3 =Image(source ='/Users/juanpi/Documents/IngeniusFolder/ui_eye_tracking/imagen/pictogramas/Limon v.2.png') 
        self.button3= Button(background_normal = '/Users/juanpi/Documents/IngeniusFolder/ui_eye_tracking/imagen/pictogramas/Limon v.2.png',size_hint = (.5, .5))
    


        self.horizontalBox.add_widget(self.button1)

        self.horizontalBox.add_widget(self.button2)
        self.horizontalBox.add_widget(self.button3)

        self.verticalBox     = BoxLayout(orientation='vertical')

        self.button3         = Button(background_normal = '/Users/juanpi/Documents/IngeniusFolder/ui_eye_tracking/imagen/pictogramas/Naranja v.2.png')

        self.button4         = Button(text="Four")


        self.verticalBox.add_widget(self.button3)

        self.verticalBox.add_widget(self.button4)

        self.superBox.add_widget(self.horizontalBox)

        self.superBox.add_widget(self.verticalBox)


        return self.superBox
    
    def update(self):
        self.button3  = Button(background_normal = '/Users/juanpi/Documents/IngeniusFolder/ui_eye_tracking/imagen/pictogramas/Sandia v.2.png')
        

app=TestApp()
app.run()
while True:
    app.update()