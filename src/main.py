from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from stuffless_db_init import init_db


class Login(Screen):
    pass


class Inbox(Screen):
    pass


class StufflessApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Login(name='login'))
        sm.add_widget(Inbox(name='inbox'))
        return sm


if __name__ == '__main__':
    init_db()
    StufflessApp().run()