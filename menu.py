import os
import random


db = {} # Simula base de datos

def registro():
  print("Registro de Usuario")
  nombre = input("Ingrese su nombre: ")
  email = input("Ingrese su email: ")
  telefono = input("Ingrese su teléfono: ")
  password = input("Ingrese su contraseña: ")
  print("Registro exitoso!")

  db["nombre"] = nombre
  db["email"] = email
  db["telefono"] = telefono
  db["password"] = password

def login():
  print("\nInicio de Sesión")
  opcion = input("Ingrese 1 para email o 2 para teléfono: ")
  
  if opcion == "1":
    email_login = input("Ingrese su email: ")
    if email_login != db["email"]:
      print("Email incorrecto")
      return False
    
  elif opcion == "2":  
    telefono_login = input("Ingrese su teléfono: ")
    if telefono_login != db["telefono"]:
      print("Teléfono incorrecto")
      return False

  password_login = input("Ingrese su contraseña: ")
  if password_login != db["password"]:
    print("Contraseña incorrecta")
    return False

  captcha = input("Ingrese el resultado de 2+2: ")
  if captcha != "4":
    print("Captcha incorrecto")
    return False

  print(f"Bienvenido {db['nombre']}!")
  return True

def menu1():
  print("Menú Principal")
  print("1. Registro")
  print("2. Login")
  print("3. Salir")
  
  opcion = input("Ingrese una opción: ")
  
  if opcion == "1":
    registro()
  elif opcion == "2":
    if login():
      menu2()
  elif opcion == "3":
    print("Saliendo...")
    exit()
  else:
    print("Opción inválida")

def menu2():
  print("Menú Secundario")
  print("1. App Compras")
  print("2. Juego")
  print("3. Volver")
  
  opcion = input("Ingrese una opción: ")
  
  if opcion == "1":
    compras()
  elif opcion == "2":
    juego()
  elif opcion == "3":
    menu1()
  else:
    print("Opción inválida")
  
def compras():

  print("App Compras")

  cupo_total = 500

  try:
    nombre = input("\nIngrese su nombre: ")  
    compra = float(input("\nIngrese el valor de la compra: "))
    cuotas = int(input("\nIngrese número de cuotas: "))

    if compra > cupo_total:
      print("\nCompra excede el cupo")
      return

    if cuotas <= 0:
      print("\nNúmero de cuotas inválido")
      return

    valor_cuota = compra / cuotas

    print(f"\nDetalle de pagos de {nombre}")

    for i in range(1, cuotas+1):
      print(f"\nCuota {i}: ${valor_cuota:.2f}")

  except ValueError:
    print("\nDebe ingresar valores numéricos válidos")
  
  compra_data = {
    "nombre": nombre, 
    "total": compra,
    "cuotas": cuotas
  }

  print("\nCompra registrada exitosamente!")

  input("\nPresione enter para volver al menú...")
  return menu2()

def juego():

  print("Juego")

  vidas = 5
  puntos = 0

  while vidas != 0:

    num = random.randint(0,9)

    if num == 0:
        vidas -= 1
        print(f"Te quedan {vidas} vidas")
        
    else:
        puntos += 1
        print(f"Has ganado {puntos} puntos")

  print("Juego terminado")  
  input("Presione enter para volver...")
  
  return menu2()

while True:
  os.system("cls") 
  menu1()