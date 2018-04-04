from suds.client import Client
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
print(Client('http://localhost:10002/calculadora?wsdl').service.Somar(a, b))
print(Client('http://localhost:10002/calculadora?wsdl').service.Substrair(a, b))
print(Client('http://localhost:10002/calculadora?wsdl').service.Multiplicar(a, b))
print(Client('http://localhost:10002/calculadora?wsdl').service.Dividir(a, b))


