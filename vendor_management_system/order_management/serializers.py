from rest_framework import serializers
from .models import PurchaseOrder

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        read_only_fields = [
            "po_number", "vendor", "order_date", "delivery_date", "status", 
            "quality_rating", "issue_date", "acknowledgment_date",
        ]