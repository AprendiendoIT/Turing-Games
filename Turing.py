def ganador(num,clavados):
    clavados=int(clavados)
    num=str(num)
    valores=num[10:]
    cont=1
    puntaje=0
    promAux=0
    contganador=1
    for salto in valores: #recorro los valores "777766665555"
        salto=int(salto)
        puntaje+=salto
        if cont%clavados==0: #cuando el contador es divisible por clavados quiere decir que es otro competidor
            prom=puntaje/cont
            if prom>promAux:
                promAux=puntaje/cont
                ganador=contganador
            puntaje=0 #Redefino a 0 para calcular el puntaje del otro competidor
            cont=0 #Redefino a 0 para volver a cont para otro clavadista
            contganador+=1 #Cuento los competidores
        cont+=1
        
    res=[ganador,promAux] #Retorno una lista ya que debo sacar dos valores
    return res

def cantclav(num):
    num=str(num)
    return num[9]

def cantcomp(num):
    num=str(num)
    return num[8]

def temporada(num):
    num=str(num)
    mes=num[4:6]
    mes=int(mes)
    dia=num[6:8]
    dia=int(dia)
    if mes>=6 and mes<=9: #Si se encuentra entre los meses de Junio y Septiembre
        return "Invierno"
    elif mes<=4 or mes>=11: #Si se encuentra entre los meses de Enero a Mayo o es noviembre/diciembre
        return "Verano"
    elif dia>=21 and mes==10: #Si se encuentra entre los dias 21-31 de Octubre 
        return "Verano"
    elif dia<21 and mes==10: #Si se encuentra entre los dias 1-20 de Octubre 
        return "Invierno"
    elif dia<21 and mes==5:  #Si se encuentra entre los dias 1-20 de Mayo
        return "Verano"
    elif dia>=21 and mes==5: #Si se encuentra entre los dias 21-31 de Mayo
        return "Invierno"
    

def sacaranio(num):
    num=str(num)
    return num[0:4]

def main():
    num=int(input("Ingrese el numero de la competencia: "))
    print("Año:",sacaranio(num))
    print("Temporada:",temporada(num))
    
    print("Cantidad de competidores:",cantcomp(num))
    cantclavados=cantclav(num)
    
    print("Cantidad de clavados:",cantclavados)
    listaRes=ganador(num,cantclavados)
    print("Competidor ganador:",listaRes[0],"\nPromedio:",listaRes[1])
main()