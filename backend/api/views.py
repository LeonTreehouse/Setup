from rest_framework import views, status
from rest_framework.response import Response
from api.models import Car
from api.serializers import CarSerializer


# Create your views here.
class CarView(views.APIView):
    serializer_class = CarSerializer

    # Get request

    def get(self, request, format=None):
        query_set = Car.objects.all()
        serializer = self.serializer_class(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Post request
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)