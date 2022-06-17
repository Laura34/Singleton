from datetime import datetime
from models.conexion import Conexion
from models.databaseMeta import DatabaseMeta


class Nube(metaclass=DatabaseMeta):
    def __init__(self, nombre_archivo: str, access_token: str) -> None:
        self.__contenido: bytes = b""
        self.__conexion = Conexion(nombre_archivo, access_token)

    def msg(self, mensaje: str):
        cadena = f"\n[{datetime.now()}]\tMensaje:\t{mensaje}"
        self.__contenido += bytes(cadena, "utf-8")
        self.__conexion.escribir(self.__contenido)

    def exito(self, mensaje: str):
        cadena = f"\n[{datetime.now()}]\tExito:\t\t{mensaje}"
        self.__contenido += bytes(cadena, "utf-8")
        self.__conexion.escribir(self.__contenido)

    def advertencia(self, mensaje: str):
        cadena = f"\n[{datetime.now()}]\tAdvertencia:\t{mensaje}"
        self.__contenido += bytes(cadena, "utf-8")
        self.__conexion.escribir(self.__contenido)

    def error(self, mensaje: str):
        cadena = f"\n[{datetime.now()}]\tError:\t\t{mensaje}"
        self.__contenido += bytes(cadena, "utf-8")
        self.__conexion.escribir(self.__contenido)
