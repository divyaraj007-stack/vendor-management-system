import string

from django.db import models
from vendors.models import Vendor
from django.utils.crypto import get_random_string

def get_po_id():
    possible_characters = string.digits + string.ascii_uppercase
    return "PO" + get_random_string(8, allowed_chars=possible_characters)

class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    po_number = models.CharField(max_length=12, unique=True, primary_key=True, default=get_po_id)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, related_name='vendor_purchase_orders')
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(null=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
