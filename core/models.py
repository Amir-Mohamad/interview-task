# app/models.py

from django.db import models

class Titanic(models.Model):
    PassengerId = models.IntegerField()
    Survived = models.BooleanField()
    Pclass = models.IntegerField()
    Name = models.CharField(max_length=100)
    Sex = models.CharField(max_length=10)
    Age = models.IntegerField(null=True)
    SibSp = models.IntegerField()
    Parch = models.IntegerField()
    Ticket = models.CharField(max_length=20)
    Fare = models.FloatField()
    Cabin = models.CharField(max_length=20, null=True)
    Embarked = models.CharField(max_length=1)

    def __str__(self):
        return self.Name