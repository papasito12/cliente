from io import *		

		while True:
			registr=input("Ya te has registrado?:" )
			registro=registr.lower()
			if registro=="no":

				while True:
					midiccionario={}
					midiccionario1={}
					gmail = input("Gmail: ")
					arroba=gmail.count("@")

					if (arroba!=1 or gmail.rfind("@")==(len(gmail)-1) or gmail.find("@")==0 ):#esto hace que el gmail cumpla una serie de condiciones como que el @ no este en el principio ni delante del pùtnto y tambien siempre debe haber un . y una @
				
						print("Gmail incorrecto")
					else:
				
						print("Gmail correcto")

						contraseña = input("Contraseña(de 6 a 12 caracteres): ")
						contraseñan= input("Repite la contraseña: ")
						if 6<=len(contraseña)<=12 and contraseña==contraseñan:#aqui la contraseña se vuelve en caracteres y si la contraseña tuviese mas de 12 pues tal y si tuviera menos de 6 pues tal ajajajajajja
							ddd=contraseñan
							midiccionario1[gmail]=contraseña
		
							midiccionario.update(midiccionario1)
		
							dd=(midiccionario)
							loko=open("lesee.txt","a+")

							loko.write(str(dd))
		
							loko.close()
							
							break
						else:
							print("Contraseña invalida")
			elif registro=="si":
				while True:
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
						
						loko.close()
						ll=open("frese.txt","r+")
						ll.seek(0)
						lol=ll.read()
	
						ll.close()
						if lol in soock:
							print("Gmail y Contraseña correctas")
							break