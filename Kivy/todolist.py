# -*- coding: utf-8 -*-

import os

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.factory import Factory

from libs.applibs.kivymd.theming import ThemeManager
from libs.dataBase import DataBase


class TodoList(App, DataBase):
    title = 'Todo List'
    icon = 'icon.png'
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'LightGreen'

    def __init__(self, **kvargs):
        super(TodoList, self).__init__(**kvargs)
        Window.bind(on_keyboard=self.eventsProgram)
        Window.softinput_mode = 'below_target'
        self.Window = Window
        self.pathToBase = '%s/data/dataProjects.json' % self.directory
        self.nameAuthor = u'Иванов Юрий'

    def build(self):
        self.setDataProjects()
        self.loadAllKvFiles(os.path.join(self.directory, 'libs', 'uix', 'kv'))
        self.rootScreen = Factory.RootScreen()  # стартовый экран программы
        # Инстансы Activity.
        self.activityManager = self.rootScreen.ids.activityManager
        self.listProjectsActivity = self.rootScreen.ids.listProjectsActivity
        self.listNotesActivity = self.rootScreen.ids.listNotesActivity
        self.addNewNoteActivity = self.rootScreen.ids.addNewNoteActivity

        return self.rootScreen

    def loadAllKvFiles(self, directory_kv_files):
        for kv_file in os.listdir(directory_kv_files):
            kv_file = os.path.join(directory_kv_files, kv_file)
            if os.path.isfile(kv_file):
                Builder.load_file(kv_file)

    def on_start(self):
        self.listProjectsActivity.setListProjects(self)

    def eventsProgram(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.activityManager.current == 'add new note activity':
                self.activityManager.backActivity(
                    'list notes activity', self.addNewNoteActivity.ids.floatingButton)
            if self.activityManager.current == 'list notes activity':
                self.activityManager.current = 'list project activity'
        return True
