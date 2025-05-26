from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)  # Set background color to white
Window.size = (400, 600)  # Set window size

class ImageBox(Widget):
    pass

class ProgressBar(Widget):
    pass

class GameScreen(Widget):
    pass

class LanguageLearnerApp(App):
    def build(self):
        game_screen = GameScreen()
        return game_screen
    
if __name__ == '__main__':
    LanguageLearnerApp().run()