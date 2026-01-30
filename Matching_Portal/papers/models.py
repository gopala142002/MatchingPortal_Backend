from django.db import models
from django.conf import settings


class Paper(models.Model):

    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("reviewing", "Reviewing"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
        ("published", "Published"),
    ]

    id = models.BigAutoField(primary_key=True)

    title = models.CharField(max_length=500)

    abstract = models.TextField()

    keywords = models.JSONField()

    subject_area = models.CharField(max_length=200)

    pdf_url = models.URLField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="papers"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="submitted"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
