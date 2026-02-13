from django.db import models
from django.contrib.auth.models import User
from skills.models import Skill


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profiles/', default='default.png')

    skills_teach = models.ManyToManyField(Skill, related_name='teach', blank=True)
    skills_learn = models.ManyToManyField(Skill, related_name='learn', blank=True)

    def __str__(self):
        return self.user.username
