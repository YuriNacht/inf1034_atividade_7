def calculator():
    continuar = "não"
    while True:
        if  continuar == 'não':
            
            numero1= float(input("Primeiro número: "))
            operador = input("Operação (+, -, *, /): ")
            numero2= float(input("Segundo número: "))
        else:
            print("Vamos continuar a calcular!")
            numeronovo=float(input("Qual o proximo numero?"))
            operacaonova=input("Qual a proxima operação?")
            operador=operacaonova
            numero1=resultado
            numero2=numeronovo
        
        if operador == '+':
            resultado = numero1 + numero2
            print (f'{resultado}')   
        elif operador == '-':
            resultado = numero1 - numero2
        
            print (f'{resultado}')
        elif operador == '*':
            resultado = numero1 * numero2
        
            print (f'{resultado}')    
        elif operador == '/' and numero2!=0:
            resultado = numero1 / numero2
            
            print (f'{resultado}')    
        else:   
            print("Erro: Divisão por zero não existe.")
        
        continuar=input("Quer continuar a calcular? (sim/não): ")    

calculator()

