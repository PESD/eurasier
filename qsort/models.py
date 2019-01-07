from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Program(models.Model):
    title = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.title

class Package(models.Model):
    LOW = 0
    MID = 1
    HIGH = 2
    BUDGET_LEVEL_CHOICES = (
        (LOW, 'Low'),
        (MID, 'Mid'),
        (HIGH, 'High'),
    )
    title = models.CharField(max_length=255, blank=False)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='packages')
    cost = models.IntegerField(null=False, default=1000)
    budget_level = models.IntegerField(null=False, choices=BUDGET_LEVEL_CHOICES)

    def __str__(self):
        return self.program.title + " - " + self.get_budget_level_display() + " - " + self.title

class Votes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    votes = models.IntegerField(null=False)


