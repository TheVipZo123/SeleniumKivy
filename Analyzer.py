import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget



# You can create your kv code in the Python file
Builder.load_string("""
<ScreenOne>:
    FloatLayout:
        background_color: 'Altus.png'
        Button:
            text: "Iniciar o programa"
            size: 150, 50
            size_hint: .4, .1
            pos_hint: {"center_x": 0.5,"center_y": 0.5}
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_two'

<ScreenTwo>:
    name1: name1
    FloatLayout:
        Label:
            text: "Por favor, insira o caminho da pasta do documento aqui:"
            font_size_hint: .9, .9
            size_hint: .9, .9
            pos_hint: {"center_x": 0.5,"center_y": 0.6}  
        TextInput:
            id: name1  #
            multiline: False
            font_size_hint: .9, .1
            size_hint: .6, .05
            pos_hint: {"center_x": 0.5,"center_y": 0.55} 

        Button:
            text: "OK"
            font_size_hint: .4, .1
            size_hint: .1, .05
            pos_hint: {"center_x": 0.87,"center_y": 0.55} 
            on_press: root.btn() #        

        Button:
            text: "Voltar"
            font_size_hint: .4, .1
            size_hint: .3, .1
            pos_hint: {"x": 0.0,"y": 0.0}
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'screen_one'
""")


# Create a class for all screens in which you can include
# helpful methods specific to that screen

class ScreenOne(Screen):
    pass


class ScreenTwo(Screen):
    class ScreenTwo(Widget):
        name1 = ObjectProperty(None)

    def btn(self):
        global NomeDoDiretorio
        NomeDoDiretorio = self.name1.text
        print("Name:", NomeDoDiretorio)



# The ScreenManager controls moving between screens
screen_manager = ScreenManager()

# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))


class KivyTut2App(App):

    def build(self):
        return screen_manager


sample_app = KivyTut2App()
sample_app.run()