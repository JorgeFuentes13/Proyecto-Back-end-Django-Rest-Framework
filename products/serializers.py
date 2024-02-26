from rest_framework import serializers
from .models import Categoria, Producto, Atributo, ProductoAtributo, Marca

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Marca
        fields = '__all__'

class AtributoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Atributo
        fields = '__all__'

class ProductoAtributoSerializer(serializers.ModelSerializer):
    nombre_atributo = serializers.CharField(source='atributo.nombre_atributo', read_only=True)

    class Meta:
        model = ProductoAtributo
        fields = ['nombre_atributo','valor','producto','atributo']

    def validate(self, data):
        producto = data['producto']
        atributo = data['atributo']
        valor = data['valor']

        # Verificar si ya existe un ProductoAtributo con el mismo producto y atributo.
        existente = ProductoAtributo.objects.filter(producto=producto, atributo=atributo).exclude(valor=valor).exists()

        if existente and self.instance is None:
            # Si existente y no se está actualizando (creando nuevo ProductoAtributo), lanza un error.
            raise serializers.ValidationError('Ya existe un valor para este atributo en el producto.')

        return data
    
class ProductoSerializer(serializers.ModelSerializer):
    # Comentario: Este serializer define cómo se serializan y deserializan los objetos Producto.
    
    #categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), allow_null=True)

    # Comentario: El siguiente campo representa la relación con los atributos del producto.
    # Se utiliza el serializer ProductoAtributoSerializer para representar la información de los atributos.
    atributos = ProductoAtributoSerializer(source='productoatributo_set', many=True, read_only=True)


    # Comentario: Este campo representa el nombre de la categoría del producto.
    # Se utiliza para mostrar el nombre de la categoría en lugar del ID en la representación JSON.
    nombre_categoria = serializers.CharField(source='categoria.nombre_categoria', read_only=True)

    # Comentario: Este campo representa el nombre de la marca del producto.
    # Se utiliza para mostrar el nombre de la marca en lugar del ID en la representación JSON.
    nombre_marca = serializers.CharField(source = 'marca.nombre_marca',read_only=True)

    
    class Meta:
        # Comentario: La clase Meta define metadatos para el serializer.
        model = Producto  # Se especifica el modelo que este serializer está manejando.
        fields = ['id', 'nombre', 'precio', 'image', 'stock', 'atributos', 'activo','categoria','nombre_categoria','marca','nombre_marca']
        # Comentario: Se especifican los campos del modelo que se incluirán en la serialización.
        # En este caso, se incluyen el ID, nombre, descripción, precio, imagen, stock, atributos, categoría y nombre de categoría.
