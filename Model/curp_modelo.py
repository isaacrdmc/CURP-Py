
# * Creamos las funciónes del pory3cto


class CurpModel:
    # Creamos el construccotor de la clase
    def __init__(self):
        pass




    
    # ? -----------------------------------------------------------------
    # ? ------------- Funciónes para la generación del CRUP--------------
    # ? -----------------------------------------------------------------
    # Creamos la función con las variables a utilizar
    def generarCurp(self, nombre, ape_Pa, ape_Ma, fecha_Nac, sexo, estado):
        # * Le decimos que sean en mayuscuals = "Isaac" -> "ISAAC"
        nombre_mayus = nombre.upper()
        ape_Pa_mayus = ape_Pa.upper()
        ape_Ma_mayus = ape_Ma.upper()
        fecha_Nac_mayus = fecha_Nac.upper()       # ! Como lo hago?
        sexo_mayus = sexo.upper()
        estado_mayus = estado.upper()


        # ^ P1: inicial y primera vocal del ap1 + inicial del ap2 e inicial del nombre

        parte1 = (
            # Llamamos la función para buscar las vocales dentro d elos apellidos
            ape_Pa_mayus[0] + 
            self.buscarVocal(ape_Pa_mayus) + 
            ape_Ma_mayus[0] + 
            nombre_mayus
        )

        # ^ P2: Fecha AA/MM/DD
        parte2 = fecha_Nac_mayus

        # ^ P3: Sexo (Hombre/Mujer)
        parte3 = sexo_mayus

        # ^ P4: Entidad federativa
        parte4 = estado_mayus

        # ^ P5: Primeras consonantes internas de apellidos y nombre
        parte5 = (
            self.buscarConsonante(ape_Pa_mayus) + 
            self.buscarConsonante(ape_Ma_mayus) + 
            self.buscarConsonante(nombre_mayus)
        )

        # ^ P6: Homoclave (No se hace)

        # * Creamos el CURP
        curp = parte1 + parte2 + parte3 + parte4 + parte5

        # ? Devolvemos el CURP como respuesta
        return curp


    # * Buscmaos la primera vocal de la palabra
    def buscarVocal(self, palabra):
        for letra in palabra[1:]:
            if letra in 'AEIOU':
                return letra
        return " "
    
    # * Buscamos la primera consonante de la palabra
    def buscarConsonante(self, palabra):
        for letra in palabra:
            if letra not in 'AEIOU':
                return letra
        return " "



    # ? -----------------------------------------------------------------
    # ? ------------- Funciónes para la verificación del CRUP--------------
    # ? -----------------------------------------------------------------
    # Creamos la función para validar el curp 
    def validarCurp(self, curp):
        return 