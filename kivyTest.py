from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        return Button(text="KNOPKA",
                      font_size=30,
                      on_press=self.btn_press,
                      background_color=[.32, .85, .94, 1],
                      background_normal='')

    def btn_press(self, instance):
        print("Knopka nazhata!!!")
        instance.text = "Hello World"


if __name__ == "__main__":
    MyApp().run()
