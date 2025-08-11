from django.shortcuts import render, get_object_or_404
from rest_framework import generics, mixins, filters
from .models import NajotTalim
from .serializers import NajotTalimSerializer, RegisterSerialzer
from .filters import NajotTalimFilter
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken



# Create your views here.


# class NajotTalimListView(mixins.ListModelMixin,
#                          mixins.CreateModelMixin,
#                          generics.GenericAPIView):
#     queryset = NajotTalim.objects.all()
#     serializer_class = NajotTalimSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_class = NajotTalimFilter
#     filterset_fields = ['Kurs_nomi', 'Kurs_narxi']
#     search_fields = ['Kurs_muddati', 'Kurs_haqida']
#     ordering_fields = ['Kurs_narxi', 'Kurs_nomi']
#     ordering = ['Kurs_narxi']

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    


# class NajotTalimDetailView(mixins.RetrieveModelMixin,
#                            mixins.UpdateModelMixin,
#                            mixins.DestroyModelMixin,
#                            generics.GenericAPIView):
#     queryset = NajotTalim.objects.all()
#     serializer_class = NajotTalimSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)
    

# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED


# class NajotTalimAPIView(APIView):
#     def get(self, request, pk=None):
#         queryset = NajotTalim.objects.all()

#         kurs_nomi = request.GET.get('Kurs_nomi')
#         if kurs_nomi:
#             queryset = queryset.filter(Kurs_nomi__icontains=kurs_nomi)

#         kurs_narxi = request.GET.get('Kurs_narxi')
#         if kurs_narxi:
#             queryset = queryset.filter(Kurs_narxi=kurs_narxi)

#         narx_gt = request.GET.get('Kurs_narxi__gt')
#         narx_lt = request.GET.get('Kurs_narxi__lt')

#         if narx_gt:
#             queryset = queryset.filter(Kurs_narxi__gt=narx_gt)
#         if narx_lt:
#             queryset = queryset.filter(Kurs_narxi__lt=narx_lt)

#         search = request.GET.get('search')
#         if search:
#             queryset = queryset.filter(
#                 Q(Kurs_nomi__icontains=search) | Q(Kurs_haqida__icontains=search)
#             )
#         ordering = request.GET.get('ordering')
#         if ordering:
#             queryset = queryset.order_by(ordering)
#         if pk:
#             obj = get_object_or_404(queryset, pk=pk)
#             serializer = NajotTalimSerializer(obj)
#         else:
#             serializer = NajotTalimSerializer(queryset, many=True)

#         return Response(serializer.data, status=status.HTTP_200_OK)

# class NajotTalimDetailAPIView(APIView):
#     def get_object(self, pk):
#         try:
#             return NajotTalim.objects.get(pk=pk)
#         except NajotTalim.DoesNotExist:
#             return None
        
#     def get(self, request, pk):
#         najot = self.get_object(pk)
#         if not najot:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serialzer = NajotTalimSerializer(najot)
#         return Response(serialzer.data)
    



#     def put(self, request, pk):
#         najot = self.get_object(pk)
#         if not najot:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serialzer = NajotTalimSerializer(najot, data=request.data)
#         if serialzer.is_valid():
#             serialzer.save()
#             return Response(serialzer.data)
#         return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     def delete(self, request, pk):
#         najot = self.get_object(pk)
#         if not najot:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         najot.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

    

#     def patch(self, request, pk):
#         najot_talim = get_object_or_404(NajotTalim, pk=pk)
#         serializer = NajotTalimSerializer(najot_talim, data=request.data, partial=True)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.generics import GenericAPIView
from django.db.models import Q

class NajotTalimAPIView(GenericAPIView):
    queryset = NajotTalim.objects.all()
    serializer_class = NajotTalimSerializer

    def get(self, request, pk=None):
        products = self.get_queryset()

        category = request.GET.get('category')
        price = request.GET.get('price')
        if category:
            products = products.filter(category=category)
        if price:
            products = products.filter(price=price)

        
        search = request.GET.get('search')
        if search:
            products = products.filter(
                Q(name__icontains=search) | Q(description__icontains=search)
            )

       
        ordering = request.GET.get('ordering')
        if ordering:
            products = products.order_by(ordering) 

   
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class NajotTalimDetail(GenericAPIView):

    queryset = NajotTalim.objects.all()
    serializer_class = NajotTalimSerializer


    def put(self, request, pk):
        obj = get_object_or_404(NajotTalim, pk=pk)
        serializer = self.get_serializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk=None):
        obj = get_object_or_404(NajotTalim, pk=pk)
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
    def delete(self, request, pk):
        obj = get_object_or_404(NajotTalim, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated


class RegisterView(APIView):
    def post(self, request):
        serialzer = RegisterSerialzer(data=request.data)
        if serialzer.is_valid():
            user = serialzer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Registered successfully',
                'refresh': str(refresh),
                'access': str(refresh.access_token),

            }, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'successful',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({"error": "Parol yoki Username notugri"}, status=status.HTTP_401_UNAUTHORIZED)


    

class Logout(APIView):

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logut buldi"}, status=status.HTTP_200_OK)
        except Exception:
            return Response({"error": "token mavjud emas"}, status=status.HTTP_400_BAD_REQUEST)


