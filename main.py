import os
import shutil

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation = "vertical")

        # input section
        self.folderinput = TextInput(background_color="black", foreground_color="white", multiline=False, height=1)
        main_layout.add_widget(self.folderinput)

        # button section
        button = Button(text = "Press Enter to Manage File", font_size=30, background_color="grey", pos_hint = {"center_x":0.5, "center_y":0.5})
        button.bind(on_press = self.on_button_press)
        main_layout.add_widget(button)

        return main_layout

    def on_button_press(self, instance):
        path = self.folderinput.text
        if path:
            files = os.listdir(path)
            for file in files:
                filename, extensionTemp = os.path.splitext(file)
                extension = extensionTemp[1:]
                folderpath = path + "\\" + extension
                if os.path.exists(folderpath):
                    shutil.move(path + "\\" + file, path + "\\" + extension + "\\" + file)
                else:
                    os.makedirs(folderpath)
                    shutil.move(path + "\\" + file, path + "\\" + extension + "\\" + file)
            return
        else:
            return

if __name__ == "__main__":
    app=MainApp()
    app.run()