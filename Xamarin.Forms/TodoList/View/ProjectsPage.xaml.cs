using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Forms;
using System.Reflection;
using TodoList.Model;
using TodoList.ViewModel;

namespace TodoList.View {
    public partial class ProjectsPage : ContentPage {
        MainViewModel ViewModel { get { return BindingContext as MainViewModel; } }

        public ProjectsPage() {
            InitializeComponent();
        }

        async Task AddNew_Clicked(object sender, EventArgs e) {
            string result = await InputBox(this.Navigation);
            if (result == null)
                return;

            ViewModel.AddNewProject(result);
        }

        async Task DeleteItem_Clicked(object sender, EventArgs e) {
            MenuItem menuItem = sender as MenuItem;
            if (menuItem == null)
                return;

            Project project = menuItem.CommandParameter as Project;
            if (project == null)
                return;

            bool answer = await DisplayAlert("Are you sure?", string.Format("Would you like to remove the {0} project", project.Name), "Yes", "No");
            if(answer)
                ViewModel.DeleteProject(project);
        }

        void List_ItemTapped(object sender, Xamarin.Forms.ItemTappedEventArgs e) {
            Project project = e.Item as Project;
            if (project == null)
                return;

            this.Navigation.PushAsync(new NotesPage() { BindingContext = new ProjectViewModel(project) });
        }

        public static Task<string> InputBox(INavigation navigation) {
            // wait in this proc, until user did his input 
            var tcs = new TaskCompletionSource<string>();

            var lblTitle = new Label { Text = "Title", HorizontalOptions = LayoutOptions.Center, FontAttributes = FontAttributes.Bold };
            var lblMessage = new Label { Text = "Enter new text:" };
            var txtInput = new Entry { Text = "" };

            var btnOk = new Button {
                Text = "Ok",
                WidthRequest = 100,
                BackgroundColor = Color.FromRgb(0.8, 0.8, 0.8),
            };
            btnOk.Clicked += async (s, e) => {
                // close page
                var result = txtInput.Text;
                await navigation.PopModalAsync();
                // pass result
                tcs.SetResult(result);
            };

            var btnCancel = new Button {
                Text = "Cancel",
                WidthRequest = 100,
                BackgroundColor = Color.FromRgb(0.8, 0.8, 0.8)
            };
            btnCancel.Clicked += async (s, e) => {
                // close page
                await navigation.PopModalAsync();
                // pass empty result
                tcs.SetResult(null);
            };

            var slButtons = new StackLayout {
                Orientation = StackOrientation.Horizontal,
                Children = { btnOk, btnCancel },
            };

            var layout = new StackLayout {
                Padding = new Thickness(0, 40, 0, 0),
                VerticalOptions = LayoutOptions.StartAndExpand,
                HorizontalOptions = LayoutOptions.CenterAndExpand,
                Orientation = StackOrientation.Vertical,
                Children = { lblTitle, lblMessage, txtInput, slButtons },
            };

            // create and show page
            var page = new ContentPage();
            page.Content = layout;
            navigation.PushModalAsync(page);
            // open keyboard
            txtInput.Focus();

            // code is waiting her, until result is passed with tcs.SetResult() in btn-Clicked
            // then proc returns the result
            return tcs.Task;
        }
    }
}
