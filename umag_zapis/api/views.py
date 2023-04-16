from api.models import *
from api.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q, Sum, F
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

# Supply


@api_view(["GET", "POST"])
def getSupplies(request):
    """
    List all supplies, or create a new supply.
    """
    if request.method == "GET":
        barcode = request.data["barcode"]
        from_time = request.data["fromTime"]
        to_time = request.data["toTime"]
        supply_filter = Q(barcode=barcode) & Q(
            supplyTime__gte=from_time) & Q(supplyTime__lte=to_time)
        supply = Supply.objects.filter(supply_filter)
        serializer = SupplySerializer(supply, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        max_id = Supply.objects.aggregate(models.Max("id"))["id__max"]
        if max_id is None:
            max_id = 0

        new_id = max_id + 1

        data = request.data
        data["id"] = new_id
        serializer = SupplySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"id": new_id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def getSupply(request, pk):
    """
    Retrieve, update or delete a supply.
    """
    try:
        supply = Supply.objects.get(id=pk)
    except Supply.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SupplySerializer(supply, many=False)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = SupplySerializer(
            instance=supply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
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
        max_id = Sale.objects.aggregate(models.Max("id"))["id__max"]
        if max_id is None:
            max_id = 0

        new_id = max_id + 1

        data = request.data
        data["id"] = new_id
        serializer = SaleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"id": new_id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def getSale(request, pk):
    """
    Retrieve, update or delete a sale.
    """
    try:
        sale = Sale.objects.get(id=pk)
    except Sale.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SaleSerializer(sale, many=False)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = SaleSerializer(
            instance=sale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        sale.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def getReport(request):

    startTime = time.time()

    fromTime = datetime.strptime(request.data["fromTime"], "%Y-%m-%dT%H:%M:%S")
    toTime = request.data["toTime"]
    barcode = request.data["barcode"]

    supply_q = Q(barcode=barcode) & Q(supplyTime__lte=toTime)

    supply = Supply.objects.filter(supply_q).values(
        "quantity", "price", "supplyTime").order_by("supplyTime")

    sale_q = Q(barcode=barcode) & Q(saleTime__lte=toTime)

    sale = Sale.objects.filter(sale_q).values("quantity", "price", "saleTime").order_by("saleTime")

    # sale = Sale.objects.filter(barcode=barcode, saleTime__lte=toTime).values(
    #     "quantity", "saleTime").order_by("saleTime")

    # sale = Sale.objects.filter(
    # barcode=barcode, saleTime__lte=toTime
    # ).aggregate(total=Sum("quantity"))["total"]

    quantity = Sale.objects.filter(
        barcode=barcode, saleTime__range=(fromTime, toTime)
    ).aggregate(total=Sum("quantity"))["total"]

    revenue = Sale.objects.filter(
        barcode=barcode, saleTime__range=(fromTime, toTime)
    ).aggregate(total=Sum(F("quantity") * F("price")))["total"]
    # i = 0
    # quantity = 0
    # netProfit = revenue
    # for s in sale:
    #     quantity += s["quantity"]
    #     while s["quantity"] > 0:
    #         if s["quantity"] >= supply[i]["quantity"]:
    #             s["quantity"] -= supply[i]["quantity"]
                
    #             if s["saleTime"] >= fromTime:
    #                 netProfit -= supply[i]["quantity"] * supply[i]["price"]
    #             i += 1
    #         else:
    #             supply[i]["quantity"] -= s["quantity"]
    #             if s["saleTime"] >= fromTime:
    #                 netProfit -= s["quantity"] * supply[i]["price"]
    #             break

    netProfit = 0
    i = 0
    for s in sale:
        if s["saleTime"] <= fromTime:
            netProfit = 0
        while s["quantity"] > 0:
            if s["quantity"] >= supply[i]["quantity"]:
                netProfit += supply[i]["quantity"] * (s["price"] - supply[i]["price"])
                i += 1
                s["quantity"] -= supply[i]["quantity"]
            else:
                netProfit += s["quantity"] * (s["price"] - supply[i]["price"])
                supply[i]["quantity"] -= s["quantity"]
                break

    return Response({"barcode": barcode,
                     "quantity": quantity,
                     "revenue": revenue,
                     "netProfit": netProfit})
