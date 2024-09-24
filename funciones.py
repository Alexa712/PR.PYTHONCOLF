def calculadora (variable1, variable2, operacion):
    variable1 = int(variable1)
    variable2 = int(variable2)
    if(variable1 <0 or variable2 <0):
        print ('no puedes ingresar valores negativos')
    else:
        if(operacion == '+'):
            resultado = variable1 + variable2
            print (resultado)
        elif (operacion == '-'):
            resultado = variable1 - variable2
            print (resultado)
        elif (operacion == '*'):
            resultado = variable1 * variable2
            print (resultado)
        elif (operacion == '/'):
            if(variable2 == 0):
                print ('no se puede dividir por cero')
            else:
                resultado = variable1 // variable2
                print (resultado)
        else:
            print ('Has ingresado un parametro incorrecto')

num1 = input('Por favor digite el numero a operar: ')
num2 = input('Por favor digite el segundo numero a operar: ')
#ope = input('Por favor digite la operacion a realizar permitividad (+ - x /): ')

print ('El resultado de la operación es: ') 
calculadora (num1,num2,'+') 
calculadora (num1,num2,'-')
calculadora (num1,num2,'*')
calculadora (num1,num2,'/')