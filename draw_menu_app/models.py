from django.core import validators
from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=255, unique=True, validators=[
        validators.MinLengthValidator(1),
    ])


class MenuNode(models.Model):
    name = models.CharField(max_length=255, unique=True, validators=[
        validators.MinLengthValidator(1),
    ])
    readable_name = models.TextField()
    parent_node = models.ForeignKey(
        'MenuNode',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True,
        default=None,
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='nodes',
    )


    def __str__(self) -> str:
        parent_name = self.parent_node.name if self.parent_node else None
        return f'MenuNode(name="{self.name}", parent_node="{parent_name}")'
