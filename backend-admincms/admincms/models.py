from django.db import models

class AdminCMS(models.Model):
    account_type = models.CharField(max_length=100,primary_key=True, blank=True)
    currency_type = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Account: {self.account_type}, Currency: {self.currency_type}"

    class Meta:
            db_table = 'admincms'