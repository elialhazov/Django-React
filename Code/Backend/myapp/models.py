from django.db import models

class ExampleTable(models.Model):
    column1 = models.CharField(max_length=100)
    column2 = models.IntegerField()

    def __str__(self):
        return self.column1

