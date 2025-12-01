import Operaciones

def iniciar():
    print("--- Calculadora Simple ---")
    print("1. Sumar")
    print("2. Restar")
    
    opcion = input("Elige una opción (1-2): ")
    
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        if opcion == '1':
            resultado = Operaciones.sumar(num1, num2)
            print(f"El resultado es: {resultado}")
        elif opcion == '2':
            resultado = Operaciones.restar(num1, num2)
            print(f"El resultado es: {resultado}")
        else:
            print("Opción no válida")
            
    except ValueError:
        print("Error: Por favor ingresa solo números.")

if __name__ == "__main__":
    iniciar()