using System;
using System.Globalization;
using Xamarin.Forms;

namespace TodoList.Utils {
    public class PathToImageConverter : IValueConverter {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture) {
            if (value == null)
                return null;
            
            return ImageSource.FromResource(value.ToString());
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture) {
            throw new NotImplementedException();
        }
    }
}
