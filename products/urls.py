from django.urls import path, include
from rest_framework import routers
from .views import ListProduct, ProductoViewSet, CategoriaViewSet, AtributoViewSet, ProductoAtributoViewSet,MarcaViewSet,ProductDetail
from .views import ListaProductosView,ProductsSearchFilter,ProductCreate,ProductUpdate,FiltringProducts


router = routers.DefaultRouter()

router.register('producto', ProductoViewSet)
router.register('categoria', CategoriaViewSet)
router.register('atributo', AtributoViewSet)
router.register('producto-atributo', ProductoAtributoViewSet)
router.register('marca', MarcaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('list-product/', ListProduct.as_view(), name='list-product'),
    path('producto-detail/<int:pk>/', ProductDetail.as_view(), name='producto-detail'), 
    path('products-filtros', ProductsSearchFilter.as_view(), name='producto-search'),
    path('product-create',ProductCreate.as_view(),name='producto-create'),
    path('product-update/<int:pk>/',ProductUpdate.as_view(),name='producto-update'),
    path('products-filtrosv2', FiltringProducts.as_view(), name='producto-search'),

    path('productos-mixin/', ListaProductosView.as_view(), name='lista_productos') #No sé hace.
]






