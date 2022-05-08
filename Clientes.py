Txt0="Ingrese {}"

Txt1 ="los productos que va a vender: "
Txt2 ="el nombre del producto {}: "
Txt3 ="el precio de cada uno: "
Txt4 ="el descuento hecho si se compran más de diez: "

Txt5 ="la cantidad de clientes le compraron hoy: "

Txt6 ="Cliente {}:"
Txt7 ="  Nombre: "
Txt8 ="  Producto: "
Txt9 ="  Cantidad: "

Txt10="{:10s} {:5s} {:3d}  ${:7.2f}"
Txt11='''
Valor:         ${}
Valor con IVA: ${}
Descuento:     {}%
Total:         ${}
'''

N=input(Txt0.format(Txt1))

n=[]
p=0

for i in range(1,eval(N)+1):
    p+=1
    n.append(input(Txt0.format(Txt2.format(p))))
    print(n)