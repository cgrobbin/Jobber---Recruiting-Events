from django.apps import AppConfig


class MainAppConfig(AppConfig):
    name = 'main_app'

class UsersConfig(AppConfig):
    name = 'users'
    def ready(self):
        import users.signals  #noqa