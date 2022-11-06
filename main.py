import kivy
from time import *
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

kivy.require('2.1.0')  # replace with your current kivy version !




class Okno(BoxLayout):
    def __init__(self, **args):
        super(Okno, self).__init__(**args)
        def my_callback(dt):
            czas1 = "(gmt +1) \n" + ctime(time())
            czas2 = "(gmt +2) \n" + ctime(time() + 3600)
            czas3 = "(gmt +3) \n" + ctime(time() + 7200)
            self.clear_widgets()
            label = Label(text=czas1)
            self.add_widget(label)
            label2 = Label(text=czas2)
            self.add_widget(label2)
            label3 = Label(text=czas3)
            self.add_widget(label3)
        Clock.schedule_interval(my_callback, 1)


class MyApp(App):
    def build(self):
        self.root = root = Okno()
        return root

if __name__ == '__main__':
    MyApp().run()
