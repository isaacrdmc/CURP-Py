
# * Creamos las funciónes del pory3cto


class CurpModel:
    # Creamos el construccotor de la clase
    def __init__(self):
        pass



    # Creamos la función con las variables a utilizar
    def generarCurp(self, nombre, ape_Pa, ape_Ma, fecha_Nac, sexo, estado):
        # * Le decimos que sean en mayuscuals = "Isaac" -> "ISAAC"
        nombre = nombre.upper()
        ape_Pa = ape_Pa.upper()
        ape_Ma = ape_Ma.upper()
        fecha_Nac = fecha_Nac.upper()       # ! Como lo hago?
        sexo = sexo.upper()
        estado = estado.upper()


    # P1: inicial y primera vocal del ap1 + inicial del ap2 e inicial del nombre
    # P2: Fecha AA/MM/DD
    # P3: Sexo (Hombre/Mujer)
    # P4: Entidad federativa
    # * Definimos los estados
    codigoEstadoCurp = ["AS", "BC", "BS", "CC", "CL", "CM", "CS", "CH", "DF", "DG", 
                    "GT", "GR", "HG", "JC", "MC", "MN", "MS", "NT", "NL", "OC",
                    "PL", "QT", "QR", "SP", "SL", "SR", "TC", "TS", "TL", "VZ",
                    "YN", "ZS", "NE"]
    # P5: Primeras consonantes internas de apellidos y nombre
    # P6: Homoclave (No se hace)

    # * Creamos el CURP
    curp = ''


    # Creamos la función para validar el curp 
    def validarCurp(self, curp):
        return 