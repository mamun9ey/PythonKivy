import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    #Initialize infinite keywords
    def _init_(self, **kwargs):
        #call grid layout constructor
        super(MyGridLayout, self)._init_(**kwargs)
        #self colums
        self.cols = 2
        
        #Add widgets
        self.add_widget(Label(text="Name: "))
        #Add input box
        self.name= TextInput(multiline=False)
        self.add_widget(self.name)
        
        #Add widgets
        self.add_widget(Label(text="Food: "))
        #Add input box
        self.pizza= TextInput(multiline=False)
        self.add_widget(self.pizza)
        
        #Add widgets
        self.add_widget(Label(text="Color: "))
        #Add input box
        self.color= TextInput(multiline=False)
        self.add_widget(self.color)
        
class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    MyApp().run()