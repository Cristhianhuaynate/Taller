""" Se desea obtener la nómina semanal salario neto de los empleados de una empresa cuyo trabajo se paga por horas y del modo siguiente:
Las horas inferiores o iguales a 35 horas(normales) se pagan a una tarifa determinada que se debe introducir por teclado
al igual que el numero de horas y nombre del trabajador
Las horas superiores a 35 se pagaran como extras a un promedio de 1.5 por hora
Los impuestos a deducir a los trabajadores varian en funcion de su sueldo mensual

sueldo = 2000 libre de impuestos
los siguientes 220 euros al 20 por 100
el resto al 30 por 100
"""

nombre = input("Ingrese el nombre del trabajador");
horas = float(input("Ingrese las horas del trabajo del trabajador"));
tarifa = float(input("Ingrese la tarifa "));

if horas <= 35:
    sbruto = horas * tarifa;
else:
    sbruto=35 * tarifa + (horas - 35) * 1.5 * tarifa;

if sbruto <= 2000:
    impuesto=0;
elif (sbruto > 2000) and (sbruto <= 2200):
    impuesto= (sbruto - 2000) * 0.20
else:
    impuesto=(220 * 0.20) + (sbruto - 2220) * 0.30;            

sneto=sbruto - impuesto;
print("El trabajador",nombre);
print("Tiene un sueldo bruto de :",sbruto);
print("LOs impuesto que paga son :",impuesto);
print("El sueldo neto que recibe es :",sneto);
