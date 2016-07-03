import kivy
from kivy.config import Config
from kivy.app import App
from kivy.lang import Builder

# Builder.load_file('data/style.kv')


class VdiClientApp(App):
  def do_login(self, username, password):
    print 'hello! %s login with password %s.' % (username.text, password.text)


if __name__ == '__main__':
  Config.set('graphics', 'fullscreen', 'auto')
  Config.write()
  VdiClientApp().run()
