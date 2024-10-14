from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer
from .models import Todo
from rest_framework.views import APIView
from rest_framework import viewsets


@api_view(['GET', 'POST', 'PATCH'])
def home(request):
    if request.method== 'GET':
        return Response({
        'status' :200, 
        'message' : 'Yes! Django rest framework is working!!!',
        'method_called' : 'you called GET method'
        
    })
    elif request.method== 'POST':
        return Response({
        'status' :200, 
        'message' : 'Yes! Django rest framework is working!!!',
        'method_called' : 'you called POST method'
        })
        
    elif request.method== 'PATCH':
        return Response({
        'status' :200, 
        'message' : 'Yes! Django rest framework is working!!!',
        'method_called' : 'you called PATCH method'
    })
        
    else:
        return Response({
        'status' :400, 
        'message' : 'Yes! Django rest framework is working!!!',
        'method_called' : 'you called INVALID method'
        })

@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data 
        serializer =  TodoSerializer(data = data)
        if serializer.is_valid():
            print(serializer.data)
            return Response({
                'status':True,
                'message':'Success Data',
                'data':serializer.data
            })
        
        return Response({
            'status':False,
            'message':'Invalid data',
            'data':serializer.errors
        })
    except Exception as e:
        return Response({
            'status':False,
             'message': 'An error occured' 
        })
        
@api_view(['GET'])
def get_todo(request):
    try:
        data=Todo.objects.all()
        serializer =  TodoSerializer(data,many= True)
        return Response({
            'status':200,
            'data':serializer.data
        })
    except Exception as e:
        return Response({
            'status':False,
            'message':'An error occured'
        })
@api_view(['PATCH'])
def patch_todo(request):
    try:
        data = request.data
        if not data.get('uid'):
            return Response({
                'status' : False,
                'message':'uid is required',
                'data':{}
            })
        
        obj = Todo.objects.get(uid = data.get('uid'))
        serializer = TodoSerializer(obj , data = data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':True,
                'message':'Success Data',
                'data':serializer.data
            })
        
        return Response({
            'status':False,
            'message':'error invalid data',
            'data':serializer.data
        })
    
    except Exception as e:
        return Response({
            'status':False,
            'message':'error ',
            'data':serializer.data
        })      

class TodoView(APIView):

    def get(self,request):
        return Response({
            'status':True,
            'message':'Todo list',
            'method-called':'You called a get method'
        })
    

    def post(self,request):
        return Response({
            'status':True,
            'message':'Todo list',
            'method-called':'You called post request'
        })
    

    def patch(self,request):
        return Response({
            'status':True,
            'message':'Todo list',
            'method-called':'You called Patch request'
        })
    

    def delete(self,request):
        return Response({
            'status':True,
            'message':'Todo List',
            'method-called':'You called delete request'
        })
        
class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()