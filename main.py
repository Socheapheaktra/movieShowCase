from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp

from kivy.properties import ObjectProperty
from kivy.core.window import Window

from libs.uix.baseclass.main_screen import MainScreen

width = 288.96 * 2
height = 618.24 * 2
Window.size = (width, height)
Window.left = 0
Window.top = 0

class MainWindow(MDBoxLayout):
    main_screen = ObjectProperty()
    detail_screen = ObjectProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_screen = MainScreen()

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Dark"
        return MainWindow()

    def on_start(self):
        self.root.ids.main_scrn.add_widget(self.root.main_screen)

if __name__ == '__main__':
    MainApp().run()
