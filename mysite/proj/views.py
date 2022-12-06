from django.shortcuts import render
import ast
from django.http import JsonResponse
from . import models
from .models import Student

# Create your views here.
def proj_view(request):
    return render(request, 'proj/index.html')

def plswork(request):
    query = Student.objects.all()
    return render(request, 'proj/index.html', {"Student":query})

#def MyView(request):
 #   query = Student.objects.all()
  #  context = {
   #     'query': query,
   # }
    #return render(request, 'index.html', context)

#def index(request):
 #   from django.core import serializers
  #  data = serializers.serialize("python", Student.objects.all())
   # context = {
    #    'data': data,
    #}
    #return render(request, 'index.html', context)

#def getdata(request):
def getdata():
 #   if request.method == 'GET':
  #      data = request.body.decode('utf-8')
   #     data = ast.literal_eval(data)
     #   print(data)
        tmpstud = []
        allstud = list(models.Student.objects.all())

        if len(allstud) > 1:
            for stud in allstud:
                tmpstud.append([allstud.name, allstud.surname, allstud.group])
        else:
            tmpstud.append([allstud[0].name, allstud[0].surname, allstud[0].group])

  #      return JsonResponse({
   #        "st": "test",
    #        "all_stud": tmpstud
     #   })
