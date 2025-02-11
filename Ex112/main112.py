#from utilidadadesCeV.moeda import resumo
from utilidadadesCeV.dado import leia_dinheiro
from utilidadadesCeV import moeda

preco = leia_dinheiro('Digite o preco: R$')
moeda.resumo(preco, 80, 35)