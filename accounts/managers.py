from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, mail_verified=False):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            mail_verified=mail_verified,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, mail_verified=True):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            mail_verified=mail_verified,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
