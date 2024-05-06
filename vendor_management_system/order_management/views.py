from rest_framework import viewsets, decorators, response
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer, PurchaseOrderAcknowledgeSerializer, PurchaseOrderIssueSerializer

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    http_method_names = [
        "get",
        "post",
        "put",
        "delete",
    ]

    @decorators.action(methods=["POST"], detail=True, serializer_class=PurchaseOrderIssueSerializer)
    def issue_order(self, request, *args, **kwargs):
        order_id = kwargs.get('pk')
        po = PurchaseOrder.objects.filter(po_number=order_id).first()
        
        if po is None:
            return response.Response(data={"message": "No order Found"}, status=404)

        serializer = PurchaseOrderIssueSerializer(instance=po, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(data={"message": "Your Order has been Issue"}, status=200)

        return response.Response(data={"message": serializer.errors}, status=200)

    @decorators.action(methods=["POST"], detail=True, serializer_class=PurchaseOrderAcknowledgeSerializer)
    def acknowledge_order(self, request, *args, **kwargs):
        print(kwargs)
        order_id = kwargs.get('pk')
        po = PurchaseOrder.objects.filter(po_number=order_id).first()
        
        # print(po)
        if po is None:
            return response.Response(data={"message": "No order Found"}, status=404)
        
        serializer = PurchaseOrderAcknowledgeSerializer(data={},instance=po)
        serializer.is_valid()
        serializer.save()

        return response.Response(data={"message": "Your Order has been Acknowledged!"}, status=200)
