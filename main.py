import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_file("design.kv")

class MyLayout(Widget):
    def press(self):
        #create variable for our widgets on kv file
        #ids means we are going to use ids of variables in kv file
        
        name = self.ids.name_input.text

        #update the label
        self.ids.name_label.text = f"Hello {name}"

        #clear input box
        self.ids.name_input.text = ""

class MyApp(App):
    def build(self):
        Window.clearcolor= (1,0,0,1)
        return MyLayout()
if __name__ == "__main__":
    MyApp().run()
