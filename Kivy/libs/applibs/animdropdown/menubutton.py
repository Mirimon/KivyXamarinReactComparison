# -*- coding: utf-8 -*-

# Copyright © 2010-2018 HeaTTheatR
#
# For suggestions and questions:
# <kivydevelopment@gmail.com>

from kivy.properties import ObjectProperty, NumericProperty, StringProperty

from kivymd.button import BaseRoundButton, BaseFlatButton, BasePressedButton


class MenuButton(BaseRoundButton, BaseFlatButton, BasePressedButton):
    icon = StringProperty('android')
    dropdown_holder = ObjectProperty()
    dropdown_holder_width = NumericProperty()
    dropdown_cls = ObjectProperty()
    _on_dropdown_fnc = ObjectProperty(lambda x: None)

    def __init__(self, *args, **kwargs):
        super(MenuButton, self).__init__(*args, **kwargs)
        self.dropdown = self.dropdown_cls(parent_obj=self)

    def on_press(self, *args):
        if self.dropdown.parent is None:
            self.dropdown.open(self)
            self._on_dropdown_fnc(None)
