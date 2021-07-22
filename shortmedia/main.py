import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
import mysql

Window.size = (450, 750)

Builder.load_string("""
<LoginScreen>:
    BoxLayout:
        orientation: 'vertical'
        spacing: 20
        Image:
            source: 'tism2.png'
            size_hint: None,None
            size: 200,70
            pos_hint: {'center_x': 0.5,'center': 0.8}
        MDCard:
            elevation: 25
            radius: 30
            orientation: 'vertical'
            size_hint: None,None
            size: 400,400
            padding: 50
            spacing: 20
            pos_hint: {'center_x':0.5 , 'center_y':0.5 }
            MDTextField:
                hint_text: "Usename"
                multiline: False
                font_size: 25
                icon_right: 'account'
                font_size: 22
                padding: 5
                mode: "rectangle"
            MDTextField:
                hint_text: "password"
                multiline: False
                font_size: 25
                icon_right: 'eye-off'
                font_size: 22
                padding: 5
                mode: "rectangle"
                password: True
            MDRaisedButton:
                text: f"{' '*int(dp(25))}Login{' '*int(dp(25))}"
                pos_hint: {"center_x":0.5}
            MDRectangleFlatButton:
                text: f"{' '*int(dp(30))}create account{' '*int(dp(30))}"
                text_color: 0, 160/255, 0, 1
                line_color: 0,160/255, 0, 1
                pos_hint: {'center_x': 0.5 }
                on_press: root.manager.current = 'signin'
        MDCard:
            elevation: 25
            radius: 20
            orientation: 'vertical'
            size_hint: None,None
            size: 400,100
            size_hint_y: None
            pos_hint: {'center_x':0.5 , 'center_y':0.5 }
            MDLabel:
                text: "Created by Venkat"
                halign: 'center'
        BoxLayout:
            size_hint_y: None
            height: 55     
          
<SigninScreen>:
    BoxLayout:
        orientation: 'vertical'
        spacing: 20
        Image:
            source: 'tism2.png'
            size_hint: None,None
            size: 200,70
            pos_hint: {'center_x': 0.5,'center': 0.8}
        MDCard:
            elevation: 25
            radius: 30
            orientation: 'vertical'
            size_hint: None,None
            size: 400,400
            padding: 50
            spacing: 20
            pos_hint: {'center_x':0.5 , 'center_y':0.5 }
            MDTextField:
                hint_text: "Usename"
                multiline: False
                font_size: 22
                padding: 5
                mode: "rectangle"
            
            MDTextField:
                hint_text: "password"
                multiline: False
                font_size: 22
                icon_right: 'eye-off'
                password: True
                padding: 5
                mode: "rectangle"
            MDRaisedButton:
                text: f"{' '*int(dp(25))}Signin{' '*int(dp(25))}"
                pos_hint: {"center_x":0.5}
            MDRectangleFlatButton:
                text: f"{' '*int(dp(30))}create account{' '*int(dp(30))}"
                text_color: 0, 160/255, 0, 1
                line_color: 0,160/255, 0, 1
                pos_hint: {'center_x': 0.5 }
        BoxLayout:
            size_hint_y: None
            height: 55     
""")
# BoxLayout:
# 	    	orientation: 'vertical'
# 	        id: login 
		# Button:
	 #            text: 'next'
	 #            on_press: root.manager.current = 'settings'
class LoginScreen(Screen):
    pass

class SigninScreen(Screen):
    pass

class ShortApp(MDApp):
    def build(self):
        # 'White'. Must be one of: ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']

        # Create the screen manager
        # self.theme_cls.primary_palette = "White"
        # self.theme_cls.accent_palette = "Red"
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SigninScreen(name='signin'))

        return sm

if __name__ == '__main__':
    ShortApp().run()
               