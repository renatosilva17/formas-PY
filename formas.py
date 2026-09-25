def circulo():
    raio = float(input("qual valor do raio: "))
    resultado = 3.14 * (raio * raio)
    print (f"a area do circulo é {resultado}")

def triangulo():
    base1 = float(input("qual valor da base: "))
    altura = float(input("qual valor da altura: "))
    resultado = (base1 * altura) /2
    print (f"a area do triangulo é {resultado}")

def quadrado():
    lado = float(input("qual lado do quadrado: "))
    resultado = lado * lado
    print(f"a area do quadrado é {resultado}")

def retangulo():
    base = float(input("qual é a base:  "))
    altura = float(input("qual a altura: "))
    resultado = base * altura
    print(f"a area do retangulo é {resultado}")

def paralelogramo():
    base = float(input("qual a base: "))
    altura = float(input("qual a altura"))
    resultado = (f"a area do paralelogramo é {resultado}")

def losangulo():
    dmaior = float(input("qual a diagonal maior: "))
    dmenor = float(input("qual a diagonal menor: "))
    resultado = (dmaior * dmenor) /2
    print(f"a area do losangulo é {resultado}")

def trapezio():
    baseMaior = float(input("qual a base maior: "))
    baseMenor = float(input("qual a base menor: "))
    altura = float(input("qual a altura: "))
    resultado = (baseMaior + baseMenor * altura) /2
    print(f"a area do trapézio é {resultado}")

while True:
    print("Calculadora de areas")
    print("1 - circulo")
    print("2 - triangulo")
    print("3 - quadrado")
    print("4 - retangulo")
    print("5 - paralelogramo")
    print("6 - losangulo")
    print("7 - trapezio")
    print("0 - sair do programa")

    opcao = input("digite um numero")
    
    if opcao == "1":
     circulo()
    elif opcao == "2":
     triangulo()
    elif opcao == "3":
     quadrado()
    elif opcao == "4":
       retangulo()
    elif opcao == "5":
       paralelogramo()
    elif opcao == "6":
       losangulo()
    elif opcao == "7":
       trapezio()
    elif opcao == "0":
       print("saindo do sistema")
       break