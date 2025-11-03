#1

import json


personas_dict = {
    "jadiazcoronado": {
        "nombres": "Juan Antonio",
        "apellidos": "Díaz Coronado",
        "edad": 19,
        "colombiano": True,
        "deportes": ["Fútbol", "Ajedrez", "Gimnasia"]
    },
    "mprada": {
        "nombres": "María Fernanda",
        "apellidos": "Prada Gómez",
        "edad": 22,
        "colombiano": True,
        "deportes": ["Natación", "Ajedrez"]
    },
    "rcortesp": {
        "nombres": "Ricardo",
        "apellidos": "Cortés Pérez",
        "edad": 30,
        "colombiano": False,
        "deportes": ["Ciclismo", "Fútbol"]
    },
    "dmlunasol": {
        "nombres": "Dorotea Maritza",
        "apellidos": "Luna Sol",
        "edad": 25,
        "colombiano": False,
        "deportes": ["Baloncesto", "Ajedrez", "Gimnasia"]
    },
    "ljgarcia": {
        "nombres": "Luis Javier",
        "apellidos": "García Torres",
        "edad": 28,
        "colombiano": True,
        "deportes": ["Tenis", "Natación"]
    }
}


print("Ahora ingresará 5 nuevas personas:\n")

for i in range(5):
    print(f"--- Persona nueva {i+1} ---")
    usuario = input("Usuario (sin espacios): ").strip()
    nombres = input("Nombres: ").strip()
    apellidos = input("Apellidos: ").strip()

    
    while True:
        try:
            edad = int(input("Edad: "))
            break
        except ValueError:
            print("Ingrese una edad válida (entero).")

    
    while True:
        es_colombiano = input("¿Es colombiano? (S/N): ").strip().upper()
        if es_colombiano in ["S", "N"]:
            colombiano = True if es_colombiano == "S" else False
            break
        else:
            print("Ingrese solo 'S' o 'N'.")

    
    deportes_input = input("Deportes (separe con comas): ").strip()
    deportes = [d.strip() for d in deportes_input.split(",") if d.strip()]

    
    personas_dict[usuario] = {
        "nombres": nombres,
        "apellidos": apellidos,
        "edad": edad,
        "colombiano": colombiano,
        "deportes": deportes
    }
    print()


with open("personas.json", "w", encoding="utf-8") as archivo:
    json.dump(personas_dict, archivo, ensure_ascii=False, indent=4)

print("\n Archivo 'personas.json' creado correctamente con todos los datos.\n")


with open("personas.json", "r", encoding="utf-8") as archivo:
    personas = json.load(archivo)

deporte_buscado = input("Ingrese un deporte para buscar: ").strip().lower()

print(f"\nPersonas que practican {deporte_buscado.capitalize()}:")
encontradas = False

for usuario, datos in personas.items():
    if deporte_buscado in [d.lower() for d in datos["deportes"]]:
        print(f"  - {datos['nombres']} {datos['apellidos']}")
        encontradas = True

if not encontradas:
    print("  Ninguna persona practica ese deporte.")






#2

import json


with open("personas.json", "r", encoding="utf-8") as archivo:
    personas = json.load(archivo)


while True:
    try:
        edad_min = int(input("Ingrese la edad mínima: "))
        edad_max = int(input("Ingrese la edad máxima: "))
        if edad_min > edad_max:
            print(" La edad mínima no puede ser mayor que la máxima.")
        else:
            break
    except ValueError:
        print(" Ingrese valores numéricos válidos.")


print(f"\nPersonas con edades entre {edad_min} y {edad_max} años:")
encontradas = False

for usuario, datos in personas.items():
    if edad_min <= datos["edad"] <= edad_max:
        print(f"  - {datos['nombres']} {datos['apellidos']} ({datos['edad']} años)")
        encontradas = True

if not encontradas:
    print("  No hay personas en ese rango de edad.")



#3
import json


with open("personas.json", "r", encoding="utf-8") as archivo:
    personas = json.load(archivo)

deportes_dict = {}

for usuario, datos in personas.items():
    for deporte in datos["deportes"]:
        deporte_clean = deporte.strip()  
        if deporte_clean not in deportes_dict:
            deportes_dict[deporte_clean] = []
        deportes_dict[deporte_clean].append(usuario)


with open("deportes.json", "w", encoding="utf-8") as archivo:
    json.dump(deportes_dict, archivo, ensure_ascii=False, indent=4)

print("Archivo 'deportes.json' creado correctamente.")


#4

import json


with open("personas.json", "r", encoding="utf-8") as f1:
    datos1 = json.load(f1)

with open("deportes.json", "r", encoding="utf-8") as f2:
    datos2 = json.load(f2)


coincidencias = {}


for clave1, valor1 in datos1.items():
    if clave1 in datos2:  
        valor2 = datos2[clave1]
        if valor1 == valor2:  
            coincidencias[clave1] = valor1


with open("coincidencias.json", "w", encoding="utf-8") as salida:
    json.dump(coincidencias, salida, ensure_ascii=False, indent=4)

print("Archivo 'coincidencias.json' creado con las coincidencias exactas entre los dos archivos.")





5# 
import json


with open("notas.json", "r", encoding="utf-8") as archivo:
    notas_estudiantes = json.load(archivo)


print("Códigos de estudiantes disponibles:")
for codigo in notas_estudiantes.keys():
    print(" -", codigo)

codigo = input("\nIngrese el código del estudiante para calcular su promedio: ").strip()

if codigo in notas_estudiantes:
    notas = notas_estudiantes[codigo]

    
    if len(notas) > 0:
        promedio = sum(notas) / len(notas)
    else:
        promedio = 0

    
    resultado = {codigo: {"promedio": round(promedio, 2)}}

    
    with open("promedio_estudiante.json", "w", encoding="utf-8") as salida:
        json.dump(resultado, salida, ensure_ascii=False, indent=4)

    print(f"\nArchivo 'promedio_estudiante.json' creado correctamente con el promedio de {codigo}.")
else:
    print("\n El código ingresado no existe en el archivo.")


#6 

import json


with open("encriptado.json", "r", encoding="utf-8") as archivo:
    cadenas = json.load(archivo)


reemplazos = {
    "$": "a",
    "#": "e",
    "*": "i",
    "¬": "o",
    "+": "u"
}


desencriptado = {}

for clave, texto in cadenas.items():
    nuevo_texto = texto
    
    for simbolo, vocal in reemplazos.items():
        nuevo_texto = nuevo_texto.replace(simbolo, vocal)
    desencriptado[clave] = nuevo_texto


with open("desencriptado.json", "w", encoding="utf-8") as salida:
    json.dump(desencriptado, salida, ensure_ascii=False, indent=4)

print(" Archivo 'desencriptado.json' creado correctamente.")
