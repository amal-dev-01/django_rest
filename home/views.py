from django.shortcuts import render
from home.models import Students
from home.serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.



def student_detail(request,pk):
    std = Students.objects.get(id=pk)
    serializer = StudentSerializers(std)
    return JsonResponse(serializer.data)


# def student_detail(request,pk):
#     std = Students.objects.get(id=pk)
#     #student object
#     print(std)
#     # anu
#     serializer = StudentSerializers(std)
#     # attribute will return a Python dictionary representation of the serialized data from the std object.
#     # print(serializer.data)
#     # {'name': 'anu', 'roll': 101, 'distict': 'Malappuram'}
#     json_data = JSONRenderer().render(serializer.data)
#     # In the code you provided, you are using the JSONRenderer to render the data from the serializer into JSON format.
#     # print(json_data)
#     # b'{"name":"anu","roll":101,"distict":"Malappuram"}'
#     return HttpResponse(json_data,content_type='application/json')




def student_list(request):
    std = Students.objects.all()
    # it will bu return a queryset
    print(std)
    # <QuerySet [<Students: anu>, <Students: Aju>, <Students: thanu>]>
    serializer = StudentSerializers(std ,many=True)
    #  the many argument is used when you want to serialize multiple objects (e.g., a queryset of objects) with the same serializer.
    # attribute will return a Python dictionary representation of the serialized data from the std object.
    # print(serializer.data)
    # [OrderedDict([('name', 'anu'), ('roll', 101), ('distict', 'Malappuram')]), OrderedDict([('name', 'Aju'), ('roll', 102), ('distict', 'kozhikode')]), OrderedDict([('name', 'thanu'), ('roll', 103), ('distict', 'Thirsur')])]
    # json_data = JSONRenderer().render(serializer.data)
    # In the code you provided, you are using the JSONRenderer to render the data from the serializer into JSON format.
    # print(json_data)
    # b'[{"name":"anu","roll":101,"distict":"Malappuram"},{"name":"Aju","roll":102,"distict":"kozhikode"},{"name":"thanu","roll":103,"distict":"Thirsur"}]''
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)