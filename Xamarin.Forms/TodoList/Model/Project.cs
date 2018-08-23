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
            Project project = new Project() { Name = "Сравнение фреймворков" };
            project.Notes.Add(new Note() { UserName = "Александр Блинов", EditTime = DateTime.Now, Text = "Сравнить Xamarin.Forms, Kivy и React Native на примере TODO List приложения", UserIconPath = "TodoList.Images.User1.png" });
            project.Notes.Add(new Note() { UserName = "Юрий Иванов", EditTime = DateTime.Now, Text = "Написать по статье для каждого фреймворка", UserIconPath = "TodoList.Images.User2.png" });
            project.Notes.Add(new Note() { UserName = "Александр Блинов", EditTime = DateTime.Now, Text = "Возможно, сделать отдельную статью для выводов", UserIconPath = "TodoList.Images.User1.png" });
            result.Add(project);
            result.Add(new Project() { Name = "Тестовый проект" });

            return result;
        }
    }
}
