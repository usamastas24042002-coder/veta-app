from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import datetime
import random

class VETASimple:
    def __init__(self):
        self.commands = {
            'привет': 'Привет, любимый! 💕',
            'как дела': 'Всё прекрасно! 🥰', 
            'обними': 'Обнимаю крепко! 💝',
            'любишь': 'Люблю больше жизни! 💖',
            'время': 'Сейчас время 🕒'
        }
    
    def process_command(self, command):
        for cmd, response in self.commands.items():
            if cmd in command.lower():
                if cmd == 'время':
                    return f'Сейчас {datetime.datetime.now().strftime("%H:%M")} 🕒'
                return response
        return 'Не поняла... 💖'

class VETAApp(App):
    def build(self):
        self.veta = VETASimple()
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.input_field = TextInput(hint_text='Введите команду...', size_hint=(1, 0.1))
        self.input_field.bind(on_text_validate=self.process_input)
        
        send_btn = Button(text='Отправить', size_hint=(1, 0.1))
        send_btn.bind(on_press=self.process_input)
        
        scroll = ScrollView()
        self.output_label = Label(text='VETA готова! 💖', size_hint_y=None, markup=True)
        self.output_label.bind(texture_size=self.output_label.setter('size'))
        scroll.add_widget(self.output_label)
        
        main_layout.add_widget(self.input_field)
        main_layout.add_widget(send_btn)
        main_layout.add_widget(scroll)
        
        return main_layout
    
    def process_input(self, instance):
        command = self.input_field.text.strip()
        if command:
            response = self.veta.process_command(command)
            new_text = f'[color=333333]Вы: {command}[/color]\n[color=ff69b4]VETA: {response}[/color]\n' + self.output_label.text
            self.output_label.text = new_text
            self.input_field.text = ''

if __name__ == '__main__':
    VETAApp().run()
