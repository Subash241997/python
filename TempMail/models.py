from django.db import models

# Create your models here.
class Email(models.Model):
    email_address = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Email to {self.email_address} at {self.received_at}"