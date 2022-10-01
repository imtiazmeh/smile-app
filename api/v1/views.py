from django.shortcuts import render
import io
from requests import delete
from rest_framework.parsers import JSONParser
from api.serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from api.v1.models import Student
# Create your views here.

# Class Based API


@method_decorator(csrf_exempt, name='dispatch')
class StudenAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        if not json_data:
            student = Student.objects.all()
            serializer = StudentSerializer(student, many=True)
            return JsonResponse(serializer.data, safe=False)
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Student Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Student Updated !'}
            return JsonResponse(res, safe=False)
        return JsonResponse(serializer.errors, safe=False)

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = Student.objects.get(id=id)
        student.delete()
        res = {'msg': 'Student has been deleted !'}
        return JsonResponse(res, safe=False)

# Function Based API


@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Student Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')


def get_specific_student(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get(id, None)
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return JsonResponse(serializer.data, safe=False)
        student = Student.objects.all()
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data, safe=False)


def update_student(request):
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get(id)
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Student Updated !'}
            return JsonResponse(res, safe=False)
        return JsonResponse(serializer.errors, safe=False)

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = Student.objects.get(id=id)
        student.delete()
        res = {'msg': 'Student has been deleted !'}
        return JsonResponse(res, safe=False)
