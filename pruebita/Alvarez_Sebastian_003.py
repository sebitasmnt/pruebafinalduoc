import csv

lista = []


def menu():
    print("Menu pinky y cerebrito")
    print("1.- Agregar plan")
    print("2.-Listar planes")
    print("3.-Eliminar plan por ID")
    print("4.-Generar csv")
    print("5.-Cargar csv")
    print("6.- Estadisticas")
    print("0.- Salir")
    
def validar():
    try:
        
        if 0 <= porcentaje <= 100:
            return ("Siga nomas")
        else:
            return ("Porfavor ingrese un porcentaje valido")
            
    except:
        print("Error, volviendo al menu de agregar plan")
            
        
        
        
def estadisticas():
        acumulador  = 0
        porcentaje_max = 0
        
        for x in lista:
             
            acumulador =+ x['porcentaje']
            if x['porcentaje'] > porcentaje_max:
                porcentaje_max = x['porcentaje']
            
        total_lista = len(lista)
        promedio = acumulador / total_lista
            
        print("El promedio de porcentajes es",promedio)
        print("El porcentaje mas alto hasta ahora es ",porcentaje_max)
        

    
        

    
    
while True:
    menu()
    eleccion = int(input("Ingrese una opcion, 0 para salir"))
    
    if eleccion == 1:
        print("Agregar plan")
        
        id  = int(input("Ingrese ID"))
        nombre  = input("Ingrese nombre")
        porcentaje = int(input("Ingrese porcentaje de efectividad"))
        
        validar()
        
        if 0 <= porcentaje <= 25:
            categoria = "Chiste"
        elif 26 <= porcentaje <= 50:
            categoria = "Anecdota"
        elif 51 <= porcentaje <=75:
            categoria = "Peligro"
        elif 76 <= porcentaje <= 99:
            categoria = "Atencion"
        elif porcentaje == 100:
            categoria = "Esclavitud"
            
        diccionario = {'id':id,'nombre':nombre,'porcentaje':porcentaje,'categoria':categoria}
        lista.append(diccionario)
        
        
        
        
        
    elif eleccion == 2:
        print("listar planes")
        for x in lista:
            print(x)
    elif eleccion == 3:
        print("Eliminar por ID")
        encontrado = False
        buscar_id = int(input("Ingrese el id a buscar\n"))
        for x in lista:
            if x['id'] == buscar_id:
                respuesta = input("Está seguro??? (si/no)\n")
                if respuesta == "si":
                    encontrado = True
                    lista.remove(x)
                    print("Personaje eliminado correctamente")
                else:
                    print("Saliendo....")
                    break
              
   
        if encontrado == False:
            print("Adios!!")        
                


               
    elif eleccion == 4:
        print("Generar CSV")
        with open('pinky.csv','w',newline='') as pinky:
            campos = ['id','nombre','porcentaje','categoria']
            escritor_csv = csv.DictWriter(pinky,fieldnames=campos)
            escritor_csv.writeheader()
            escritor_csv.writerows(lista)
    elif eleccion == 5:
        print("Cargar csv")
        lista.clear()
        
        with open('pinky.csv','r',newline='') as pinky:
            lector_csv = csv.DictReader(pinky)
            for x in lector_csv:
                x['id'] = int(x['id'])
                x['porcentaje'] = int(x['porcentaje'])
                lista.append(x)
    elif eleccion == 6:
        print("Estadisticas")
        estadisticas()
       
            
    elif eleccion == 0:
        print("Adios!!!")
        break