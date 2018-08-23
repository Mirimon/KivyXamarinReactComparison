using System;
using System.Collections.Generic;
using TodoList.ViewModel;
using Xamarin.Forms;

namespace TodoList.View {
    public partial class EditNotePage : ContentPage {
        EditNoteViewModel ViewModel { get { return BindingContext as EditNoteViewModel; } }

        public EditNotePage() {
            InitializeComponent();
        }

        void Save_Clicked(object sender, EventArgs e) {
            ViewModel.SaveText();
        }
    }
}
