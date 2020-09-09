from kivy.app import App 
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image 


class MainApp(App):
    def on_start(self):
        print("aqui")
        Clock.schedule_interval(self.update_label,1)
    
    def update_label(self, *args):
        print("Aqui")
        print(self.root.ids.ima1.source)
        print( self.root.ids.counter.text)
        self.root.ids.counter.text =str(int(self.root.ids.counter.text)+1)
        #self.root.ids.input.text =str(int(self.root.ids.counter.text)+1)
        if int(self.root.ids.counter.text)>= 1 and int(self.root.ids.counter.text)<= 2 :
            self.cleanIamgen()
            self.root.ids.ima1.source=str('imagen/pictogramas/Caballo v.3.png') 

        if int(self.root.ids.counter.text)>= 3 and int(self.root.ids.counter.text)<= 4 :
            self.cleanIamgen()
            self.root.ids.ima2.source=str('imagen/pictogramas/Chancho v.3.png') 

        if int(self.root.ids.counter.text)>= 5 and int(self.root.ids.counter.text)<= 6 :
            self.cleanIamgen()
            self.root.ids.ima3.source=str('imagen/pictogramas/Manzana v.3.png') 
        if int (self.root.ids.counter.text)==7:
            self.cleanIamgen()
            print("Entro")
            self.root.ids.counter.text="0"



    def cleanIamgen(self):
        self.root.ids.ima1.source=str('imagen/pictogramas/Caballo v.2.png') 
        self.root.ids.ima2.source=str('imagen/pictogramas/Chancho v.2.png') 
        self.root.ids.ima3.source=str('imagen/pictogramas/Manzana v.2.png') 

        

MainApp().run()