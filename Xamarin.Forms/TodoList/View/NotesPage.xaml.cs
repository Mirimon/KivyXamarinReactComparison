using System;
using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Threading.Tasks;
using TodoList.Model;
using TodoList.ViewModel;
using Xamarin.Forms;

namespace TodoList.View {
    public partial class NotesPage : ContentPage {
        ProjectViewModel ViewModel { get { return BindingContext as ProjectViewModel; } }

        public NotesPage() {
            InitializeComponent();
        }

        void AddNew_Clicked(object sender, EventArgs e) {
            Note note = Note.CreateCurrentUserNote();
            ViewModel.AddNote(note);
            EditNote(note);
        }

        async Task DeleteItem_Clicked(object sender, EventArgs e) {
            MenuItem menuItem = sender as MenuItem;
            if (menuItem == null)
                return;

            Note note = menuItem.CommandParameter as Note;
            if (note == null)
                return;

            await DeleteNote(note);
        }

        void List_ItemTapped(object sender, Xamarin.Forms.ItemTappedEventArgs e) {
            Note note = e.Item as Note;
            if (note == null)
                return;

            EditNote(note);
        }

        void EditNote(Note note) {
            this.Navigation.PushAsync(new EditNotePage() { BindingContext = new EditNoteViewModel(note, ViewModel.Project.Name) });
        }

        async Task RowMenu_Clicked(object sender, System.EventArgs e) {
            string action = await DisplayActionSheet("Note action:", "Cancel", null, "Edit", "Delete");
            if (action == null)
                return;
            
            BindableObject bindableSender = sender as BindableObject;
            if(bindableSender != null) {
                Note note = bindableSender.BindingContext as Note;
                if (action == "Edit") {
                    EditNote(note);
                } else if(action == "Delete") {
                    await DeleteNote(note);
                }
            }
        }

        async Task DeleteNote(Note note) {
            bool answer = await DisplayAlert("Are you sure?", "Would you like to remove this note", "Yes", "No");
            if (answer)
                ViewModel.DeleteNote(note);
        }
    }

    public class MyCellGrid : Grid {
        protected override SizeRequest OnMeasure(double widthConstraint, double heightConstraint) {
            SizeRequest sizeRequest = base.OnMeasure(widthConstraint, heightConstraint);
            if (sizeRequest.Request.Height <= 150)
                return sizeRequest;
            
            return new SizeRequest(new Size() { Width = sizeRequest.Request.Width, Height = 150 });
        }
    }

    public class MyLabel : Label {
        protected override void OnPropertyChanged([CallerMemberName] string propertyName = null) {
            base.OnPropertyChanged(propertyName);

            if (propertyName == "Text") {
                ((this.Parent as MyCellGrid).Parent as Cell).ForceUpdateSize();
            }
        }
    }
}
