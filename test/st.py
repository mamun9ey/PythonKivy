from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDRaisedButton
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout



class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class studentmanagementsystem(MDApp):
    def build(self):
        #return Builder.load_string(KV)
        return Builder.load_file("st.kv")


studentmanagementsystem().run()