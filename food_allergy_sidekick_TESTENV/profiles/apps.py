from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

class ProfilesConfig(AppConfig):
    name = 'profiles'

    def ready(self):
        import profiles.signals
