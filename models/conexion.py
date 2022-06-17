from dropbox import Dropbox
import dropbox
from dropbox.files import WriteMode


class Conexion:
    def __init__(self, nombre_archivo: str, access_token: str):
        self.__dbx: Dropbox = dropbox.Dropbox(access_token)
        self.__destino: str = f"/Logs/{nombre_archivo}.txt"
        self.__dbx.files_upload(
            b"REGISTROS", self.__destino, mode=dropbox.files.WriteMode.overwrite
        )

    def escribir(self, texto: bytes):
        self.__dbx.files_upload(
            texto, self.__destino, mode=dropbox.files.WriteMode.overwrite
        )
