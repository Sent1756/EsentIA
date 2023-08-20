# Importar Datos
from BaseDatos import Intervalos, CalculadoraInterválica, GeneradorAcordes, Acordes, GeneradorEscalas
# Base de Datos
Intervalos
# Esentia
def EsentIA():
    # Presentación y Selección de Modos de la IA
    print("¡Bienvenido a E-Sent-I.A!, ¿En qué puedo ayudarte?")
    # Inteligencia Artificial
    while True:
        # Introducción a los Modos
        Modo = input("Escribe [Modos] para ver los Modos de la IA o Seleccione el Modo: ")
        # Modos
        if Modo == "Modos":
            # Intervalos
            print("Intervalos (I)")
            # Acordes
            print("Acordes (II)")
            # Escalas
            print("Escalas y Modos (III)")
            # Selección de Modo
            Modo = input("Seleccione el Modo: ")
        # Modo I: Intervalos
        elif Modo == "I":
            # Opciones
            print("Escribe [Mostrar] para ver las diferentes Opciones o [Salir] para cambiar de Modo")
            # Calculadora Interválica
            while True:
                # Entrada I: Nota Base
                NotaBase = input("Nota Base: ")
                # Mostrar Nota Base
                while NotaBase == "Mostrar":
                    Disponibles = list(Intervalos.keys())
                    print(Disponibles)
                    NotaBase = input("Nota Base: ")
                    if NotaBase is Disponibles:
                        break
                    elif NotaBase is not Disponibles:
                        continue
                # Salir Nota Base
                if NotaBase == "Salir":
                    Salir = input("Desea Salir del Modo Intervalos? (Sí/No): ").lower()
                    if Salir == "si":
                        break
                    elif Salir == "no" or Salir is None:
                        continue
                # Entrada II: Tipo de Intervalo
                TipoIntervalo = input("Tipo de Intervalo: ")
                # Mostrar Tipo de Intervalo
                while TipoIntervalo == "Mostrar":
                    Disponibles = list(Intervalos[NotaBase].keys())
                    print(Disponibles)
                    TipoIntervalo = input("Tipo de Intervalo: ")
                    if TipoIntervalo is list(Intervalos[NotaBase].keys()):
                        break
                    elif TipoIntervalo is not list(Intervalos[NotaBase].keys()):
                        continue
                # Salir Tipo de Intervalo
                if TipoIntervalo == "Salir":
                    Salir = input("Desea Salir del Modo Intervalos? (Sí/No): ").lower()
                    if Salir == "si":
                        break
                    elif Salir == "no" or Salir is None:
                        continue
                # Resultado
                print(f"La {TipoIntervalo} de {NotaBase} es: {CalculadoraInterválica(NotaBase, TipoIntervalo)}")
        # Modo II: Acordes
        elif Modo == "II":
            # Opciones
            print("Escribe [Mostrar] para ver las diferentes Opciones o [Salir] para cambiar de Modo")
            while True:
                # Entrada I: Nota Base
                NotaBase = input("Nota Base: ")
                # Mostrar Nota Base
                while NotaBase == "Mostrar":
                    Disponibles = list(Intervalos.keys())
                    print(Disponibles)
                    NotaBase = input("Nota Base: ")
                    if NotaBase is list(Intervalos.keys()):
                        break
                    elif NotaBase is not list(Intervalos.keys()):
                        continue
                # Salir Nota Base
                if NotaBase == "Salir":
                    Salir = input("Desea Salir del Modo Intervalos? (Sí/No): ").lower()
                    if Salir == "si":
                        break
                    elif Salir == "no" or Salir is None:
                        continue
                # Entrada II: Tipo de Acorde
                TipoAcorde = input("Tipo de Acorde: ")
                # Mostrar Tipo de Acorde
                while TipoAcorde == "Mostrar":
                    Disponibles = list(Acordes[TipoAcorde].keys())
                    print(Disponibles)
                    TipoAcorde = input("Tipo de Acorde: ")
                    if TipoAcorde is Disponibles:
                        break
                    elif TipoAcorde is not Disponibles:
                        continue
                # Salir Tipo de Acorde
                if TipoAcorde == "Salir":
                    Salir = input("Desea Salir del Modo Intervalos? (Sí/No): ").lower()
                    if Salir == "si":
                        break
                    elif Salir == "no" or Salir is None:
                        continue
                print(f"{NotaBase}{TipoAcorde} está formado por: {GeneradorAcordes(NotaBase, TipoAcorde)}")
        # Modo III: Escalas
        elif Modo == "III":
            while True:
                NotaBase = input("Nota Base: ")
                Escala = input("Escala: ")
                Grado = input("Grado de la Escala: ")
                print(f"{NotaBase} {Grado} está formada por: {GeneradorEscalas(NotaBase, Escala, Grado)}")
# Llamada a la IA
EsentIA()