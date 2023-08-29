import datetime
from django.http import HttpResponse

#ahora aca agrego mis propias vistas
def hola(request):
    return HttpResponse("<h1>Hola bienvenidos al curso Django</h1>")

def chaoo(request):
    return HttpResponse('Hasta luego...')

def saludo2(request):
    documet = """
                <html>
                    <body>
                        <h1>Hola a todos nuevamente</h1>
                    </body>
                </html>"""
    return HttpResponse(documet)

def verhora(request):
    fecha_actual = datetime.datetime.now()
    documet = """
                <html>
                    <body>
                        <h2>La fecha y hora actual es: %s</h2>
                    </body>
                </html>""" % fecha_actual

    return HttpResponse(documet)

def calculaedad(request, agno, edad):
    #edad=18
    periodo = agno - 2023
    edadfuturo = edad + periodo

    documet = """
                <html>
                    <body>
                        <h2>En el año %s tendras %s años</h2>
                    </body>
                </html>""" % (agno, edadfuturo)
    return HttpResponse(documet)





