from enum import Enum

from django.contrib.auth.models import (
    BaseUserManager
)


class UserRoles(Enum):
    USER = ('user', 'пользователь')
    ADMIN = ('admin', 'администратор')


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone,
                    password=None, role=UserRoles.USER.value[0]):
        if not email:
            raise ValueError('The user must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role=role
        )
        user.is_active = True
        user.set_password(password),
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone,
                         password=None, role=UserRoles.ADMIN.value[0]):
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            role=role
        )
        user.save(using=self._db)

        return user
