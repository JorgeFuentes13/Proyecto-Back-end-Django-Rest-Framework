from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Categoria, Producto, Atributo, ProductoAtributo, Marca
from .serializers import CategoriaSerializer, ProductoSerializer, AtributoSerializer, ProductoAtributoSerializer, MarcaSerializer
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend


from rest_framework.response import Response

#filtros
from rest_framework import filters

#pagination
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination


from rest_framework.generics import CreateAPIView

# Create your views here.

# CREATE ,UPDATE, DELETE AND LISTAR
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoriaSerializer

class ProductoAtributoViewSet(viewsets.ModelViewSet):
    queryset = ProductoAtributo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoAtributoSerializer


class AtributoViewSet(viewsets.ModelViewSet):
    queryset = Atributo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AtributoSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MarcaSerializer


#Producto
#GET
class ListProduct(generics.ListAPIView):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer


#GET ID
class ProductDetail(generics.RetrieveAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

#POST
class ProductCreate(generics.CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

#UPDATE
class ProductUpdate(generics.RetrieveUpdateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

#Lista para buscar
class ProductsSearchFilter(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['nombre','categoria__nombre_categoria', 'marca__nombre_marca']
    ordering_fields = ['nombre', 'precio']
    ordering = ['-precio']
    pagination_class = LimitOffsetPagination  # Cambio a LimitOffsetPagination


#Lista filtrar productos
class FiltringProducts(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categoria__nombre_categoria','marca__nombre_marca']


#Lista Products Mixin
class ListaProductosView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
