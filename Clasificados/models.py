from django.db import models
import json
# Create your models here.
class Anuncio(models.Model):
    id = models.IntegerField(primary_key=True)
    Image =models.ImageField(upload_to="./static")
    descripcion = models.CharField(max_length=256)
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()
    telefono = models.IntegerField()
    precio = models.IntegerField()
    
    def __str__(self):
        
        
        return str(json.dumps({"id":self.id,
        "Image":str(self.Image.url),
        "descripcion":self.descripcion,
        "titulo":self.titulo,
        "fecha":str(self.fecha),
        "contacto":str(self.telefono),
        "precio":str(self.precio)}))
        
        pass
