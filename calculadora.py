#registro de datos
nombre = input ('Hola ¿Cómo te llamas?')
print ('Mucho gusto ' +nombre)


# Calculadora de IMC
# IMC = Peso / (Altura x Altura)
# < 19: delgadez
# entre 20 y 25: normal
# entre 26 y 30: sobrepeso
# > de 30: obesidad

def calcularIMC(peso, alturaEnMetros):
    imc = peso / (alturaEnMetros * alturaEnMetros)
    return imc

def pedirElIMC():
    peso = float(input('Ingrese su peso en kg'))
    alturaEnCm = int(input('Ingrese su altura en cm'))
    alturaEnMetros = alturaEnCm /100
    imc = calcularIMC(peso, alturaEnMetros)

    print('Su IMC es de ' +str(imc))

    if imc < 20:
        print('Tu estado es de delgadez, necesitas ver a tu nutricionista' +nombre)
    if imc >= 20 and imc < 26:
        print('Felicidades, tienes un peso normal,' +nombre)
    if imc >= 26 and imc < 30:
        print('Preocupate!, estas en un estado de Sobrepeso,' +nombre)
    if imc >= 30:
        print('Empecemos la dieta, ya que tu estado es de Obesidad,' +nombre )

print('Calcular el peso IMC')
pedirElIMC()
