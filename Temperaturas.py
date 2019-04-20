##Se que todo esto se podia hacer en muchas menos lineas y menos complicado con el uso de las funciones
##Pero aun no las he estudiado lo suficiente xd
import math
def temperaturas ( ):
    registro=0
    tssantander=[ ]
    tguajira=[ ]
    tnariño=[ ]
    a=0
    prom=[ ]
    f=0
    d=1
    sumsantander=0
    sumguajira=0
    sumnariño=0
    menu1 = " "
    meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    while menu1 != "1" or menu1 != "2":
        print("Digite alguna opción")
        print("Digite /1/ para añadir las temperaturas, Digite /2/ para mirar el promedio de esas temperaturas")
        menu1=input(" ")
        if menu1=="1":
            while registro<12 and f<12 and d<13:
                registro += 1
                print("Por favor digite las temperaturas de los departamentos del mes de",meses[f:d])
                f+=1
                d+=1
                while True:
                    try:
                        print("Temperatura de Santander: ")
                        can=1
                        mayors=0
                        menors=0
                        i=1
                        while(can>0):
                            santander = int(input( ))
                            tssantander.append(santander)
                            sumsantander+=santander
                            i=i+1
                            can=can-1
                            mayors=max(tssantander)
                            menors=min(tssantander)
                        break
                    except ValueError:
                        print("Asegurese de digitar un numero entero")
                while True:
                    try:
                        print("Temperatura de Guajira: ")
                        can=1
                        mayorg=0
                        menorg=0
                        i=1
                        while(can>0):
                            guajira =  int(input( ))
                            tguajira.append(guajira)
                            sumguajira+=guajira
                            i=i+1
                            can=can-1
                            mayorg=max(tguajira)
                            menorg=min(tguajira)
                        break
                    except ValueError:
                        print("Asegurese de digitar un numero entero")
                while True:
                    try:
                        print("Temperatura de Nariño: ")
                        can=1
                        mayorn=0
                        menorn=0
                        i=1
                        while(can>0):
                            nariño = int(input( ))
                            tnariño.append(nariño)
                            sumnariño+=nariño
                            i=i+1
                            can=can-1
                            mayorn=max(tnariño)
                            menorn=min(tnariño)
                        break
                    except ValueError:
                        print("Asegurese de digitar un numero entero")
            if registro==12 and f==12 and d==13:
                registro-=12
                a += 1
                lel=("Registro",a)
                tssantander.append(lel)
                tguajira.append(lel)
                tnariño.append(lel)
                f-=12
                d-=12
        if menu1=="2":
            menu2 = " "
            while menu2 != "a" and menu2 != "b" and menu2 != "c" and menu2 != "d" and menu2 != "e" and menu2 != "f" and menu2 != "g":
                print("Digite alguna opción")
                print("Digite /a/ para ver el promedio de la temperatura de cada departamento")
                print("Digite /b/ para ver el promedio de la temperatura a nivel nacional")
                print("Digite /c/ para ver el mes mas caliente de cada departamento")
                print("Digite /d/ para ver el promedio de la temperatura de los meses mas calientes de los 3 departamentos")
                print("Digite /e/ para ver cual fue el promedio mas caliente de los 3 departamentos")
                print("Digite /f/ para ver la temperatura mas caliente del año en su respectivo departamento y mes")
                print("Digite /g/ para ver la desviación estandar de la temperatura de cada departamento")
                print("Digite /0/ para volver")
                menu2=input(" ")
                if menu2 == "0":
                    break
                if menu2 == "a":
                    menudep=" "
                    while menudep != "0":
                        print("Digite /s/ para ver el prom de Santander, /g/ para ver el prom de Guajira, /n/ para ver el prom de Nariño")
                        print("Digite /0/ para volver")
                        menudep=input(" ")
                        if menudep == "s":
                            proms= sumsantander/12
                            print(proms)
                        if menudep == "g":
                            promg= sumguajira/12
                            print(promg)
                        if menudep == "n":
                            promn= sumnariño/12
                            print(promn)
                if menu2 == "b":
                    proms=sumsantander/12
                    promg=sumguajira/12
                    promn=sumnariño/12
                    promxd=proms+promg+promn/3
                    print("El promedio de la temperatura ´´Nacional´´ es de:",promxd)
                if menu2 == "c":
                    menudep2= " "
                    while menudep2 != "0":
                        print("Digite /s/ para ver el mes mas caliente de santander, /g/ para ver el mes mas caliente de guajira, /n/ para ver el mes mas caliente de nariño")
                        print("Digite /0/ para volver")
                        menudep2=input(" ")
                        if menudep2 == "s":
                            print("Temperatura mas alta de Santander", mayors)
                            print("Temperatura mas baja de Santander", menors)
                        if menudep2 == "g":
                            print("Temperatura mas alta de Guajira", mayorg)
                            print("Temperatura mas baja de Guajira", menorg)
                        if menudep2 == "n":
                            print("Temperatura mas alta de Nariño", mayorn)
                            print("Temperatura mas baja de Nariño", menorn)
                if menu2 == "d":
                    promtemperaturasxd= mayors+mayorg+mayorn/3
                    print("Promedio de temperaturas mayores:",promtemperaturasxd)
                if menu2 == "e":
                    proms=sumsantander/12
                    promg=sumguajira/12
                    promn=sumnariño/12
                    if promg>promn:
                        if proms>promg:
                            print("Promedio mayor; Santander:", proms)
                        else:
                            print("Promedio mayor; Guajira:", promg)
                    else:
                        if proms>promn:
                            print("Promedio mayor; Santander:", proms)
                        else:
                            print("Promedio mayor; Nariño:", promn)
                if menu2 == "f":
                    try:
                        if mayorg>mayorn:
                            if mayors>mayorg:
                                print("Temperatura mayor, Santander:", mayors)
                            else:
                                print("Temperatura mayor, Guajira:", mayorg)
                        else:
                            if mayors>mayorn:
                                print("Temperatura mayor, Santander:", mayors)
                            else:
                                print("Temperatura mayor, Nariño:", mayorn)
                    except ValueError:
                        print("Pls asegurese de que hallan valores en las listas")
                        #No supe como hacer lo de cual fue el mes#
                if menu2 == "g":
                    print("Digite /s/ para ver la desviación estandar de santander, /g/ para ver la desviación estandar de la guajira /n/ para ver la desviación estandar de nariño")
                    s = " "
                    while s != "0":
                        print("Digite /s/ para ver la desviación estandar de santander, /g/ para ver la desviación estandar de la guajira /n/ para ver la desviación estandar de nariño")
                        s = input(" ")
                        if s == "s":
                            x= sumsantander/12
                            rest=0
                            for i in tssantander:
                                rest=rest+i-x
                                print(rest)
                                rest**2
                            xdddd= math.sqrt(rest)
                            asdf=xdddd/4
                            ss= math.sqrt(asdf)
                            print("Desviación estandar de la temperatura de santander:", ss)
                        if s == "g":
                            xg = sumguajira/12
                            restg=0
                            for i in tguajira:
                                restg=restg+i-xg
                                print(restg)
                                restg**2
                            xdsds= math.sqrt(restg)
                            asdfg= xdsds/4
                            sg= math.sqrt(asdfg)
                        if s == "n":
                            xn = sumnariño/12
                            restn=0
                            for i in tnariño:
                                restn=restn+i-xn
                                print(restn)
                                rest**2
                            uuuu= math.sqrt(restn)
                            abcd= uuuu/4
                            sn= math.sqrt(abcd)
                        #Al finalizar esta parte del codigo tira error en vez de regresar al menu :,v
temperaturas ( )

