from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image

class GameScreen(Widget):
    pass

class LanguageLearnerApp(App):
    def build(self):
        game_screen = GameScreen()
        return game_screen
    
if __name__ == '__main__':
    LanguageLearnerApp().run()