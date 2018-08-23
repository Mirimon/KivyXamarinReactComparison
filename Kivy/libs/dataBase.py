import io
import datetime
import json


class DataBase(object):
    dataProjects = {}

    def getDate(self):
        now = datetime.datetime.now()
        return '%s.%s.%s' % (now.month, now.month, now.year)

    def updateDataProjects(self):
        self.saveDataProjects()
        self.setDataProjects()

    def saveDataProjects(self):
        with io.open(self.pathToBase, 'w', encoding='utf-8') as outfile:
            try:
                outfile.write(json.dumps(self.dataProjects, ensure_ascii=False))
            except TypeError:
                outfile.write(u'')

    def setDataProjects(self):
        try:
            self.dataProjects = json.load(open(self.pathToBase))
        except ValueError:
            self.dataProjects = {}

    def addNoteInBase(self, projectName, textNote, avatar):
        dataNote = {
            'nameDate': '%s\n%s' % (self.nameAuthor, self.getDate()),
            'textNote': textNote, 'nameAuthor': self.nameAuthor,
            'pathToAvatar': avatar}
        self.dataProjects[projectName][1].append(dataNote)
        self.updateDataProjects()

    def addProjectInBase(self, projectName):
        self.dataProjects[projectName] = [{"projectName": projectName}, []]
        self.updateDataProjects()

    def deleteProjectFromBase(self, projectName):
        del self.dataProjects[projectName]
        self.updateDataProjects()

    def deleteNoteFromBase(self, nameProject, textNote):
        for data in self.dataProjects[nameProject][1]:
            if data['textNote'] == textNote:
                self.dataProjects[nameProject][1].remove(data)
                break
        self.updateDataProjects()

    def addEditNoteInBase(self, nameProject, textNote, oldTextNote):
        for dataNotes in self.dataProjects[nameProject][1]:
            if dataNotes['textNote'] == oldTextNote:
                dataNotes['textNote'] = textNote
                break
        self.updateDataProjects()
