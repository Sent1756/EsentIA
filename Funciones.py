'''
# Funciones
# Función I: Opciones
def Options():
    while NotaBase == "Options":
        # Mostrar Funciones Disponibles
        print("Ingresar: Introduzca una Nota Base")
        print("Mantener: Mantiene la Nota dando la oportunidad de cambio al Intervalo")
        print("Cambiar: Cambia de Mantener la Nota a Mantener el Intervalo")
        print("Mostrar: Muestra todas las Notas que puedes Ingresar")
        print("Salir: Te permite Salir del Modo")
        continue
# Función II: Mantener
def Mantener():
    input("¿Mantener? Nota (N)/Intervalo (I): ").lower()
    # Si Mantiene la Nota
    if Mantener == "n":
        CalculadoraInterválica(TipoIntervalo = input("Tipo de Intervalo: "))
    # Si Mantiene el Intervalo
    elif Mantener == "i":
        CalculadoraInterválica(NotaBase = input("Nota Base: "))
# Función IV: Mostrar
def Mostrar():
    while TipoIntervalo == "Mostrar":
        IntervalosDisponibles = list(Intervalos[CalculadoraInterválica(TipoIntervalo)].keys())
        print(IntervalosDisponibles)
        TipoIntervalo = input("Tipo de Intervalo: ")
# Función IV: Cambiar
def Cambiar():
    Cambiar = input("¿Cambiar? (Sí/No): ").lower()
    if Cambiar == "si":
        if Mantener == "n":
            Mantener = "i"
        if Mantener == "i":
            Mantener = "n"
# SubFunción IV.I: Anti-Cambio
def AntiCambio():
    while Cambiar == "no":
        # Anticambio Manteniendo la Nota
        if Mantener == "n":
            TipoIntervalo = input("Tipo de Intervalo: ")
            if TipoIntervalo == "Cambiar":
                Cambiar = input("¿Cambiar? (Sí/No): ").lower()
                if Cambiar == "si":
                    break
# Función V: Salir
def Salir():
    while True:
        Salir = input("Desea Salir del Modo Intervalos? (Sí/No): ").lower()
        if Salir == "si":
            break
        elif Salir == "no" or Salir is None:
            continue
'''