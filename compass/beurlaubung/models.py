from django.db import models
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from django.utils.crypto import get_random_string

class beurlaubung(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    slug = AutoSlugField(unique=True, always_update=False)
    name = models.CharField("Name des Antragsstellers", max_length=255)
    klasse = models.CharField("Klasse des Antragsstellers", max_length=10)
    datum_gestellt = models.DateTimeField(auto_now_add=True) 
    tutor = models.CharField("Kürzel des Tuturs", max_length=3)
    begruendung = models.CharField("Begründung des Antrages", max_length=1000)

    def __str__(self):
        return self.name
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.slug:
            unique_slug = False
            while not unique_slug:
                random_slug = get_random_string(10)
                if not self.__class__.objects.filter(slug=random_slug).exists():
                    unique_slug = True
            self.slug = random_slug    

    def getredirceturl(self, pfad):
        return pfad + self.slug
