from api.models import *
from api.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(["GET", "POST"])
def getSupply(request):
    """
    List all supplies, or create a new supply.
    """
    if request.method == "GET":
        supply = Supply.objects.all()
        serializer = SupplySerializer(supply, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = SupplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

