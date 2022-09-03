text="Este correo electrónico contiene información privada y confidencial. Si usted no es el destinatario del mensaje no está autorizado a leerlo, copiarlo o difundirlo. Si lo ha recibido por error, por favor contacte con el remitente y destruya su contenido. En cumplimiento del Reglamento (UE) 2016/679 del Parlamento Europeo y del Consejo de 27 de abril de 2016 y de la Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales, le informamos que sus datos de carácter personal son tratados por Suma. Gestión Tributaria. Diputación de Alicante (SUMA), con la finalidad con carácter general de disponer de los datos fiscales de los contribuyentes de la provincia de Alicante, de controlar la documentación de registro, de gestionar las consultas y/o sugerencias, los eventos organizados y las acciones de difusión de la actividad del Organismo así como aquellas otras expresadas en nuestra Política de Privacidad (ver www.suma.es). Podrá ejercer los derechos de acceso, rectificación, oposición, supresión, portabilidad y limitación del tratamiento de sus datos de carácter personal y/o la retirada del consentimiento prestado para el tratamiento de los mismos, dirigiendo su petición a SUMA, Plaza San Cristóbal 1, 03002 Alicante, o bien: dpd@suma.es"
# https://stackoverflow.com/questions/1546226/is-there-a-simple-way-to-remove-multiple-spaces-in-a-string
tx=" ".join(text.split())
tx = tx.split(' ')

# remove the first 'o' character with 9 letters if it contains it.
tx2=tx.copy()
for i in range(len(tx)):
    if (len(tx[i])>=9) & ('o' in tx[i]):
        for j in range(len(tx[i])):
            if tx[i][j]=='o':
                left, right = tx[i][:j], tx[i][j+1:]
                tx2[i]=left+right
                break
text_final=" ".join(tx2)
print("\n", text_final)

# remove the first 'o' word with 9 letters if it contains it.
tx2=[]
for i in range(len(tx)):
    if (len(tx[i])>=9) & ('o' in tx[i]):
        continue
    else:
        tx2.append(tx[i])
text_final=" ".join(tx2)
print("\n", text_final)
    