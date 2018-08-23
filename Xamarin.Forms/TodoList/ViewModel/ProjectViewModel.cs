using System;
using TodoList.Model;

namespace TodoList.ViewModel {
    public class ProjectViewModel {
        public Project Project { get; set; }

        public ProjectViewModel(Project project) {
            Project = project;
        }

        public void AddNote(Note note) {
            Project.Notes.Add(note);
        }

        public void DeleteNote(Note note) {
            Project.Notes.Remove(note);
        }
    }
}
