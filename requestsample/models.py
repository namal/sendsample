from django.db import models
from master.models import Purpose
# app : requestsample

# Request
# ---> purpose
# ---> buyer
# ---> season
# ---> style
# 	Request_QTY
# 	---> request_id
# 	---> delivery
# 	---> color
# 	---> size
# 	---> qty
# ---> decision # this is 1 or 0
# ---> remark
# ---> create_date
# ---> create_by


class Request(models.Model):

    DECISIONS_CATOGARY = [
        ('1', 'Approved'),
        ('0', 'Reject'),
    ]
    purpose = models.ForeignKey(
        Purpose, on_delete=models.CASCADE)
    buyer = models.CharField(max_length=255)
    season = models.CharField(max_length=255)
    style = models.CharField(max_length=255)
    decision = models.IntegerField(
        choices=DECISIONS_CATOGARY, default=0)
    remark = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)


class Request_QTY(models.Model):
    request = models.ForeignKey(
        Request, on_delete=models.CASCADE)
    delivery = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    size_wise_qty = models.IntegerField()
    date_add = models.DateTimeField(auto_now_add=True)
