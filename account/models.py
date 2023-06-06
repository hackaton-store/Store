from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):

    def _create(self, username, email, password, **extra_info):
        if not username:
            raise ValueError('Enter username')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_info)
        user.set_password(password)
        user.save()
        return user
    

    def create_user(self, username, email, password, **extra_info):
        extra_info.setdefault('is_active', False)
        extra_info.setdefault('is_staff', False)
        return self._create(username, email, password, **extra_info)
    

    def create_superuser(self, username, email, password, **extra_info):
        extra_info.setdefault('is_active', True)
        extra_info.setdefault('is_staff', True)
        return self._create(username, email, password, **extra_info)
    

class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=10, blank=True)

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    objects = UserManager()

    def has_module_perms(self, app_label):
        print(app_label)
        return self.is_staff
    
    def has_perm(self, obj=None):
        return self.is_staff
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'