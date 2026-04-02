from kivy.app import App
from kivy.uix.button import Button

class SamratApp(App):
    def build(self):
        return Button(text='Victory is Yours, Shyam Ji!', background_color=(0,1,0,1))

if __name__ == '__main__':
    SamratApp().run()
  
