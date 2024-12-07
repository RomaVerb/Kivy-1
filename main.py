from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label

Window.size = (450, 800)
Window.title = "Calculator"


class MyApp(App):
    def build(self):
        self.number = "0"
        self.text_output = Label(text="0", size_hint=(1, 0.3), font_size=55, halign="right")
        self.last_char = None
        grid = GridLayout(cols=4)
        btn7 = Button(text="7", font_size=45, background_color=(1, 1, 1, 0.6), on_press=self.add_num)
        grid.add_widget(btn7)
        btn8 = Button(text="8", font_size=45, background_color=(1, 1, 1, 0.6), on_press=self.add_num)
        grid.add_widget(btn8)
        btn9 = Button(text="9", font_size=45, background_color=(1, 1, 1, 0.6), on_press=self.add_num)
        grid.add_widget(btn9)
        btn11 = Button(text="+", font_size=45, background_color=(1, 1, 1, 0.75), on_press=self.add_operation)
        grid.add_widget(btn11)

        btn4 = Button(text="4", font_size=45, background_color=(1, 1, 1, 0.6), on_press=self.add_num)
        grid.add_widget(btn4)
        btn5 = Button(text="5", font_size=45, background_color=(1, 1, 1, 0.6), on_press=self.add_num)
        grid.add_widget(btn5)
        btn6 = Button(text="6", font_size=45, background_color=(1, 1, 1, 0.6), on_press=self.add_num)
        grid.add_widget(btn6)
        btn12 = Button(text="-", font_size=45, background_color=(1, 1, 1, 0.75), on_press=self.add_operation)
        grid.add_widget(btn12)

        btn1 = Button(text="1", font_size=45, background_color=(1, 1, 1, 0.6), on_press=self.add_num)
        grid.add_widget(btn1)
        btn2 = Button(text="2", font_size=45, background_color=(1, 1, 1, 0.6), on_press=self.add_num)
        grid.add_widget(btn2)
        btn3 = Button(text="3", font_size=45, background_color=(1, 1, 1, 0.6), on_press=self.add_num)
        grid.add_widget(btn3)
        btn13 = Button(text="*", font_size=45, background_color=(1, 1, 1, 0.75), on_press=self.add_operation)
        grid.add_widget(btn13)

        btn10 = Button(text="0", font_size=45, background_color=(1, 1, 1, 0.6), on_press=self.add_num)
        grid.add_widget(btn10)
        btn14 = Button(text="=", font_size=45, background_color=(1, 1, 1, 0.9), on_press=self.result)
        grid.add_widget(btn14)
        btn15 = Button(text=".", font_size=45, background_color=(1, 1, 1, 0.75), on_press=self.add_operation)
        grid.add_widget(btn15)
        btn16 = Button(text="/", font_size=45, background_color=(1, 1, 1, 0.75), on_press=self.add_operation)
        grid.add_widget(btn16)

        box = BoxLayout(orientation="vertical")
        box.add_widget(self.text_output)
        box.add_widget(grid)

        return box

    def add_num(self, instance):
        if self.last_char == "=":
            self.number = "0"
        if self.number == "0":
            self.number = ""
        self.number += str(instance.text)
        self.text_output.text = self.number
        self.last_char = str(instance.text)

    def add_operation(self, instance):
        self.number += str(instance.text)
        self.text_output.text = self.number
        self.last_char = str(instance.text)

    def result(self, instance):
        try:
            self.number = str(round(eval(self.text_output.text), 9))
            self.text_output.text = self.number
        except SyntaxError:
            self.text_output.text = "Incorrect Option"
        self.last_char = str(instance.text)


if __name__ == "__main__":
    MyApp().run()
