using System;
using System.Collections.ObjectModel;
using TodoList.Model;

namespace TodoList.ViewModel {
    public class MainViewModel {
        public ObservableCollection<Project> Projects { get; set; }

        public MainViewModel() {
            Projects = Project.GetTestProjects();
        }

        public void AddNewProject(string name) {
            Project project = new Project() { Name = name };
            Projects.Add(project);
        }

        public void DeleteProject(Project project) {
            Projects.Remove(project);
        }
    }
}
