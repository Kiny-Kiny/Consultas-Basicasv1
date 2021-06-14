import os,time
from data import ui
from data import cep
from data import cpf
from data import ip
## Tabela de cores ANSI (Python) \\ OK

global C,R,O,W,L,E,Y,a,l,e,i,s,t,ë,r,XV,XXI

# fonte #
C='\033[1;30m'     # Preto 
R='\033[1;31m'     # Vermelho 
O='\033[1;32m'     # Verde 
W='\033[1;33m'    # Amarelo 
L='\033[1;34m'     # Azul 
E='\033[1;35m'     # Rosa
Y='\033[1;36m'     # Ciano

##
XV='\033[1;37m'     # Branco
XXI='\033[0;0m'      # Remover
##

# fundo #
a='\033[1;40m'     # Preto
l='\033[1;41m'      # Vermelho
e='\033[1;42m'     # Verde
i='\033[1;43m'      # Amarelo
s='\033[1;44m'     # Azul
t='\033[1;45m'      # Rosa
ë='\033[1;46m'     # Ciano
p='\033[;7m'          # Inverte 

###

Sair=False
while(Sair==False):
	ui.banner()
	ui.menu()
	op = input(f'{p}{XV}Digite sua opção:{XXI} ').upper()
	print(f'{XV}Aguarde...')
	time.sleep(3)
	if op == '1':
		ip.consultar()
	elif op == '2':
		cpf.consultar()
	elif op == '3':
		cep.consultar()
	
	elif op == 'S':
		os.system('clear')
		Sair=True
	elif op == 'M':
		ui.meuzap()
	elif op == 'G':
		ui.grupozap()
	else:
		ui.error()
		