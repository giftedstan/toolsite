from django.db import models

# Create your models here.

class TemplateRecord(models.Model):
    temp=models.CharField(max_length=100, blank=True, null=True)
    date_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link