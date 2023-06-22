# flake8 main.py
# mypy main.py

# from fila_normal import FilaNormal
# from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida


# fila_teste = FilaNormal()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# print(fila_teste.chama_cliente(5))
# print(fila_teste.chama_cliente(5))
#
# fila_teste_2 = FilaPrioritaria()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# print(fila_teste_2.chama_cliente(10))
# print(fila_teste_2.chama_cliente(1))
# print(fila_teste_2.estatistica('01/01/2001', 215, 'detail'))

teste_fabrica = FabricaFila.pega_fila('prioritaria')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(10))

print(teste_fabrica.estatistica(EstatisticaResumida('20/03/2025', 120,)))

teste_fabrica2 = FabricaFila.pega_fila('prioritaria')
teste_fabrica2.atualiza_fila()
teste_fabrica2.atualiza_fila()
teste_fabrica2.atualiza_fila()
print(teste_fabrica2.chama_cliente(14))

print(teste_fabrica2.estatistica(EstatisticaDetalhada('20/03/2025', 120,)))
