from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

from libs.applibs.swipetodelete import SwipeBehavior


class ProjectItem(SwipeBehavior, BoxLayout):
    projectName = StringProperty()

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.move_to = self.x, self.y
            return super(ProjectItem, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.reduce_opacity()
            return super(ProjectItem, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.check_for_left()
            self.check_for_right()
            return super(ProjectItem, self).on_touch_up(touch)
