from django.apps import AppConfig

class MusicConfig(AppConfig):
    # name = 'music_site'
    # label = 'my.music_site'  # <-- this is the important line - change it to anything other than the default, which is the module name ('foo' in this case)
    name = 'music'
    # default_app_config = 'full.python.path.to.your.app.foo.apps.FooConfig'