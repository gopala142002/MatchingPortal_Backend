from django.db import models
from django.conf import settings

class Reviewer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviewer"
    )

    reviewer_name = models.CharField(max_length=255)
    institutes = models.JSONField(default=list)
    research_domains = models.JSONField(default=list)
    keywords = models.JSONField(default=list)

    class Meta:
        db_table = "reviewers"

    def __str__(self):
        return self.reviewer_name
