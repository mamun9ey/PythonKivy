from kivymd.app import MDApp
from kivy.core.text import LabelBase

LabelBase.register(name="OpenSans",
                   fn_regular= "OpenSans-Regular.ttf"
                   )

class Login(MDApp):
    def build(self):
        return

Login().run()