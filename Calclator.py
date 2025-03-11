from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.size = (500, 700)
Window.minimum_width = 350
Window.minimum_height = 400
Builder.load_file("calculator.kv")

class Calc(Widget):
    
    def clear(self):
        self.ids.calc_input.text = "0"
        
    def btn_add(self, button_text):
        prior = self.ids.calc_input.text
        if prior == "0":
            self.ids.calc_input.text = button_text
        else:
            self.ids.calc_input.text = prior + button_text

    def calculate(self):
        try:
            result = self.ids.calc_input.text 
            self.ids.calc_input.text = str(eval(result))
        except Exception as e:
            self.ids.calc_input.text = "Error"
            print(f"Calculation error: {e}")
            
class Calculator(App):
    def build(self):
        return Calc()

if __name__ == '__main__':
    Calculator().run()
