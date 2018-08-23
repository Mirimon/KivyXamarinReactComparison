from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

from libs.applibs.animdropdown import MenuButton
from libs.applibs.swipetodelete import SwipeBehavior
from . ContextMenu import ContextMenu


class NoteActivity(SwipeBehavior, BoxLayout):
    nameDate = StringProperty()
    textNote = StringProperty()
    pathToAvatar = StringProperty()

    def __init__(self, **kwargs):
        super(NoteActivity, self).__init__(**kwargs)
        self.objApp = App.get_running_app()
        menuButton = MenuButton(
            dropdown_cls=ContextMenu, icon='dots-vertical',_on_dropdown_fnc=self.setCurrentPost)
        self.ids.titleBox.add_widget(menuButton)

    def setCurrentPost(self, *args):
        self.objApp.listNotesActivity.checkCurentPost = self

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.move_to = self.x, self.y
            return super(NoteActivity, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.reduce_opacity()
            return super(NoteActivity, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.check_for_left()
            self.check_for_right()
            return super(NoteActivity, self).on_touch_up(touch)
