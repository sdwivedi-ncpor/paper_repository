from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.CharField(
        _("group"),
         max_length=100,
         unique = True)
    def __str__(self):
        return self.group
    class Meta:
        ordering = ('group',)

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    department = models.CharField(
        _("department"),
         max_length=100,
         unique = True)
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        null=True,
        blank =True)
    
    def __str__(self):
        return self.department
    class Meta:
        ordering = ('department',)

class CustomUsers(AbstractUser):
    username = models.EmailField(_("username"), unique=True)
    email = models.EmailField(_("email address"), unique=True)
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        null=True,
        blank =True)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True,
        blank =True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super(CustomUsers, self).save(*args, **kwargs)