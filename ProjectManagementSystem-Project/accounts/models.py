from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField

class CustomManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Create and save a user with the given email, and
        password.
        """
        if not email:
            raise ValueError('The given email must be set')
        if not password:
            raise ValueError('Account must have a password.')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


# Custom User Model
class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',
                              max_length=255,
                              unique=True,
                              null=True
                              )
    full_name = models.CharField(max_length=128, blank=True)
    mobile_verified = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    mobile = PhoneNumberField(null=True, unique=True, default=None)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomManager()

    is_manager = models.BooleanField(default=True)
    is_member = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if(self.email):
            return self.email
        else:
            return str(self.mobile)

    def get_email(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
