using System;
using System.ComponentModel;
using System.Runtime.CompilerServices;

namespace TodoList.Model {
    public class NotificationObject : INotifyPropertyChanged {
        public event PropertyChangedEventHandler PropertyChanged;

        protected void RaisePropertyChanged([CallerMemberName] string name = null) {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));
        }
    }
}
