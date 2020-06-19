from django.core.exceptions import ValidationError


def validar_longitud_cedula (cedula):
    if len(cedula) != 13:
        raise ValidationError('Longitud de cedula incorrecta')

def validar_numeros_cedula (cedula):
    S = cedula
    P = S[0:3]
    V = S[4:11]
    Y = S[-1]

    for N in P+V+Y:
        if N not in['0','1','2','3','4','5','6','7','8','9']:
            raise ValidationError("Cedula contiene caracteres no numericos")

def validar_digito_verificador (cedula):
    validar_longitud_cedula(cedula)
    validar_numeros_cedula(cedula)

    suma = 0
    S = cedula
    P = S[0:3]
    V = S[4:11]
    Y = S[-1]
    O = P+V
    A = 0


    for I in range(len(O)):
        if I % 2 == 0:
            A = 1

        else:
            A = 2

        mult = A * int(O[I])

        if mult > 9:
            mult = mult - 10 + 1

        suma += mult

    digito = (10 - (suma % 10)) % 10

    if int(Y) != digito:
        raise ValidationError("Cedula no Valida")

def validar_vehiculo_rentado (vehiculo_id, ):
    from .models import Vehiculos
    vehiculo: Vehiculos = Vehiculos.objects.get(id=vehiculo_id)
    if not vehiculo.estado:
        raise ValidationError("Vehiculo ya esta rentado")