from django.db import models

# Create your models here.
class Book(models.Model):

    class BookConditions(models.TextChoices):
        NEW = 'N', ('New')
        VERY_GOOD = 'VG', ('Very Good')
        GOOD = 'G', ('Good')
        USED = 'U', ('Used')
        NEEDS_REPAIR = 'NR', ('Needs Repair')
    title = models.CharField(max_length=200)
    author_first = models.CharField(max_length=60)
    author_last = models.CharField(max_length=60)
    fiction = models.BooleanField(default=False)
    condition = models.CharField(max_length=2, choices=BookConditions.choices, default=BookConditions.GOOD)
    assunta_read = models.BooleanField(default=False)
    lucian_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.author_first} {self.author_last}"