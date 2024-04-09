


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout



class Mainpage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text='hi'))
class gorika(App):
    def build(self):
        return Mainpage()

gorika().run()
