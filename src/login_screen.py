from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from peewee import DoesNotExist
from user_model import User


class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(Label(text='Username:'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Password:'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        self.login_button = Button(text='Login')
        self.login_button.bind(on_press=self.verify_credentials)
        self.add_widget(self.login_button)

        self.register_button = Button(text='Register')
        self.register_button.bind(on_press=self.register_user)
        self.add_widget(self.register_button)

    def verify_credentials(self, instance):
        try:
            user = User.get(User.username == self.username.text)
            if user.password == self.password.text:
                print("Login successful")
                # TODO: Navigate to the inbox screen
            else:
                print("Incorrect password")
        except DoesNotExist:
            print("User does not exist")

    def register_user(self, instance):
        try:
            User.get(User.username == self.username.text)
            print("Username already exists")
        except DoesNotExist:
            new_user = User(username=self.username.text, password=self.password.text)
            new_user.save()
            print("User registered")
            # TODO: Navigate to the inbox screen
