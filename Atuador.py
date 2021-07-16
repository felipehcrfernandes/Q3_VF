from Sensor import leitor
from usina import Usina
class controlador():
    def __init__(self,estado = True,usina = Usina()):
        self.__usina = usina
        self.estado = estado
    def fechar(self):
       self.__usina.set_actuator(False)
       print(self.__usina.get_actuator())
        
        
'''
U = Usina()
Controle = controlador(U)  
Controle.abrir()
'''
    
    

