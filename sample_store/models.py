from django.db import models


class Style(models.Model):
    buyer = models.CharField(max_length=255)
    buyer_season = models.CharField(max_length=255)
    style = models.CharField(max_length=255)
    sc = models.CharField(max_length=255)
    delivery = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    size_wise_qty = models.IntegerField()
    date_add = models.DateTimeField(auto_new_add=True)
