from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)


class User(AbstractUser):
    about = models.TextField(max_length=500, blank=True)
    role_id = models.ForeignKey(
        Role,
        related_name='users',
        on_delete=models.SET_NULL,
        null=True
    )
    full_name = models.TextField(max_length=100, blank=True)


class Document(models.Model):
    title = models.CharField(max_length=255, blank=False, unique=True)
    content = models.TextField(blank=True)
    access = models.CharField(default='public', max_length=100)
    author = models.ForeignKey(
        User,
        related_name='documents',
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def user(self):
        return {
            'username': self.author.username,
            'role_id': self.author.role_id.id
        }

    @property
    def author_id(self):
        return self.author.id
