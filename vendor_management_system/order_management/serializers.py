from django.utils import timezone
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


class PurchaseOrderIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ("vendor", )

    def update(self, instance, validated_data):
        """
        Update the PurchaseOrder instance with the issue_date.
        """
        instance.issue_date = timezone.now()
        instance.vendor = validated_data['vendor']
        instance.save()
        return instance


class PurchaseOrderAcknowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ("deli", )

    def update(self, instance, *args, **kwargs):
        """
        Update the PurchaseOrder instance with the acknowledgment_date.
        """
        instance.acknowledgment_date = timezone.now()
        instance.save()
        return instance

        