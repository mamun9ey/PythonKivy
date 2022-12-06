from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.text import LabelBase
LabelBase.register(name="OpenSans",
                   fn_regular= "OpenSans-Regular.ttf"
                   )

KV = '''
<ContentNavigationDrawer>

    ScrollView:

        MDList:
            Label :
                text : "Navigation"
            OneLineListItem:
                text: "Home"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Students"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"
            OneLineListItem:
                text: "Result"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 3"
            OneLineListItem:
                text: "Academic Records"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 4"
                    
            OneLineListItem:
                text: "Login"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 7"
            OneLineListItem:
                text: "Registration"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 8"


MDScreen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Menu"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager
            
            MDScreen:
                name: "scr 1"
                size_hint : None,None
                size : 1000,800
                MDBoxLayout:
                    size_hint_y: None
                    height: "540dp"
                    orientation: 'vertical'
                
                    FitImage:
                        size_hint_y: 2
                        source: 'image/home.jpg'

            MDScreen:
                name: "scr 2"

                MDLabel:
                    halign: "center"
                    md_bg_color :  [232/255, 232/255, 232/255,1]
                    size_hint : 1,0.9
                    MDScreen :
                        
                        MDCard :
                            size_hint : None,None
                            size : 800,400
                            
                            elevation : 15
                            spacing : 5
                            md_bg_color :  [250/255, 250/255, 250/255,1]
                            orientation : "vertical"
                            padding_y : 15
                            
                            MDBoxLayout:
                                size_hint_y: None
                                height: "160dp"
                                orientation: 'vertical'
                            
                                FitImage:
                                    size_hint_y: 3
                                    source: 'image/1.jpg'
                            
                            MDLabel : 
                                text : 'STUDENT INFORMATION'
                                font_name : "OpenSans"
                                font_style : 'Button'
                                font_size : 35
                                halign : "center"
                                size_hint_y : None
                                height : self.texture_size[1]
                                padding_y : 5
                            MDTextField : 
                                font_name : "OpenSans"
                                hint_text : "Department Name"
                                size_hint_x : None
                                width : 260
                                font_size : 20
                                pos_hint : {"center_x":.5}
                            MDTextField : 
                                font_name : "OpenSans"
                                hint_text : "'Semister'"
                                size_hint_x : None
                                width : 260
                                font_size : 20
                                pos_hint : {"center_x":.5}
                            MDTextField : 
                                font_name : "OpenSans"
                                hint_text : "Year"
                                size_hint_x : None
                                width : 260
                                font_size : 20
                                pos_hint : {"center_x":.5}
                            MDTextField : 
                                font_name : "OpenSans"
                                hint_text : "Student ID"
                                size_hint_x : None
                                width : 260
                                font_size : 20
                                pos_hint : {"center_x":.5}
                            
                            
                
            MDScreen:
                name: "scr 3"
            
                MDLabel:
                    halign: "center"
                    md_bg_color :  [232/255, 232/255, 232/255,1]
                    size_hint : 1,0.9
                    MDScreen :
                        
                        MDCard :
                            size_hint : None,None
                            size : 800,400
                            
                            elevation : 15
                            spacing : 5
                            md_bg_color :  [250/255, 250/255, 250/255,1]
                            orientation : "vertical"
                            padding_y : 15
                            MDBoxLayout:
                                size_hint_y: None
                                height: "150dp"
                                width: "800dp"
                                orientation: 'vertical'
                            
                                FitImage:
                                    size_hint_y: 3
                                    source: 'image/1.jpg'
                            
                            MDLabel : 
                                text : 'STUDENT GRADE INFORMATION'
                                font_name : "OpenSans"
                                font_style : 'Button'
                                font_size : 35
                                halign : "center"
                                size_hint_y : None
                                height : self.texture_size[1]
                                padding_y : 5
                            MDTextField : 
                                font_name : "OpenSans"
                                hint_text : "Student Name"
                                size_hint_x : None
                                width : 260
                                font_size : 20
                                pos_hint : {"center_x":.5}
                            MDTextField : 
                                font_name : "OpenSans"
                                hint_text : "Student ID"
                                size_hint_x : None
                                width : 260
                                font_size : 20
                                pos_hint : {"center_x":.5}
                            MDTextField : 
                                font_name : "OpenSans"
                                hint_text : "Department"
                                size_hint_x : None
                                width : 260
                                font_size : 20
                                pos_hint : {"center_x":.5}
                            MDTextField : 
                                font_name : "OpenSans"
                                hint_text : "TOTAL CGPA"
                                size_hint_x : None
                                width : 260
                                font_size : 20
                                pos_hint : {"center_x":.5}
                            
                    
            MDScreen:
                name: "scr 4"
            
                MDLabel:
                    halign: "center"
                    md_bg_color :  [232/255, 232/255, 232/255,1]
                    size_hint : 1,0.9
                    MDScreen :
                        
                        MDCard :
                            size_hint : None,None
                            size : 800,200
                            
                            elevation : 15
                            spacing : 5
                            md_bg_color :  [250/255, 250/255, 250/255,1]
                            orientation : "vertical"
                            padding_y :5
                            MDBoxLayout:
                                size_hint_y: None
                                height: "150dp"
                                orientation: 'vertical'
                            
                                FitImage:
                                    size_hint_y: 0.5
                                    source: 'image/service1.jpg'
                            
                            MDLabel : 
                                text : 'STUDENT RECORD LIST'
                                font_name : "OpenSans"
                                font_style : 'Button'
                                font_size : 35
                                halign : "center"
                                size_hint_y : None
                                height : self.texture_size[1]
                                padding_y : 5
                            MDLabel : 
                                text : 'Record 1'
                                font_name : "OpenSans"
                                icon_left : "start"
                                size_hint_x : None
                                width : 260
                                font_size : 20
                                pos_hint : {"center_x":.5}
                                size_hint_y : None
                                height : self.texture_size[1]
                                padding_y : 5
                            MDLabel : 
                                text : 'Record 2'
                                font_name : "OpenSans"
                                icon_left : "start"
                                size_hint_x : None
                                width : 260
                                font_size : 20
                                pos_hint : {"center_x":.5}
                                size_hint_y : None
                                height : self.texture_size[1]
                                padding_y : 5
                            MDLabel : 
                                text : 'Record 3'
                                font_name : "OpenSans"
                                icon_left : "start"
                                size_hint_x : None
                                width : 260
                                font_size : 20
                                pos_hint : {"center_x":.5}
                                size_hint_y : None
                                height : self.texture_size[1]
                                padding_y : 5
                            MDLabel : 
                                text : 'Record 4'
                                font_name : "OpenSans"
                                icon_left : "start"
                                size_hint_x : None
                                width : 260
                                font_size : 20
                                pos_hint : {"center_x":.5}
                                size_hint_y : None
                                height : self.texture_size[1]
                                padding_y : 5
                            MDLabel : 
                                text : 'Record 5'
                                font_name : "OpenSans"
                                icon_left : "start"
                                size_hint_x : None
                                width : 260
                                font_size : 20
                                pos_hint : {"center_x":.5}
                                size_hint_y : None
                                height : self.texture_size[1]
                                padding_y : 5
                            
            MDScreen:
                name: "scr 7"
            
                MDLabel:
                    halign: "center"
                    md_bg_color :  [200/255, 230/255, 197/255,1]
                    size_hint : 1,0.9
                    MDScreen :
                        MDCard :
                            size_hint : None,None
                            size : 320,400
                            
                            elevation : 15
                            spacing : 30
                            md_bg_color :  [213/255, 222/255, 191/255,1]
                            orientation : "vertical"
                            padding_y : 15
                            #Adding items to the card
                            MDBoxLayout:
                                size_hint_y: None
                                height: "120dp"
                                orientation: 'vertical'
                            
                                FitImage:
                                    size_hint_y: 3
                                    source: 'image/logo.jpg'
                            
                            MDLabel : 
                                text : 'Sign In'
                                font_name : "OpenSans"
                                font_style : 'Button'
                                font_size : 35
                                halign : "center"
                                size_hint_y : None
                                height : self.texture_size[1]
                                padding_y : 5
                                
                            MDTextField : 
                                font_name : "OpenSans"
                                hint_text : "User Name"
                                size_hint_x : None
                                width : 260
                                font_size : 20
                                pos_hint : {"center_x":.5}
                            MDTextField :
                                hint_text : "Password"
                                size_hint_x : None
                                width : 260
                                font_size : 20
                                pos_hint : {"center_x":.5}
                            Button : 
                                text : 'LOGIN'
                                bold : True
                                pos_hint : {"center_x":.5}
                                font_size : 15
                                size: 260,50
                                size_hint: None,None
                                pos : "288dp","180dp"
                                md_bg_color:[84/255, 204/255, 75/255,1]
            
            MDScreen:
                name: "scr 8"
            
                MDLabel:
                    halign: "center"
                    md_bg_color :  [200/255, 230/255, 197/255,1]
                    size_hint : 1,0.9
                    MDScreen :
                        MDCard :
                            size_hint : None,None
                            size : 320,540
                            halign : "center"
                            elevation : 15
                            spacing : 20
                            md_bg_color :  [213/255, 222/255, 191/255,1]
                            orientation : "vertical"
                            padding_y : 15
                            
                            
                            MDLabel : 
                                text : 'Registration'
                                font_name : "OpenSans"
                                font_style : 'Button'
                                font_size : 30
                                halign : "center"
                                size_hint_y : None
                                height : self.texture_size[1]
                                padding_y : 5
                            MDTextField : 
                                font_name : "OpenSans"
                                hint_text : "Name"
                                size_hint_x : None
                                width : 260
                                font_size : 20
                                pos_hint : {"center_x":.5} 
                            MDTextField : 
                                font_name : "OpenSans"
                                hint_text : "Student ID"
                                size_hint_x : None
                                width : 260
                                font_size : 20
                                pos_hint : {"center_x":.5}
                            MDTextField : 
                                font_name : "OpenSans"
                                hint_text : "Mobile No."
                                size_hint_x : None
                                width : 260
                                font_size : 20
                                pos_hint : {"center_x":.5}
                            MDTextField :
                                hint_text : "Password"
                                size_hint_x : None
                                width : 260
                                font_size : 20
                                pos_hint : {"center_x":.5}
                            Button : 
                                text : 'Registration'
                                bold : True
                                pos_hint : {"center_x":.5}
                                font_size : 15
                                size: 260,50
                                size_hint: None,None
                                pos : "288dp","180dp"
                                md_bg_color:[84/255, 204/255, 75/255,1]
                    
        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class StudentManagementSystem(MDApp):
    def build(self):
        return Builder.load_string(KV)


StudentManagementSystem().run()