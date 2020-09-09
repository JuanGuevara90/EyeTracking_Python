from kivy.app import App
from kivy.base import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget 
from kivy.uix.button import Button
from kivy.uix.image import Image 

Builder.load_string("""
<rootwi>:
    orientation:'vertical'

    BoxLayout:
        padding:5
        Image:
            source:"imagen/pictogramas/Caballo v.3.png"
            size_hint_x: 0.4
            allow_stretch: True

        Image:
            source:"imagen/pictogramas/Chancho v.2.png"
            size_hint_x: 0.4
            allow_stretch: True
        
        Image:
            source:"imagen/pictogramas/Caballo v.2.png"
            size_hint_x: 0.4
            allow_stretch: True
    
    BoxLayout:
        padding:5
        Image:
            source:"imagen/pictogramas/Caballo v.2.png"
            size_hint_x: 0.4
            allow_stretch: True

        Image:
            source:"imagen/pictogramas/Chancho v.2.png"
            size_hint_x: 0.4
            allow_stretch: True
        
        Image:
            source:"imagen/pictogramas/Caballo v.2.png"
            size_hint_x: 0.4
            allow_stretch: True
    
    BoxLayout:
        padding:5
        Image:
            source:"imagen/pictogramas/Caballo v.2.png"
            size_hint_x: 0.4
            allow_stretch: True

        Image:
            source:"imagen/pictogramas/Chancho v.2.png"
            size_hint_x: 0.4
            allow_stretch: True
        
        Image:
            source:"imagen/pictogramas/Caballo v.2.png"
            size_hint_x: 0.4
            allow_stretch: True
    
    BoxLayout:
        padding:5
        Image:
            source:"imagen/pictogramas/Caballo v.2.png"
            size_hint_x: 0.4
            allow_stretch: True

        Image:
            source:"imagen/pictogramas/Chancho v.2.png"
            size_hint_x: 0.4
            allow_stretch: True
        
        Image:
            source:"imagen/pictogramas/Caballo v.2.png"
            size_hint_x: 0.4
            allow_stretch: True

""")
class rootwi(BoxLayout):
    pass


class MyApp(App):
    def build(self):
        s = Widget() 
        self.img =Image(source ='/Users/juanpi/Documents/IngeniusFolder/ui_eye_tracking/imagen/pictogramas/Caballo v.2.png') 
        self.img.pos = (200, 100) 

        s.add_widget(s)
        s.add_widget(rootwi())
        return s

if __name__ == '__main__':
    MyApp().run()