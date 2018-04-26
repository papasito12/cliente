from io import *

def diccionario():
	merro={}
	contraseñ2nggg=input(str("ss: "))
	contraseñ2n=input(str("contra: "))
	merro[contraseñ2nggg]=contraseñ2n
	los=(merro)
	ll=open("frese.txt","w+")
	ll.write(str(los))
	ll.close()

	loko=open("lesee.txt","r+")
	
	loko.seek(0)
	soock=loko.read()
	print(soock)
	loko.close()
	ll=open("frese.txt","r+")
	ll.seek(0)
	lol=ll.read()
	print(lol)
	ll.close()

	if lol in soock:
		print("vicicicicitoriiaaa")
	
	
	

	


while True:
	midiccionario={}
	midiccionario1={}
	contraseñanggg= input("Repite la contraseña: ")
	contraseñan= input("Repite la contraseña: ")
	if 6<=len(contraseñan)<=12:#aqui la contraseña se vuelve en caracteres y si la contraseña tuviese mas de 12 pues tal y si tuviera menos de 6 pues tal ajajajajajja
		ddd=contraseñan
		midiccionario1[contraseñanggg]=contraseñan
		
		midiccionario.update(midiccionario1)
		
		dd=(midiccionario)
		loko=open("lesee.txt","a+")

		loko.write(str(dd))
		
		loko.close()
		
		
		
	

	

		
		break


	

diccionario()	
