using System;
using Xamarin.Forms;

namespace TodoList.Model {
    public class Note : NotificationObject {
        //public string UserIconPath { get; set; }
        //public string UserName { get; set; }
        //public DateTime EditTime { get; set; }
        //public string Text { get; set; }

        string userIconPath = null;
        public string UserIconPath { 
            get { return userIconPath; }
            set {
                if(userIconPath != value) {
                    userIconPath = value;
                    RaisePropertyChanged();
                }
            }
        }

        string userName = "";
        public string UserName {
            get { return userName; }
            set {
                if (userName != value) {
                    userName = value;
                    RaisePropertyChanged();
                }
            }
        }

        DateTime editTime = DateTime.MinValue;
        public DateTime EditTime {
            get { return editTime; }
            set {
                if (editTime != value) {
                    editTime = value;
                    RaisePropertyChanged();
                }
            }
        }

        string text = "";
        public string Text {
            get { return text; }
            set {
                if (text != value) {
                    text = value;
                    RaisePropertyChanged();
                }
            }
        }

        public static Note CreateCurrentUserNote() {
            return new Note() { UserName = "Первый пользователь", UserIconPath = "TodoList.Images.User1.png", EditTime = DateTime.Now, Text = "" };
        }
    }
}
