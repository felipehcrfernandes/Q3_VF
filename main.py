from usina import Usina
from Sensor import leitor
from Atuador import controlador
from Subsistema import subsistema

U = Usina()
Leitor = leitor(U)
Controle = controlador(U)
Sub = subsistema(Leitor,Controle)
Sub.operar_sistema()