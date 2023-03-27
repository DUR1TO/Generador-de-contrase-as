import random
import time


def generar_contrasena(longitud=12):
    minus = "abcdefghijklmnopqrstuvwyxz"
    mayus = minus.upper()
    numeros = "0123456789"
    símbolos = "@()[]{}*,;/-_¿?.!¡$<>#&+%"
    base = minus+mayus+numeros+símbolos
    muestra= random.sample(base, longitud)
    password= "".join(muestra)
    return password


    while true:
        try:
            print("Te generaré una contraseña nueva y totalmente segura")
            respuesta = input("""
            ¿Deseas hacerlo?
            Si.
            No.
            """).strip().lower()

            if respuesta == "si":
                password = generar_contrasena()
                print("OK")
                print(f"Tu contraseña generada es: {password}")

                elif respuesta == "no":
                    print("OK, felicidades.")
                    opcion_respuesta = input(
                        "¿Quieres volver a generar una contraseña? (Si/No):").strip().lower()
                        if opcion_respuesta == "si":
                            print("Entonces empecemos de nuevo.")
                            password = generar_contrasena()
                            print("OK")
                            time.sleep(2)
                            print(f"Tu contraseña generada es: {password}")
                            time.sleep(3)
                            elif opcion_respuesta == "no":
                                password = generar_contrasena()
                                print("Bro, sucks.")
                                time.sleep(2)
                                print(f"Tu contraseña generada es: {password}")
                                time.sleep(2)
                    else:
                        time.sleep(2)
                        print("Por favor, ingresa una respuesta válida (Si o No).")
                except ValueError:
                    time.sleep(2)
                    print("A la próxima coloca números no letras.")
                    