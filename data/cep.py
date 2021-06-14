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
{XV}[{W} AVISO {XV}] {C}Digite o CEP sem pontos ou traços.\n''')
		cep = input(f'{L}Digite o CEP que deseja consultar:{Y} ')
		print(f'\n{XXI}❬❗❭ {XV}Consultando, aguarde.')
		try:		
			if len(cep) != 8:
					print(f'{W}Quantidade de digitos invalida!')
					time.sleep(1)
					ui.error()
			
			
			r = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
			
			
			data = r.json()
								
			if 'erro' not in data:
								
					print(f'\n{R}Resultados: \n')
			
					print('{}Cep:{} {}'.format(L, Y, data['cep']))
					print('{}Logradouro:{} {}' .format(L, Y, data['logradouro']))
					print('{}Complemento:{} {}'.format(L, Y, data['complemento']))
					print('{}Bairro:{}{}'.format(L, Y, data['bairro']))
					print('{}Localidade:{} {}'.format(L, Y, data['localidade']))
					print('{}Estado:{} {}'.format(L, Y, data['uf']))
			
			else:
					print('\n{}{}: {}CEP invalido!\n'.format(R, cep, W))
					time.sleep(1)
		except:
				pass
				
		opção = input('{}{}Deseja realizar uma nova consulta?{}\n\n{}[ 1 ] {}Sim.\n{}[ 2 ] {}Voltar.\n\n{}R:{} '.format(p, XV, XXI, C, XV, C, XV, R, W))
							
					
		if  opção == '1':
				pass
		elif opção == '2':
				Sair=True
						
		else:
				ui.error()
	
		
if __name__ == '__main__':
	consultar()