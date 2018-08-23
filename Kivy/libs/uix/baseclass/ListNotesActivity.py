# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import Screen as Activity
from kivy.properties import ObjectProperty

from . NoteActivity import NoteActivity


class ListNotesActivity(Activity):
    checkCurentPost = ObjectProperty()
    objApp = App.get_running_app()

    def clearList(self):
        if self.objApp.activityManager.current == 'list project activity':
            self.ids.layoutContainer.clear_widgets()

    def addNewNote(self, objApp):
        objApp.activityManager.current = 'add new note activity'

    def setDefaultcheckCurentPost(self):
        self.checkCurentPost = lambda x: None

    def setNotesProject(self, nameProject):
        self.ids.toolBar.title = nameProject
        for dataProject in self.objApp.dataProjects[nameProject][1]:
            self.ids.layoutContainer.add_widget(NoteActivity(
                textNote=dataProject['textNote'],
                nameDate=dataProject['nameDate'],
                pathToAvatar=dataProject['pathToAvatar']))

    def deletePost(self, instance=None):
        # Удаление свайпом.
        if not self.checkCurentPost:
            checkCurentPost = instance
        else:
            checkCurentPost = self.checkCurentPost
            self.ids.layoutContainer.remove_widget(self.checkCurentPost)

        nameProject = self.ids.toolBar.title
        self.objApp.deleteNoteFromBase(nameProject, checkCurentPost.textNote)

    def checkScroll(self):
        if self.checkCurentPost and type(self.checkCurentPost) is not NoteActivity:
            self.checkCurentPost(self)
