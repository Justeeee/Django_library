import uuid

from django.db import models


class Book(models.Model):
    # Base info
    name = models.CharField(max_length=255)
    writer = models.ForeignKey('apps.Writer', models.CASCADE)
    publisher = models.ForeignKey('apps.Publisher', models.CASCADE)
    edition = models.CharField(max_length=255)
    edition_year = models.IntegerField()
    pages = models.IntegerField()
    # document = TODO add document
    # Full info
    description = models.TextField()

    subjects = models.ManyToManyField('apps.Subject')

    # Classifications
    internet_archive = models.TextField()

    def __str__(self):
        return self.name


class Writer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    b_day = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Subject(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField()

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

