from django.shortcuts import render
from home.models import Students
from home.serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.



def student_detail(request):
    std = Students.objects.get(id=1)
    #student object
    print(std)
    # anu
    serializer = StudentSerializers(std)
    # attribute will return a Python dictionary representation of the serialized data from the std object.
    print(serializer.data)
    # {'name': 'anu', 'roll': 101, 'distict': 'Malappuram'}
    json_data = JSONRenderer().render(serializer.data)
    # In the code you provided, you are using the JSONRenderer to render the data from the serializer into JSON format.
    print(json_data)
    # b'{"name":"anu","roll":101,"distict":"Malappuram"}'
    return HttpResponse(json_data,content_type='application/json')