from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup

Window.clearcolor = (1, 1, 1, 1)  # Set background color to white
Window.size = (400, 600)  # Set window size

class ImageBox(Widget):
    pass

class ProgressBar(Widget):
    pass

class GameScreen(Widget):
    def print_something(self, *args):
        print("Popup dismissed")
    
    def show_answer_popup(self):
        content = Image(source = 'images/diamante.png')

        answer_popup = Popup(title='Correct',
                             size_hint=(.5, .4),
                            content=content,
                            title_align='center',
                            title_color=(0, 0, 0, 1),
                            background='images/white.jpg'
                            )
        answer_popup.bind(on_dismiss=self.print_something)
        answer_popup.open()



class LanguageLearnerApp(App):
    def build(self):
        game_screen = GameScreen()
        return game_screen
    
if __name__ == '__main__':
    LanguageLearnerApp().run()