import pickle

print("bienvenido")

while True:
	registr=input("Ya te has registrado?:" )
	registro=registr.lower()
	if registro=="no":

		while True:
			gmail = input("Gmail: ")
			arroba=gmail.count("@")

			if (arroba!=1 or gmail.rfind("@")==(len(gmail)-1) or gmail.find("@")==0 ):#esto hace que el gmail cumpla una serie de condiciones como que el @ no este en el principio ni delante del pùtnto y tambien siempre debe haber un . y una @
				
				print("Mail incorrecto")
			else:
				
				print("Mail correcto")

				contraseña = input("Contraseña(de 6 a 12 caracteres): ")
				contraseñan= input("Repite la contraseña: ")
				if 6<=len(contraseña)<=12 and contraseña==contraseñan:#aqui la contraseña se vuelve en caracteres y si la contraseña tuviese mas de 12 pues tal y si tuviera menos de 6 pues tal ajajajajajja
					print("Tú contraseña es válida")
					ddd=(gmail,contraseña)
					op=open("gmailpcontrasena","ab+")
					pickle.dump(ddd,op)
					op.close()
					break
				else:
					print("Contraseña invalida")
	elif registro=="si":
		while True:
			sgmail=input("Gmail: ")
			scontraseña=input("Contraseña: ")
			op=open("gmailpcontrasena","rb+")
			pickle.load(op)
			if op==sgmail and op==scontraseña:
				print("Correo y Contraseña correctos")
				break
			else:
				print("Correo y contraseña invalidos")
print("dfvvf")
