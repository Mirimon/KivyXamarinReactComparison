# -*- coding: utf-8 -*-

# Точка входа в приложение. Запускает основной программный код program.py.
# В случае ошибки, выводит на экран окно с её текстом.

import os
import sys
import traceback

from kivy.config import Config

# Никнейм и имя репозитория на github,
# куда будет отправлен отчёт баг репорта.
NICK_NAME_AND_NAME_REPOSITORY = 'https://github.com/Mirimon/KivyXamarinReactComparison/tree/master/Kivy'

directory = os.path.split(os.path.abspath(sys.argv[0]))[0]
sys.path.insert(0, os.path.join(directory, 'libs/applibs'))
sys.dont_write_bytecode = True
Config.set('kivy', 'keyboard_mode', 'system')

try:
    import webbrowser
    try:
        import six.moves.urllib
    except ImportError:
        pass

    import kivy
    kivy.require('1.9.2')

    from libs.applibs.kivymd.theming import ThemeManager
    # Activity баг репорта.
    from libs.applibs.bugreporter import BugReporter
except Exception:
    text_error = traceback.format_exc()
    print(text_error)
    traceback.print_exc(file=open(os.path.join(directory, 'error.log'), 'w'))
    sys.exit(1)


__version__ = '0.0.1'


def main():
    def create_error_monitor():
        class _App(App):
            theme_cls = ThemeManager()
            theme_cls.primary_palette = 'BlueGrey'

            def build(self):
                box = BoxLayout()
                box.add_widget(report)
                return box
        app = _App()
        app.run()

    app = None

    try:
        from todolist import TodoList  # основной класс программы

        # Запуск приложения.
        app = TodoList()
        app.run()
    except Exception:
        from kivy.app import App
        from kivy.uix.boxlayout import BoxLayout

        text_error = traceback.format_exc()
        print(text_error)
        traceback.print_exc(file=open(os.path.join(directory, 'error.log'), 'w'))

        if app:
            try:
                app.stop()
            except AttributeError:
                app = None

        def callback_report(*args):
            '''Функция отправки баг-репорта.'''

            try:
                txt = six.moves.urllib.parse.quote(
                    report.txt_traceback.text.encode('utf-8')
                )
                url = 'https://github.com/%s/issues/new?body=' % NICK_NAME_AND_NAME_REPOSITORY + txt
                webbrowser.open(url)
            except Exception:
                sys.exit(1)

        report = BugReporter(
            callback_report=callback_report, txt_report=text_error,
            icon_background='data/images/icon.png')
        if app:
            try:
                app.screen.clear_widgets()
                app.screen.add_widget(report)
            except AttributeError:
                create_error_monitor()
        else:
            create_error_monitor()


if __name__ in ('__main__', '__android__'):
    main()
