from Sensor import leitor
from usina import Usina
class controlador():
    def __init__(self,estado = True,usina = Usina()):
        self.__usina = usina
        self.estado = estado #True: comporta aberta, False: Comporta Fechada
    def fechar(self):
       self.__usina.set_actuator(False)
       
        
        
    

