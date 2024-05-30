
from django.shortcuts import render
from django.http import FileResponse
from .models import Anuncio
from datetime import date
from django.shortcuts import redirect
# Create your views here
def bdsave(request):
    filepath = './db.sqlite3'
    filename = 'db.sqlite3' # Este nombre será lo que vea el usuario cuando se descargue
    response = FileResponse(filepath, as_attachment=True)

    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response
    pass

def InsertarAnuncio(request):
    titulo = request.POST["title"]
    price = request.POST["price"]
    contact = request.POST["contact"]
    description = request.POST["description"]
    Imagn = request.FILES["image"]
    nuevo_anuncion =  Anuncio(titulo=titulo,precio=price,telefono=contact,descripcion=description,fecha=date.today(),Image=Imagn)
    nuevo_anuncion.save()
    
    return redirect("/")

def CreateView(request):
    return render(request,"crearanuncion.html")

def Home(request):
    renderizar = ""
    try:
        if(request.GET["hint"] != None):
        
          datos = Anuncio.objects.filter(titulo__icontains=request.GET["hint"])    
        
          renderizar = render(request,"index.html",{"data":datos})
          return renderizar
    
    except:
          print()   
  
        
    datos = Anuncio.objects.all()
        
    renderizar = render(request,"index.html",{"data":datos})

    return renderizar

def Search(reques):

    Anunciocogido= Anuncio.objects.filter(id=reques.GET["id"]) 
    print(Anunciocogido)
    return render(reques,"mostrarvista.html",{"data":Anunciocogido})