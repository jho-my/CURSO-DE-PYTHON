print("Tipos de datos en Python")
# tipo String
nombre = "Jhonatan Isai"
apellidoSegundo = "Ojeda Sanchez"
nombreCompleto = "Hola mi nombre es: "+nombre + " "+apellidoSegundo
print("Hola mi nombre es "+nombre+" "+apellidoSegundo)
print(nombreCompleto)

# verificamos el tipo de dato de una varible
print("Tipo de dato de la variable: "+nombre)
print(type(nombre))
print("")


#tipo int (entero)
print("TIPO DE DATO INT")
edad = 18
edad += 1
print("Edad: ",edad)
print("Tu edad es: "+str(edad))
print("Tipo de dato de la variable edad: ",type(edad))
print("")
#tipo float
altura =  180.5
print("TIPO DE DATO FLOAT")
print(altura," cm")
print("Tipo de dato de la variable altura: ",type(altura))
print("Tu altura es: "+str(altura)+" cm")
print("")

#tipo de dato boolean
print("TIPO DE DATO BOOLEAN")
humano = False
print("Es humano: ",humano)
print("Tipo de dato de la variable Humano: ",type(humano))
print("Eres un humano: "+str(humano))