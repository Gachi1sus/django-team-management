from django.db import models

class Faction(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FactionMember(models.Model):
    ROLE_CHOICES = [
        ('leader', 'Лидер'),
        ('officer', 'Офицер'),
        ('member', 'Участник'),
        ('recruit', 'Новичок'),
        ('guest', 'Гость'),
    ]


    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')
    bio = models.TextField()
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


