from kivy.app import App
from kivy.uix.button import Button

class LanguageLearnerApp(App):
    def build(self):
        # kivy's positioning system uses a coordinate system where (0, 0) is the bottom-left corner
        return Button(
            text='Hello, Language Learner!',
            pos=(50, 50),
            size_hint=(0.8, 0.8),  # Disable size hint to use absolute size
            #size=(500,500)
            )
    
if __name__ == '__main__':
    LanguageLearnerApp().run()