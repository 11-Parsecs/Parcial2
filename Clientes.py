Txt0="Ingrese {}"

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

s=''' '''

Txt12="El mayor descuento lo obtuvo {}."
Txt13="La orden más cara fue hecha por {}."

################################

################################

print(s)
N=input(Txt0.format(Txt1))
print(s)

Producto=""
n={}
p=0

for i in range(1,eval(N)+1):
    p+=1
    Producto=input(Txt0.format(Txt2.format(p)))
    Precio=input(Txt0.format(Txt3))
    Descuento=input(Txt0.format(Txt4))
    n[Producto]=(Precio,Descuento)
    print(s)

################################

################################

print(s)
M=input(Txt0.format(Txt5))

Nombre=""
Producto=""
Precio=0
Total=0
Nombres=[]
m=[]
Descuento=[]
q=0
k=0

for i in range(1,eval(M)+1):
    Precio=0
    Total=0
    q+=1

    print(Txt6.format(q))
    Nombre=input(Txt7)

    P=input(Txt0.format(Txt8))

    for j in range(1,eval(P)+1):
        print(s)
        Producto=input(Txt9)
        Cantidad=input(Txt10) 

        Precio+=eval(n[Producto][0])*eval(Cantidad)  

        if eval(Cantidad)>10:
            Total+=eval(n[Producto][0])*eval(Cantidad)*1.19*(100-eval(n[Producto][1]))/100
        else:
            Total+=eval(n[Producto][0])*eval(Cantidad)*1.19 

    print(s)
    print(Txt11.format(Precio,Precio*1.19,abs(Precio*1.19-Total),Total))
    print(s)

    Nombres.append(Nombre)
    m.append(Total)
    Descuento.append(Precio-Total)

C=m.index(max(m))
D=Descuento.index(max(Descuento))

print(Txt12.format(Nombres[D]))
print(s)
print(Txt13.format(Nombres[C]))
print(s)