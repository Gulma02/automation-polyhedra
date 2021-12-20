import math
def recuperar_lados_triangulo(largo_arista: float):
    media_arista = (largo_arista*0.5)
    hipotenusa = media_arista / math.sin(1.0472)
    opuesto = hipotenusa * math.sin(0.523599)

    return [media_arista, opuesto, hipotenusa]

def calcular_altura(opuesto: float, hipotenusa: float):
    return opuesto + hipotenusa

def calcular_superficie_cara(altura: float, base: float):
    sup = base * altura
    return sup/2

def calcular_superficie_total(sup_cara: float, total_lados: float):
    return sup_cara * total_lados

def calcular_lado_pc(lado_region_fundamental: float, lado_menor: float):
    lado_region_fundamental = recuperar_valor_cuadrado(lado_region_fundamental)
    lado_menor = recuperar_valor_cuadrado(lado_menor)
    print(lado_menor, lado_region_fundamental)
    return math.sqrt(lado_region_fundamental - lado_menor)

def recuperar_valor_cuadrado(valor_a_potenciar):
    return valor_a_potenciar * valor_a_potenciar

def calcular_lado_restante(lado_restante: float, lado_pc: float):
    lado_restante = recuperar_valor_cuadrado(lado_restante)
    lado_pc = recuperar_valor_cuadrado(lado_pc)

    return math.sqrt(lado_pc + lado_restante)

arista = float(input("Ingrese el valor de la arista: "))
que_lado = input("El lado de la region fundamental es PA o PV? ").upper()
lado_region_fundamental = float(input("Ingrese el valor del lado dado: "))
cuantas_caras = int(input('Ingrese la cantidad de caras del poliedro: '))

lados_triangulo = recuperar_lados_triangulo(arista)
print("\nLos valores de los lados son:")
print(lados_triangulo)

altura = calcular_altura(lados_triangulo[1], lados_triangulo[2])
print("\nLa altura del triangulo es:")
print(altura)

superficie_cara = calcular_superficie_cara(altura, arista)
print("\nLa superficie de la cara es:")
print(superficie_cara)

print("\nLa superficie total del poliedro es:")
print(calcular_superficie_total(superficie_cara, cuantas_caras))

if que_lado == "PA":
    lado = lados_triangulo[1]
    lado_restante = lados_triangulo[2]
elif que_lado == "PV":
    lado = lados_triangulo[2]
    lado_restante = lados_triangulo[1]

lado_pc = calcular_lado_pc(lado_region_fundamental, lado)

print("\nEl lado pc vale: ")
print(lado_pc)

print("\nEl lado restante vale: ")
print(calcular_lado_restante(lado_restante, lado_pc))
