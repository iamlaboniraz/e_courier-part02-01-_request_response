from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'account'
    icon_name = 'favorite'
    def ready(self):
        import account.signals
