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
b = ('—'*33)
# fundo #
a='\033[1;40m'     # Preto
l='\033[1;41m'      # Vermelho
e='\033[1;42m'     # Verde
i='\033[1;43m'      # Amarelo
s='\033[1;44m'     # Azul
t='\033[1;45m'      # Rosa
ë='\033[1;46m'     # Ciano
r='\033[;7m'          # Inverte 

######

import os,time

def banner():
	os.system('clear')
	print(f'{R}——— {XV}MENU {R}———')

def menu():
	print(f'''
{W}>>{XV} Consultar IP \t(01)\t{W}>>{XV} Sair (S).
{W}>>{XV} Consultar CPF\t(02)\t{W}>>{XV} Meu número (M).
{W}>>{XV} Consultar CEP\t(03)\t{W}>>{XV} Grupo no Zap (G).
''')

def error():
	os.system('clear')
	print(f'''
{R}{b}
{XV}\t❗SYSTEM ERROR❗
{R}{b}
''')
	time.sleep(2)

def grupozap():
	os.system('termux-open-url https://chat.whatsapp.com/FK4bA2lsbzo1NGFnpwVmmN')

def meuzap():
	os.system('termux-open-url https://wa.me/5567996968737')