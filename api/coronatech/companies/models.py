from django.db import models
from django.db.models import URLField
from django.utils.timezone import now


class Company(models.Model):
    class CompanyStatus(models.TextChoices):
        # text choices is a nested class to define choices which variable can have
        LAYOFFS = "Layoffs"
        HIRING_FREEZE = "Hiring Freeze"
        HIRING = "Hiring"

    name = models.CharField(max_length=50, unique=True)
    status = models.CharField(
        choices=CompanyStatus.choices, max_length=100, default=CompanyStatus.HIRING
    )
    last_update = models.DateTimeField(default=now, editable=True)
    application_link = URLField(blank=True)
    notes = models.CharField(max_length=200, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"
