from django.shortcuts import render

# Create your views here.


from rest_framework.decorators import  api_view
from rest_framework.response import Response
from .serializers import WorkerSerializers
from .models import Worker

@api_view(['GET','POST'])
def test_get(request):
    Worker_info = Worker.objects.all()
    serializer = WorkerSerializers(Worker_info, many=True)

    return Response({'status':200,'data':serializer.data})



@api_view(['GET','POST'])
def test_post(request):
    data = request.data
    serializer=WorkerSerializers(data=request.data)
    if not serializer.is_valid():
        return  Response({'status':403, 'Xatolik':serializer.errors, 'message':'Xatolik yuz berdi'})
    serializer.save()
    return Response({'status':200, 'data':serializer.data, 'message':'Malumot qabul qilindi'})


@api_view(['PUT','GET'])
def test_put(request, id):
    Worker_info = Worker.objects.get(id=id)
    try:
        serializer = WorkerSerializers(Worker_info,data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'status':403, 'message':'Xatolik yuz berdi'})
        serializer.save()
        return Response({'status':200,'data':serializer.data, 'message':'Malumot yangilandi'})
    except Exception as e:
        print(e)
        return Response({'status':403, 'message':'Xatolik yuz berdi'})

@api_view(['DELETE'])
def test_delete(request,id):
    Worker_info = Worker.objects.get(id=id)
    Worker_info.delete()
    return Response({'status':200, 'message':"Ma'lumot o'chirildi"})
