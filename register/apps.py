from __future__ import unicode_literals
from django.apps import AppConfig


class RegisterConfig(AppConfig):
    name = 'register'

    def ready(self):
        # we make signals active
        import register.signals