from Atuador import controlador
from Sensor import leitor
from usina import Usina

class subsistema():
    def __init__(self,leitor,controlador):
        self.leitor = leitor
        self.controlador = controlador        
    def operar_sistema(self):
        self.leitor.saidaSensor()
        self.controlador.fechar()

