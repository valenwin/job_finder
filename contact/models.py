from django.db import models


class ContactUs(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=50, null=True)
    description = models.TextField(blank=True, db_index=True)

    class Meta:
        verbose_name = "Contacts"
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
