from PySide2.QtCore import QObject
import serial, serial.tools.list_ports

class ComunicacaoSerialPorta(QObject):
    def __init__(self):
        super().__init__()
        
        self.serialInst = serial.Serial()
        self.baudrates = ["9600", "19200", "115200"]
        self.portas = []

    def listarPostas(self):
        self.portas = [
            porta.device for porta in serial.tools.list_ports.comports()
        ]

    def conectarSerial(self):
        try:
            self.serialInst.open()
        except:
            print("Erro ao conectar")

    def desconectarSerial(self):
        try:
            self.serialInst.close()        
        except:
            print("Erro ao desconectar")
