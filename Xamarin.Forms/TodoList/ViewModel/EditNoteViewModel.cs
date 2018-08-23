using System;
using TodoList.Model;

namespace TodoList.ViewModel {
    public class EditNoteViewModel : NotificationObject {
        public string ProjectName { get; set; }
        public Note Note { get; set; }

        string text = "";
        public string Text {
            get { return text; }
            set {
                if(text != value) {
                    text = value;
                    RaisePropertyChanged();
                }
            }
        }

        public EditNoteViewModel(Note note, string projectName) {
            Note = note;
            ProjectName = projectName;
            Text = Note.Text;
        }

        public void SaveText() {
            Note.Text = Text;
            Note.EditTime = DateTime.Now;
        }
    }
}
