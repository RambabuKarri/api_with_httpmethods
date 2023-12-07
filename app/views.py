from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def host(request):
    if request.method=='GET':
        PO=Employe.objects.all()
        JSO=EmployeMS(PO,many=True)
        return Response(JSO.data)
    elif request.method=="POST":
        JPO=EmployeMS(data=request.data)
        if JPO.is_valid():
            JPO.save()
            return Response({'message':'insertion is done'})
        return Response({'message':'invalid data'})


from app.serializers import ProductMSR
from rest_framework.views import APIView
from rest_framework.response import Response

class Boom(APIView):
    def get(self,request,pid):
        PD=Product.objects.all()
        JSD=ProductMSR(PD,many=True)
        return Response(JSD.data)
    
    def post(self,request,pid):
        JSD1=ProductMSR(data=request.data)
        #CPO=ProductMSR(JSD1)
        if JSD1.is_valid():
            JSD1.save()
            return Response({'Message':'insertion is done'})
        return Response({'Failed':'invalid data'})
        
    def put(self,request,pid):
        id=request.data['pid']
        PO=Product.objects.get(pid=id)
        UPO=ProductMSR(PO,data=request.data)
        if UPO.is_valid():
            UPO.save()
            return Response({'Message':'data is updated'})
        return Response({'Message':'data is not updated'})
    
    def patch(self,request,pid):
        id=request.data['pid']
        PO=Product.objects.get(pid=id)
        UPO=ProductMSR(PO,data=request.data,partial=True)
        if UPO.is_valid():
            UPO.save()
            return Response({'Message':'data is updated'})
        return Response({'Message':'data is not updated'})
    
    def delete(self,request,pid):
        PO=Product.objects.get(pid=pid)
        PO.delete()
        return Response({'Message':'deletion is done'})


        
        

