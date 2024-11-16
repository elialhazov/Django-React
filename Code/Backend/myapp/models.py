from django.db import models

class ExampleTable(models.Model):
    column1 = models.CharField(max_length=100)
    column2 = models.IntegerField()

    def __str__(self):
        return self.column1


class Color(models.Model):  # הפיכת Color למודל תקין
    name = models.CharField(max_length=100)
    hex_value = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.name} ({self.hex_value})"


# מודל לחישובים
class Calculation(models.Model):
    num1 = models.IntegerField()  # המספר הראשון
    num2 = models.IntegerField()  # המספר השני
    result = models.IntegerField()  # התוצאה

    def __str__(self):
        return f"{self.num1} + {self.num2} = {self.result}"
