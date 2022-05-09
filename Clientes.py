################################
#Parcial F - Juan Pablo Guevara Marulanda 
################################

Txt0="Ingrese {}" #Se escriben como variables todos los textos que se usarán en el código para evitar el Hard Coding

Txt1 ="los productos que va a vender: "
Txt2 ="el nombre del producto {}: "
Txt3 ="el precio del procuto en COP: "
Txt4 ="el descuento hecho si se compran más de diez en %: "

Txt5 ="la cantidad de clientes le compraron hoy: "

Txt6 ="Cliente {}:"
Txt7 ="Nombre: "
Txt8 ="la cantidad de productos diferentes que compró: "
Txt9 ="  Producto: "
Txt10="  Cantidad: "

Txt11='''Valor:         ${}
Valor con IVA: ${}
Descuento:     ${}
Total:         ${}'''

Txt12="El mayor descuento lo obtuvo {}."
Txt13="La orden más cara fue hecha por {}."

Txt14="Ese producto no estaba a la venta."
Txt15="Debe ser un número entero positivo."
Txt16="Los precios y el descuento deben ser números enteros positivos."

Espacio=''' '''

################################
#Función para ingresar los productos a vender
################################

def Productos():

    '''
    La función Productos permite registrar una serie de productos y las retorna en un diccionario de la forma:
    {Nombre del producto:(Precio del producto,Descuento si se compran más de diez))}
    '''
    
    print(Espacio)

    while True: #Se repite hasta que el número ingresado sea un entero positivo
        try:
            N=int(input(Txt0.format(Txt1)))
            if N>0:
                print(Espacio)
                break
            print(Txt15)
        except:
            print(Txt15)
            print(Espacio)

    Producto=""
    Almacen={}
    Cuenta=0

    for i in range(1,N+1):
        Cuenta+=1
        while True:
            try:
                Producto=input(Txt0.format(Txt2.format(Cuenta)))
                Precio=input(Txt0.format(Txt3))
                Descuento=input(Txt0.format(Txt4))
                Almacen[Producto.lower()]=(int(Precio),int(Descuento)) #Asiga la tupla (Precio,Descuento) al nombre del producto en un diccionario
                print(Espacio)
                break
            except:
                print(Txt16)
                print(Espacio)

    return(Almacen)

################################
#Función para registrar los clientes del día
################################

def Clientes(Almacen):

    '''
    La función Clientes permite registrar una serie de personas y lo que compraron del diccionario Almacen y retorna un diccionario de la forma:
    {Nombre del cliente:(Precio total,Descuento))}
    Además, indica cual cliente tuvo el descuento más alto, y cual cliente tuvo la compra más cara.
    '''

    print(Espacio)

    while True: #Se repite hasta que el número ingresado sea un entero positivo
        try:
            M=int(input(Txt0.format(Txt5)))
            if M>0:
                print(Espacio)
                break
            print(Txt15)
        except:
            print(Txt15)

    Nombre=""
    Producto=""
    Precio=0
    Total=0
    Nombres=[]
    Precios=[]
    Descuento=[]
    Registro={}
    Cuenta=0

    for i in range(1,M+1):
        Precio=0
        Total=0
        Cuenta+=1

        print(Txt6.format(Cuenta))
        Nombre=input(Txt7)

        P=eval(input(Txt0.format(Txt8)))

        for j in range(1,P+1):

            print(Espacio)

            while True:

                try:
                    Producto=input(Txt9).lower()
                    Cantidad=int(input(Txt10))
                    Precio+=Almacen[Producto][0]*Cantidad  #LLama al precio del diccionario a través del nombre del producto

                    if Cantidad>10:
                        Total+=Almacen[Producto][0]*Cantidad*1.19*(100-Almacen[Producto][1])/100
                    else:
                        Total+=Almacen[Producto][0]*Cantidad*1.19 
                
                    break

                except ValueError:
                    print(Txt15)
                    print(Espacio)
                except KeyError:
                    print(Txt14)
                    print(Espacio)

        print(Espacio)
        print(Txt11.format(Precio,Precio*1.19,abs(Precio*1.19-Total),Total))
        print(Espacio)

        Nombres.append(Nombre)
        Precios.append(Total)
        Descuento.append(Precio-Total)

        Registro[Nombre]=(Total,Precio-Total) #Asiga la tupla (Precio Total,Descuento Total) al nombre del cliente en un diccionario

    Mayor_Descuento_Pos=Descuento.index(max(Descuento))
    Mayor_Precio_Pos=Precios.index(max(Precios))

    print(Txt12.format(Nombres[Mayor_Descuento_Pos]))
    print(Espacio)
    print(Txt13.format(Nombres[Mayor_Precio_Pos]))
    print(Espacio)

    return(Registro)

################################
#Llamando las funciones
################################

Almacen=Productos()
Ventas=Clientes(Almacen)