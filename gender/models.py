from django.db import models
from dj.choices import Choices, Choice
from dj.choices.fields import ChoiceField

class Gender(Choices):
    male = Choice("male")
    female = Choice("female")
    not_specified = Choice("not specified")

class Persona(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class User(models.Model):
    gender = ChoiceField(choices=Gender,
            default=Gender.not_specified)

    def greet(self):
        if self.gender == Gender.male:
            return 'Boy'
        elif self.gender == Gender.female:
            return 'Hello, girl.'
        else:
            return 'Hey there, user!'
# Create your models here.
