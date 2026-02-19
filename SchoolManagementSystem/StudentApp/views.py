from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Student
from .serializers import StudentSerializer

@csrf_exempt
def studentApi(request,id=0):

    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed",safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully",safe=False)

    elif request.method == 'DELETE':
        student = Student.objects.get(id=id)
        student.delete()
        return JsonResponse("Deleted Successfully",safe=False)

