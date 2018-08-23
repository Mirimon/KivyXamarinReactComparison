# -*- coding: utf-8 -*-

from kivy.metrics import dp
from kivy.properties import ObjectProperty, BooleanProperty

from kivymd.toolbar import Toolbar
from kivymd.button import MDIconButton

from libs.applibs.animdropdown.menubutton import MenuButton


class ToolBar(Toolbar):
    callback = ObjectProperty(lambda x: None)
    '''Функция, которая будет вызвана при тапе на иконки тулбара.'''
    dropdown = BooleanProperty(True)

    def update_action_bar(self, action_bar, action_bar_items):
        action_bar.clear_widgets()
        new_width = 0

        for item in action_bar_items:
            new_width += dp(48)
            if self.dropdown:
                dropdown_cls = item[1]
                action_bar.add_widget(
                    MenuButton(
                        icon=item[0],
                        dropdown_cls=dropdown_cls,
                        opposite_colors=True,
                        text_color=self.specific_text_color,
                        theme_text_color='Custom',
                        on_release=lambda x: self.callback(x)
                    )
                )
            else:
                action_bar.add_widget(
                    MDIconButton(
                        icon=item[0],
                        on_release=item[1],
                        opposite_colors=True,
                        text_color=self.specific_text_color,
                        theme_text_color='Custom'
                    )
                )

        action_bar.width = new_width
