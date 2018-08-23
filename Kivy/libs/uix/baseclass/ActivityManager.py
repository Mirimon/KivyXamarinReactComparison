from kivy.app import App
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager


class ActivityManager(ScreenManager):
    def backActivity(self, nameActivity, floatingButton=None):
        def backActivity(*args):
            self.current = nameActivity

        if floatingButton:
            anim = Animation(size=(0, 0), d=.5, t='in_out_cubic')
            anim.bind(on_complete=backActivity)
            anim.start(floatingButton)
        else:
            backActivity()
