from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request): #primera vita
    nombre = "Miguel"

    doc_externo = open("/home/miguel/PycharmProjects/ApacheLunch/ApacheLaunch/plantillas/miplantilla.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"nombre_persona":nombre})

    documento = plt.render(ctx)

    return HttpResponse(documento)

def despedida(request): #despedida
    return HttpResponse("BaiBai")

def dameFecha(request):
    fecha_actual = datetime.datetime.now()

    documento = """<html>
    <body>
    <h1>
        Fecha y hora actual %s
    </h1>
    </body>
    </html> """ % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, edad, anho):

    #edadActual = 18
    periodo = anho - 2020
    edadFutura = edad + periodo

    documento="<html><body><h2>En el año %s tendras %s años</html></body></h2>" %(anho, edadFutura)

    return HttpResponse(documento)
