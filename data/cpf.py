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

import os,time,requests
from data import ui

def consultar():
	Sair=False
	while(Sair==False):
		os.system('clear')
		print(f'''
{XV}[{W} AVISO {XV}] {C}Digite o CPF sem pontos ou traços.
{XV}[{W} NOTA {XV}] {C}Eu tenho outra API de CPF, uma melhor!\n''')
		cpf = input(f'{L}Digite o CPF que deseja consultar:{Y} ')
		print(f'\n{XXI}❬❗❭ {XV}Consultando, aguarde.')
		try:
			if len(cpf) != 11:
				print(f'{W}Quantidade de digitos invalida!')
				time.sleep(1)
				ui.error()
					
			r = requests.get(f'http://api.trackear.com.br:80/basepv/cpf/{cpf}/noip')
			data = r.json()
			
			if 'erro' not in data:
				print(f'\n{R}Resultados:\n')
				print('{}Code:{} {}'.format(L, Y, data['code']))
				print(f'{L}Cpf:{Y} {cpf}')
				print('{}Nome:{} {}'.format(L, Y, data['nome']))
				print('{}Sexo:{} {}'.format(L, Y, data['sexo']))
				print('{}SexoSig:{} {}'.format(L, Y, data['sexoSig']))
				print('{}Data De Nascimento:{} {}'.format(L, Y, data['dtNascimento']))
				print('{}Idade:{} {}'.format(L, Y, data['idade']))
				print('{}Data da Consulta:{} {}'.format(L, Y, data['dtConsulta']))
				print('{}Delay:{} {}\n'.format(L, Y, data['delay']))
			
			else:
				print('\n{}{}: {}CPF invalido!\n'.format(R, cpf, W))
				time.sleep(1)
		except:
			pass
			
		opção = input('{}{}Deseja realizar uma nova consulta?{}\n\n{}[ 1 ] {}Sim.\n{}[ 2 ] {}Voltar.\n\n{}R:{} '.format(p, XV, XXI, C, XV, C, XV, R, W))
		os.system('clear')
				
		if  opção == '1':
			pass
		elif opção == '2':
			Sair=True
			
		else:
			ui.error()
if __name__ == '__main__':
	consultar()