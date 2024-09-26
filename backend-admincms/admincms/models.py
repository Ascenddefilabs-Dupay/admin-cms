from django.db import models
import random
from cloudinary.models import CloudinaryField

class AdminCMS(models.Model):
    id = models.PositiveIntegerField(primary_key=True, editable=False)
    account_type = models.CharField(max_length=100, null=True, blank=True)
    currency_type = models.CharField(max_length=100, blank=True, null=True)
    icon = CloudinaryField('icon', folder='admin', blank=True, null=True)  # Cloudinary field to upload the icon

    def __str__(self):
        return f"Account: {self.account_type}, Currency: {self.currency_type}"

    class Meta:
        db_table = 'admincms'

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.generate_unique_id()
        super().save(*args, **kwargs)

    def generate_unique_id(self):
        while True:
            new_id = random.randint(100000, 999999)
            if not AdminCMS.objects.filter(id=new_id).exists():
                return new_id
