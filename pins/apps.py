from django.apps import AppConfig


class PinsConfig(AppConfig):
    name = 'pins'

    def ready(self):
        import pins.signals
