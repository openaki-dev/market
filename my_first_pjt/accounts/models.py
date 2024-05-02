from django.db import models
from django.contrib.auth import models as auth_models


class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # ... 필요에 따라 다른 사용자 정보 필드 추가

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    objects = auth_models.UserManager()

    def __str__(self):
        return self.username
