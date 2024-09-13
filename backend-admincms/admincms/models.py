from django.db import models

class AdminCMS(models.Model):
    id = models.AutoField(primary_key=True) 
    account_type = models.CharField(max_length=100,null=True, blank=True)
    currency_type = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Account: {self.account_type}, Currency: {self.currency_type}"

    class Meta:
            db_table = 'admincms'