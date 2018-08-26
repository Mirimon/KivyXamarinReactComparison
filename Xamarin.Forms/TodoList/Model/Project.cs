using System;
using System.Collections.ObjectModel;
using Xamarin.Forms;

namespace TodoList.Model {
    public class Project : NotificationObject {

        string name = "";
        public string Name {
            get { return name; }
            set {
                if (name != value) {
                    name = value;
                    RaisePropertyChanged();
                }
            }
        }

        public ObservableCollection<Note> Notes { get; set; }

        public Project() {
            Notes = new ObservableCollection<Note>();
        }

        public static ObservableCollection<Project> GetTestProjects() {
            ObservableCollection<Project> result = new ObservableCollection<Project>();
            Project project = new Project() { Name = "Тестовый проект для Хабра" };
            project.Notes.Add(new Note() { UserName = "Первый пользователь", EditTime = DateTime.Now, Text = "Длинный текст, который должен занимать несколько строк. Съешь ещё этих мягких французских булок, да выпей же чаю.", UserIconPath = "TodoList.Images.User1.png" });
            project.Notes.Add(new Note() { UserName = "Второй пользователь", EditTime = DateTime.Now, Text = "Текст на одну строку", UserIconPath = "TodoList.Images.User2.png" });
            project.Notes.Add(new Note() { UserName = "Первый пользователь", EditTime = DateTime.Now, Text = "Текст на две строки, поэтому этот текст должен быть вот такой длины", UserIconPath = "TodoList.Images.User1.png" });
            result.Add(project);
            result.Add(new Project() { Name = "Пустой проект" });

            return result;
        }
    }
}
