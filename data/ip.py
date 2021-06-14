from data import ui

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
def consultar():
	Sair=False
	while(Sair==False):
		os.system('clear')
		print(f'''
{XV}[{W} AVISO {XV}] {C}Digite o IP com os pontos.\n''')
		try:
				
			ip = input(f'{L}Digite o IP que deseja consultar: {Y}')
			print(f'\n{XXI}❬❗❭ {XV}Consultando, aguarde.')
			r = requests.get('http://ip-api.com/json/{}'.format(ip))
			data = r.json()
			if 'erro' not in data:
				print(f'\n{R}Resultados: \n')
						
				print('{}IP:{} {}'.format(L, Y, data['query']))
				print('{}Status:{} {}'.format(L, Y, data['status']))
				print('{}País:{} {}'.format(L, Y, data['country']))
				print('{}Abreviação:{} {}'.format(L, Y, data['countryCode']))
				print('{}Região:{} {}'.format(L, Y, data['region']))
				print('{}Nome da região:{} {}'.format(L, Y, data['regionName']))
				print('{}Cidade:{} {}'.format(L, Y, data['city']))
				print('{}Cep:{} {}'.format(L, Y, data['zip']))
				print('{}Latitude:{} {}'.format(L, Y, data['lat']))
				print('{}Longitude:{} {}'.format(L, Y, data['lon']))
				print('{}Timezone:{} {}'.format(L, Y, data['timezone']))
				print('{}Isp:{} {}'.format(L, Y, data['isp']))
				print('{}Org:{} {}'.format(L, Y, data['org']))
				print('{}As:{} {}'.format(L, Y, data['as']))
			else:
					print('\n{}{}: {}IP invalido!\n'.format(R, ip, W))
					time.sleep(1)
		except:
			pass
		opção = input('\n{}{}Deseja realizar uma nova consulta?{}\n\n{}[ 1 ] {}Sim.\n{}[ 2 ] {}Voltar.\n\n{}R:{} '.format(p, XV, XXI, C, XV, C, XV, R, W))
		os.system('clear')
				
		if  opção == '1':
			pass
		elif opção == '2':
			Sair=True
				
		else:
			ui.error()

if __name__ == '__main__':
	consultar()