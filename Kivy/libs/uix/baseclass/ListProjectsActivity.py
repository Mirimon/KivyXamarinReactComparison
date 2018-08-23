# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import Screen as Activity

from libs.applibs.inputdialog import InputDialog
from . ProjectItem import ProjectItem


class ListProjectsActivity(Activity):
    objApp = App.get_running_app()

    def setListProjects(self, objApp):
        for nameProject in objApp.dataProjects.keys():
            self.ids.layoutContainer.add_widget(ProjectItem(projectName=nameProject))

    def createNewProject(self, projectName):
        if projectName and not projectName.isspace():
            self.ids.layoutContainer.add_widget(ProjectItem(projectName=projectName))
            self.objApp.addProjectInBase(projectName)

    def deleteProject(self, instance):
        for projectName in self.objApp.dataProjects:
            if instance.projectName == projectName:
                self.objApp.deleteProjectFromBase(projectName)
                break

    def showDialogCreateProject(self, *args):
        InputDialog(
            title='Новый проект', hintText='Имя проекта',
            textButtonCancel='Отмена', textTuttonOk='Да',
            eventsCallback=self.createNewProject).show()
