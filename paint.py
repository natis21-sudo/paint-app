# -*- coding: utf-8 -*-
# ==========================================
# PROYECTO FINAL: BOCETO DE PAINT (ENTREGA 2)
# Nota de uso de IA: Este bloque de código lógico 
# fue estructurado con apoyo de Inteligencia Artificial 
# cumpliendo la norma del curso, para simular las 
# funciones base del Paint (lápiz, borrador, colores y CSV)[cite: 1, 2].
# ==========================================

def mostrar_menu():
    print("\n" + "="*45)
    print("   BOCETO DE PAINT - MENÚ PRINCIPAL (FASE 2)")
    print("="*45)
    print("1. Activar Lápiz")
    print("2. Activar Borrador")
    print("3. Seleccionar Color (8 opciones disponibles)")
    print("4. Guardar/Abrir dibujo en archivo CSV")
    print("5. Salir del programa")
    print("="*45)

def main():
    print("¡Bienvenido al sistema base de nuestro Paint en Python!")
    ejecutando = True
    
    # Bucle while para mantener el programa abierto hasta que el usuario decida salir
    while ejecutando:
        mostrar_menu()
        opcion = input(">> Digite el número de la opción que desea probar: ")
        
        print("\n" + "-"*35)
        if opcion == "1":
            print("[ACCIÓN] Herramienta Lápiz activada.")
        elif opcion == "2":
            print("[ACCIÓN] Herramienta Borrador activada.")
        elif opcion == "3":
            print("[ACCIÓN] Paleta de 8 colores seleccionada (Negro, Rojo, Azul, Verde, Amarillo, Anaranjado, Morado, Café).")
        elif opcion == "4":
            print("[ACCIÓN] Estado del lienzo exportado/importado exitosamente en archivo CSV.")
        elif opcion == "5":
            print("Cerrando el programa de Paint... ¡Hasta pronto!")
            ejecutando = False  # Cambia a False para romper el bucle y terminar
        else:
            print("[ERROR] Opción no válida. Elija un número del 1 al 5.")
        print("-"*35)

if __name__ == "__main__":
    main()

