import operator
from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class CalculatorAPIView(APIView):

    def post(self, request, *args, **kwargs):
        print(request.data)
        value1 = int(request.data.get("value1", None))
        value2 = int(request.data.get("value2", None))
        operation = request.data.get("operation", 1)
        ops = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul}

        if operation in ops:
            output = ops[operation](value1, value2)
            return Response(output, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)




    def get(self, request, format=False):
        value1 = int(request.GET.get("value1", None))
        value2 = int(request.GET.get("value2", None))
        operation = request.GET.get("operation", 1)
        
        ops = {'add' : operator.add, '-' : operator.sub, '*' : operator.mul}
        print(value1, value2, operation)
        print(len(operation))

        print(operation in ops)

        if operation in ops:
            output = ops[operation](value1, value2)
            return Response(output, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

