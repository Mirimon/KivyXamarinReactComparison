# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.clock import Clock

from libs.applibs.animdropdown import AnimMenuDropDown


class ContextMenu(AnimMenuDropDown):
    def tapOnItem(self, textItem):
        objApp = App.get_running_app()
        if textItem == 'Удалить':
            objApp.listNotesActivity.deletePost()
        else:
            objApp.activityManager.current = 'add new note activity'
            Clock.schedule_once(objApp.addNewNoteActivity.editNote, .5)
