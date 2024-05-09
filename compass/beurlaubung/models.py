from django.db import models

# Create your models here.
class antraege(models.Model):
    id = models.AutoField(primary_key=True)
    typ =