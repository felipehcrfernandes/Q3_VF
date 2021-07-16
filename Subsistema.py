from Atuador import controlador
from Sensor import leitor
from usina import Usina

class subsistema():
    def __init__(self,leitor,controlador):
        self.leitor = leitor
        self.controlador = controlador        
    def operar_controlador(self):
        self.leitor.saidaSensor()
        self.controlador.fechar()

