from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import StudentSerializer

class StudentAPIView(APIView):

    def post(self, request):

        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
