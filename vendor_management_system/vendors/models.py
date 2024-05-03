import string

from django.db import models
from django.utils.crypto import get_random_string


def get_vendor_code():
    possible_characters = string.digits + string.ascii_uppercase
    return get_random_string(10, allowed_chars=possible_characters)


class Vendor(models.Model):
    vendor_code = models.CharField(max_length=12, unique=True, primary_key=True, default=get_vendor_code)
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.name