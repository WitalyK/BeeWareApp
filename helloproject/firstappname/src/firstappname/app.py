"""
Description my first app
"""
import vlc
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class Firstformalname(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()
        self.button = toga.Button('Играй', on_press=self.video, style=Pack(padding=20))
        main_box.add(self.button)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.vlc_instance = vlc.Instance()
        self.player = self.vlc_instance.media_player_new()
        media = self.vlc_instance.media_new("rtsp://192.168.10.67:8500/doccto")
        self.player.set_media(media)
        self.main_window.show()

    def video(self, widget):
        if self.player.is_playing():
            self.player.stop()
            self.button.label = 'Играй'
        else:
            self.player.play()
            self.button.label = 'Стоп'


def main():
    return Firstformalname()
