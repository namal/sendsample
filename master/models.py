from django.db import models

# app : master
# ------------------------
# Purpose
# ---> purpose


class Purpose(models.Model):
    purpose = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

# Issue_Approval
# ---> approval_person


class Issue_Approval_By(models.Model):
    approval_person = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

# Request_Approval
# ---> approval_person


class Request_Approval_By(models.Model):
    approval_person = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
