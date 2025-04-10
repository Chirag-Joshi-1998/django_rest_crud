from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializers
from django.views.decorators.csrf import csrf_exempt
import io
# Create your views here.

def student_detail(request,pk):
    stu = Student.objects.get(id=pk)
    serializers=StudentSerializers(stu)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data)


def student_list(request):
    stu = Student.objects.all()
    serializers=StudentSerializers(stu,many=True)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data)

@csrf_exempt
def student_create(request):
    if request.method=='POST':
        json_data=request.body
        strem = io.BytesIO(json_data)
        pythondata= JSONParser().parse(strem)
        serializer = StudentSerializers(data=pythondata)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data Inserted'}
            json_data =JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
        
        