from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, loginid, password, **extra_fields):
        if not loginid:
            raise ValueError(_('The loginid must be set'))
        user = self.model(loginid=loginid, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, loginid, password, **extra_fields):
        return self.create_user(loginid, password, **extra_fields)
