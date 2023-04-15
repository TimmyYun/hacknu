from api.models import *
from api.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from datetime import datetime

import time 

@api_view(["GET"])
def getRoutes(request):
    routes = [
        {
            "/api/supplies",
            "/api/sales",
        }
    ]
    return Response(routes)

#Supply

@api_view(["GET", "POST"])
def getSupplies(request):
    """
    List all supplies, or create a new supply.
    """
    if request.method == "GET":
        barcode = request.data['barcode']
        from_time = request.data['fromTime']
        to_time = request.data['toTime']
        supply_filter = Q(barcode=barcode) & Q(supply_time__gte=from_time) & Q(supply_time__lte=to_time)

        supply = Supply.objects.filter(supply_filter)
        serializer = SupplySerializer(supply, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        max_id = Supply.objects.aggregate(models.Max('id'))['id__max']
        if max_id is None:
            max_id = 0

        new_id = max_id + 1

        data = request.data
        data['id'] = new_id
        serializer = SupplySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"id": new_id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getSupply(request, pk):
    """
    Retrieve, update or delete a supply.
    """
    try:
        supply = Supply.objects.get(id=pk)
    except Supply.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SupplySerializer(supply, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = SupplySerializer(
            instance=supply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        supply.delete()
        return Response(status=status.HTTP_200_OK)




@api_view(["GET", "POST"])
def getSales(request):
    """
    List all sales, or create a new sale.
    """
    if request.method == "GET":
        sale = Sale.objects.all()
        serializer = SaleSerializer(sale, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        max_id = Sale.objects.aggregate(models.Max('id'))['id__max']
        if max_id is None:
            max_id = 0

        new_id = max_id + 1

        data = request.data
        data['id'] = new_id
        serializer = SaleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"id": new_id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def getSale(request, pk):
    """
    Retrieve, update or delete a sale.
    """
    try:
        sale = Sale.objects.get(id=pk)
    except Sale.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SaleSerializer(sale, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = SaleSerializer(
            instance=sale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        sale.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def getReport(request):

    startTime = time.time()

    fromTime = datetime.strptime(request.data['fromTime'], "%Y-%m-%d")
    toTime = request.data['toTime']
    barcode = request.data['barcode']
    #Quantity price time
    supply_q = Q(barcode=barcode) & Q(supply_time__lte=toTime)

    supply = Supply.objects.filter(supply_q).values('quantity', 'price', 'supply_time').order_by('supply_time')
    

    sale_q = Q(barcode=barcode) & Q(sale_time__lte=toTime)
    
    sale = Sale.objects.filter(sale_q).values('quantity', 'price', 'sale_time').order_by('sale_time')

    i = 0
    sum_margin = 0
    for s in sale:
        if s['sale_time'] <= fromTime:
            sum_margin = 0

        while i < len(supply) and s['quantity'] > 0 and s['sale_time'] >= supply[i]['supply_time']:
            if s['quantity'] >= supply[i]['quantity']:
                sum_margin += supply[i]['quantity'] * (s['price'] - supply[i]['price'])
            else:

                sum_margin += s['quantity'] * (s['price'] - supply[i]['price'])
                supply[i]['quantity'] -= s['quantity']
                break

            s['quantity'] -= supply[i]['quantity']
            i += 1

        if (i >= 3 or s['sale_time'] < supply[i]['supply_time']):
            sum_margin += s['quantity'] * s['price']

    finalTime = time.time() - startTime

    print("Total Margin =", sum_margin)
    return Response({"magrin": sum_margin, "time": finalTime})