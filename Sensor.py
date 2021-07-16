from usina import Usina
import numpy as np
import matplotlib.pyplot as plt
import time
class leitor():
    def __init__(self,saida=0,usina = Usina()):
        self.__saida = saida #saida do sensor em metros
        self.__usina= usina
    def saidaSensor(self):
        nivel = self.__usina.get_sensor()
        saida = 10 + nivel*(80/255) #saida do sensor em metros
        count = 0
        x = []        
        while saida > 70:
            self.__usina.set_actuator(True)
            nivel = self.__usina.get_sensor()
            saida = 10 + nivel*(80/255)
            self.__saida = saida
            print(self.__saida)
            x.append(self.__saida)       
            time.sleep(0.1)
            count = count + 1

        stop = 0.1*count        
        y = np.arange(0,stop,0.1)
        fig,ax = plt.subplots()
        ax.plot(y,x,'b-',linewidth=5)
        plt.show()

    @property
    def saida(self):
        return self.__saida
    
               
    
