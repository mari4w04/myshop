from django.apps import AppConfig


class LoginappConfig(AppConfig):
    name = 'loginapp'

    def ready(self):
        import loginapp.signals