from django.http import HttpResponse
from preguntasyrespuestas.models import Pregunta

def index(request):
    preguntas = Pregunta.objects.all()
    respuesta_string = "<h1>Preguntas <br/></h1>"
    respuesta_string += '<br/>'.join(["id:%s, asunto:%s"%
    (p.id,p.asunto) for p in preguntas])
    return HttpResponse(respuesta_string)

# Create your views here.
