# relationship_app/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    # You can add additional fields here if needed
    groups = models.ManyToManyField(
        Group,
        related_name='relationship_app_user_set',  # Updated related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='relationship_app_user_set',  # Updated related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title