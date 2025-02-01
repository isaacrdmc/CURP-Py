
# * Creamos las funciónes del pory3cto


class CurpModel:
    # Creamos el construccotor de la clase
    def __init__(self):
        pass

    
    # ? -----------------------------------------------------------------
    # ? ------------- Funciónes para la generación del CRUP--------------
    # ? -----------------------------------------------------------------
    # Creamos la función con las variables a utilizar
    def generarCurp(self, nombre, ape_Pa, ape_Ma, fecha_Nac_ano, fecha_Nac_mes, fecha_Nac_dia, sexo, estado):
        # * Le decimos que sean en mayuscuals = "Isaac" -> "ISAAC"
        nombre_mayus = nombre.upper()
        ape_Pa_mayus = ape_Pa.upper()
        ape_Ma_mayus = ape_Ma.upper()
        fecha_Nac_ano_mayus = fecha_Nac_ano.upper()       # ! Como lo hago?
        fecha_Nac_mes_mayus = fecha_Nac_mes.upper()       # ! Como lo hago?
        fecha_Nac_dia_mayus = fecha_Nac_dia.upper()       # ! Como lo hago?
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
        parte2 = (
            # Llamamos las funciones para berificar
            self.
        )

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
    
    # * Revisamos el año
    def validarAno(self, anoSeleccionado):
        # Si el año es igual que 4 y esta entre 1900 y 2025 entonces sera válido
        if len(str(anoSeleccionado)) == 4 and 1900 <= anoSeleccionado <= 2025:
            return True
        return "Error: año invalido"

    # * Revisamos el Mes
    def validarMes(sefl, mesSeleccionado):
        # Verificamos que el mes teng aun valor válido
        if 1 <= mesSeleccionado <=12:
            return True 
        return "Error: mes invalido"
    

    # * Revisamos el Día
    def validarDia(self, diaSeleccionado, anoFecha, mesFecha):
        # Creamos un diccionario con los días por mes del año:
        diasMes = {
            1:31,
            # Si no es biciesto entonces son 28 días
            2: 29 if anoBisiesto(anoFecha) else 28,
            3:31,
            4:30,
            5:31,
            6:30,
            7:31,
            8:31,
            9:30,
            10:31,
            11:30,
            12:31,
        }


        # Primero validamos si el año es bisiesto:
        def anoBisiesto(ano):
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                return True
            
        # Ahora validamos que el día es valido deacuerdo al mes:
        if 1 <= diaSeleccionado <= anoBisiesto.get(mesFecha,0):
            return True
        return "Error: Día inválido"



    # ? -----------------------------------------------------------------
    # ? ------------- Funciónes para la verificación del CRUP--------------
    # ? -----------------------------------------------------------------
    # Creamos la función para validar el curp 
    def validarCurp(self, curp):
        return 
    


# ! Probamos el código:
# Instanciamos la clase para poder utilizarla
modelo = CurpModel()

# Datos
nombre = 'Isaac'
apellidoP = 'Ramírez'
apellidoM = 'Maria Y Campos'
echaNacimiento = '20041004'
sexoHM = 'H'
estadoPais = 'GT'


# Ahora llamamos a la función:
crearCurp = modelo.generarCurp(nombre, apellidoP, apellidoM, echaNacimiento, sexoHM, estadoPais)

# Mostrmos el resultado
print(f'Tu CURP es el siguiente: {crearCurp}')


"""
Que agregi:      SAAC20          RMS
Resultado:  RAM ISAAC20041004 H GT RMS
Esperado:   RAMI 041004 H GT MRS A7
"""