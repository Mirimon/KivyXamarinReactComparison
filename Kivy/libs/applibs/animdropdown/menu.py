# -*- coding: utf-8 -*-

# Copyright © 2010-2018 HeaTTheatR
#
# For suggestions and questions:
# <kivydevelopment@gmail.com>

from kivy.uix.dropdown import DropDown
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color, Rectangle
from kivy.properties import ObjectProperty, NumericProperty, ListProperty, \
    StringProperty
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.metrics import dp

from kivymd.ripplebehavior import RectangularRippleBehavior
from libs.applibs.kivymd.label import MDLabel


Builder.load_string('''
<MenuItem>:
    size_hint_y: None
    height: dp(40)
    text_size: self.size
    padding_x: dp(10)
    valign: 'middle'
    on_release: self.menu.dismiss(immediate=False)

    Widget:
        size_hint_y: None
        height: dp(2)

<AnimMenuDropDown>:
    scroll_distance: dp(2)
    scroll_timeout: 25
    auto_width: False
    width: root.width_menu
    opacity: 1. - root.anim_progress
    _app: app

    canvas:
        Color:
            rgba: 0.3, 0.3, 0.3, 1
        Line:
            rectangle: self.x + dp(0.55), self.y + dp(0.55), self.width - dp(1.1), self.height - dp(1.1)
            width: dp(1.1)

    canvas.before:
        PushMatrix:
        Translate:
            x: root.anim_progress * root.shift
            y: root.anim_progress * 0.5 * root.shift

    canvas.after:
        PopMatrix:
''')


class AnimMenuDropDown(DropDown):
    shift = NumericProperty(dp(30))
    anim_progress = NumericProperty(1)
    parent_obj = ObjectProperty()
    width_menu = NumericProperty(100)
    text_color = StringProperty('#ffffff')
    background_color = ListProperty()
    _app = ObjectProperty()

    def open(self, *args, **kwargs):
        with self.canvas.before:
            def update_canvas_pos(instance, value):
                canvas_drop_down.pos = instance.pos

            def update_canvas_size(instance, value):
                canvas_drop_down.size = instance.size

            if not len(self.background_color):
                Color(rgba=self._app.theme_cls.primary_color)
            else:
                Color(rgba=self.background_color)
            canvas_drop_down = Rectangle(pos=self.pos, size=self.size)
            # FIXME: вынести из метода постоянный бинд.
            self.bind(size=update_canvas_size, pos=update_canvas_pos)

        super(AnimMenuDropDown, self).open(*args, **kwargs)
        self.animate_open()
        self.set_text_color()

    def set_text_color(self):
        for menu_button in self.children[0].children:
            menu_button.color = get_color_from_hex(self.text_color)

    def dismiss(self, *args, **kwargs):
        if kwargs.get('immediate', False):
           kwargs.pop('immediate')
           super(AnimMenuDropDown, self).dismiss(*args, **kwargs)
        else:
            self.animate_dismiss()

    def animate_open(self):
        Animation.cancel_all(self)
        self.anim_progress = 1
        Animation(anim_progress=0, d=0.4, t='out_cubic').start(self)

    def animate_dismiss(self):
        Animation.cancel_all(self)
        anim = Animation(anim_progress=1, d=0.2, t='out_cubic')
        anim.bind(on_complete=self.immediate_dismiss)
        anim.start(self)

    def immediate_dismiss(self, *args, **kwargs):
        self.dismiss(immediate=True)


class DropDownButton(RectangularRippleBehavior, ButtonBehavior, MDLabel):
    padding = NumericProperty(0)
    radius = NumericProperty(0)


class MenuItem(DropDownButton):
    menu = ObjectProperty()
