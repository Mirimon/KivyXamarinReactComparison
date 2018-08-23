# -*- coding: utf-8 -*-

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.lang import Builder


Builder.load_string('''
#:import MDTextField kivymd.textfields.MDTextField

<InputDialog>:
    size_hint: 0, 0
    background_color: 0, 0, 0, .2
    background: 'data/images/alpha.png'
    MDCard:
        id: cardContent

<ContentInputDialog>:
    orientation: 'vertical'
    padding: dp(15)
    spacing: dp(10)
    MDLabel:
        font_style: 'Title'
        theme_text_color: 'Primary'
        text: root.title
        halign: 'left'
    MDTextField:
        id: textField
        size_hint: 1, None
        height: dp(48)
        hint_text: root.hintText
    Widget:
    Widget:
    MDFlatButton:
        text: root.textButtonOk
        pos_hint: {'center_x': .5}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.primary_color
        on_release: root.eventsCallback(textField.text)

''')


class InputDialog(ModalView):
    title = StringProperty('Title')
    hintText = StringProperty('Write something')
    textButtonOk = StringProperty('OK')
    eventsCallback = ObjectProperty()

    def __init__(self, **kwargs):
        super(InputDialog, self).__init__(**kwargs)

    def show(self):
        self.on_dismiss = self.FadenputDialogActivity
        self.open()
        anim = Animation(size_hint=(.8, .6), d=.5, t='in_out_cubic')
        anim.bind(on_complete=self.setContentInputDialogActivity)
        anim.start(self)

    def FadenputDialogActivity(self):
        self.ids.cardContent.clear_widgets()

    def setContentInputDialogActivity(self, *args):
        def setFieldFocus(interval):
            contentInputDialog.ids.textField.focus = True

        def _eventsCallback(resultPress):
            self.dismiss()
            if resultPress:
                self.eventsCallback(
                    contentInputDialog.ids.textField.text)

        contentInputDialog = ContentInputDialog(
            title=self.title, hintText=self.hintText,
            textButtonOk=self.textButtonOk,
            eventsCallback=_eventsCallback)
        self.ids.cardContent.add_widget(contentInputDialog)
        Clock.schedule_once(setFieldFocus, .5)


class ContentInputDialog(BoxLayout):
    textButtonOk = StringProperty()
    hintText = StringProperty()
    title = StringProperty()
    eventsCallback = ObjectProperty()
