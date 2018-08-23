using System;
using TodoList.ViewModel;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

[assembly: XamlCompilation(XamlCompilationOptions.Compile)]
namespace TodoList {
    public partial class App : Application {
        public App() {
            InitializeComponent();

            NavigationPage navigation = new NavigationPage();
            navigation.PushAsync(new View.ProjectsPage() { BindingContext = new MainViewModel() });
            MainPage = navigation;
        }

        protected override void OnStart() {
            // Handle when your app starts
        }

        protected override void OnSleep() {
            // Handle when your app sleeps
        }

        protected override void OnResume() {
            // Handle when your app resumes
        }
    }
}
