from kivy.app import App
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen as Activity
from kivy.metrics import dp

from libs.uix.baseclass.NoteActivity import NoteActivity


class AddNewNoteActivity(Activity):
    objApp = None
    edit = False
    oldTextNote = ''

    def animationButton(self):
        self.objApp = App.get_running_app()
        self.ids.toolBar.title = self.objApp.listNotesActivity.ids.toolBar.title
        Animation(size=(dp(56), dp(56)), d=.5, t='in_out_cubic').start(self.ids.floatingButton)

    def addNewNotes(self, textNote):
        if self.edit:
            nameProject = self.ids.toolBar.title
            self.objApp.addEditNoteInBase(nameProject, textNote, self.oldTextNote)
            self.objApp.activityManager.backActivity('list notes activity', self.ids.floatingButton)
            self.objApp.listNotesActivity.checkCurentPost.textNote = textNote
            self.edit = False
            return

        self.objApp.listNotesActivity.ids.layoutContainer.add_widget(
            NoteActivity(
                textNote=textNote, nameDate='%s\n%s' % (
                self.objApp.nameAuthor, self.objApp.getDate()),
                pathToAvatar='data/images/user-2.png'))
        self.objApp.addNoteInBase(self.ids.toolBar.title, textNote, 'data/images/user-2.png')

    def editNote(self, interval):
        self.edit = True
        self.ids.textInput.text = self.objApp.listNotesActivity.checkCurentPost.textNote
        self.oldTextNote = self.ids.textInput.text
