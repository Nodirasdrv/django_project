from django.db import models


class Phone(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()
    kg_price = models.IntegerField(null=False)
    usd_price = models.IntegerField(null=False)

    def __str__(self):
        return self.title



