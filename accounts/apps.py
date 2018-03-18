from django.apps import AppConfig
from django.db.models.signals import post_save
from accounts.signals import verify_email, send_email


class AccountConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        User = self.get_model('User')
        EmailVerification = self.get_model('EmailVerification')
        post_save.connect(verify_email, sender=User)
        post_save.connect(send_email, sender=EmailVerification)
