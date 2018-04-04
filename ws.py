from suds.client import Client
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
op = int(input("Escolha a operação - 1) Soma 2) Subtração"))

if op == 1:
    print(Client('http://localhost:10002/calculadora?wsdl').service.Somar(a, b))

elif op == 2:
    print(Client('http://localhost:10002/calculadora?wsdl').service.Substrair(a, b))

elif op == 3:
    print(Client('http://localhost:10002/calculadora?wsdl').service.Multiplicar(a, b))

elif op == 4:
    print(Client('http://localhost:10002/calculadora?wsdl').service.Dividir(a, b))

else:
    result = print("Operação inválida!")

print(result)

