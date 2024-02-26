from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre_marca = models.CharField(max_length=255,unique=True)

    def __str__(self) -> str:
            return self.nombre_marca
    
    class Meta:
                db_table = 'Marca'


class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=255,unique=True)

    def __str__(self):
                return self.nombre_categoria
        
    class Meta:
                 db_table = 'Categoria'

class Producto(models.Model):
    nombre = models.CharField(max_length=255,unique=True)
    precio = models.IntegerField()
    image = models.CharField(max_length=255)
    stock = models.IntegerField()
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE)

    def __str__(self):
                return self.nombre
        
    class Meta:
                db_table = 'Producto'

class Atributo(models.Model):
    nombre_atributo = models.CharField(max_length=255,unique=True)

    def __str__(self):
                return self.nombre_atributo
        
    class Meta:
                db_table = 'Atributo'

class ProductoAtributo(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    atributo = models.ForeignKey(Atributo, on_delete=models.CASCADE)
    valor = models.CharField(max_length=255)

    class Meta:
                db_table = 'Producto_Atributo'