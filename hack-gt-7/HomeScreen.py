import kivy
import inventory

kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.image import Image as image
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button



Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '750')


class StartScreen(App):

    def build(self):
        a = AnchorLayout(anchor_x='center', anchor_y='center')
        img = image(source="inventory.png")
        a.add_widget(img)

        gl = GridLayout(cols=1, row_force_default=True, row_default_height=40, padding=100)
        self.textinput = TextInput(text="QR Code", multiline=False)
        gl.add_widget(self.textinput)

        submit = Button(text="Go", on_press=self.submit)
        gl.add_widget(submit)
        img = image(source="inventory.png")

        layout = FloatLayout(size=(500, 750))
        layout.add_widget(img)
        layout.add_widget(gl)

        a.add_widget(layout)

        return a

    def submit(self, obj):
        inventory.filename = self.textinput.text
        StartScreen.get_running_app().stop()
        inventory.ListScreen().run()




if __name__ == '__main__':
    StartScreen().run()

