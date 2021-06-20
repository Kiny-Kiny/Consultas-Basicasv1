global C,R,O,W,L,E,Y,a,l,e,i,s,t,ë,r,XV,XXI
C='\033[1;30m';R='\033[1;31m';O='\033[1;32m';W='\033[1;33m';L='\033[1;34m';E='\033[1;35m';Y='\033[1;36m';XV='\033[1;37m';XXI='\033[0;0m';a='\033[1;40m';l='\033[1;41m';e='\033[1;42m';i='\033[1;43m';s='\033[1;44m';t='\033[1;45m';ë='\033[1;46m';p='\033[;7m'

def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
import os,sys,time,json,subprocess,platform
try:
	from data import ui
	from data import cep
	from data import cpf
	from data import ip
except:
	print(f"{C}[{R}*{C}] Arquivo Corrompido!");exit()
	
try:
    if __name__ == '__main__':
        ui.dialog('Buscando atualizações ...')
        update = subprocess.check_output('git pull', shell=True)
        if 'Already up to date' not in update.decode():
            ui.dialog('Atualização instalada.\nReiniciando...')
            restart()
        else:
            print(f'{C}[{Y}i{C}] Nenhuma atualizacao disponivel.')
            time.sleep(2)
except:
    if os.path.exists('.git'):
        pass
    else:
        ui.error_dialog('Falta de repositório GIT local')

try:
    subprocess.check_output('apt update -y', shell=True)
    os.system("apt install figlet curl -y")
except:
    os.system("pacman -Sy figlet curl")

Sair=False
while(Sair==False):
	ui.banner()
	ui.menu()
	op = input(f'{p}{XV}Digite sua opção:{XXI} ').upper()
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
