from django.db import models

# Create your models here.
class SubmitModel(models.Model):
    letter = models.CharField(max_length=1)

    def __str__(self):
        return self.letter

class Db_SubmitModel(models.Model):
    word_db = models.CharField(max_length=1)

    def __str__(self):
        return self.word_db