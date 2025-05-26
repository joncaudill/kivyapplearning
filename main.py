from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.properties import StringProperty
from kivy.properties import NumericProperty


class GameScreen(Widget):
    label_text = StringProperty("")
    numeric = NumericProperty(0)

    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.label_text = "Here is some text"
        self.numeric = 42

class LanguageLearnerApp(App):
    def build(self):
        game_screen = GameScreen()
        return game_screen
    
if __name__ == '__main__':
    LanguageLearnerApp().run()