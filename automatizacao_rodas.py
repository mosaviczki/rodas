from os import add_dll_directory


MENU = """
Voce quer usar
1 - Polegadas
2 - Centimetros
3 - SAIR
"""
pop = True
while pop == True:
    print(MENU)
    op = int(input())
    if op is 1:
        MTOW = float(input('MTOW (kg): '))
        df = float(input('Distribuicao de peso do TP dianteiro (decimal): '))
        dt = float(input('Distribuicao de peso do TP traseiro (decimal): '))
        nf = float(input('Numero de rodas frontais: '))
        nt = float(input('Numero de rodas traseiras: '))
        pop1 = True
        MENU2 = """
        Voce quer usar
        1 - Aviação
        2 - Business Twin
        3 - Transporte/Bombardeiro
        4- Aviao de caça
        """
        while pop1 == True:
            print(MENU2)
            op2 = int(input())
            if op2 is 1:
                #Calculo diametro e espessura rodas frontais
                Wwf = (MTOW * df)/nf
                d_f = 1.51 * (Wwf**0.349)
                e_f = 0.715 * (Wwf**0.312)
                print("Wwf: {:.3f} Kg" .format(Wwf))
                print("d_f: {:.3f} cm" .format(d_f))
                print("e_f: {:.3f} cm" .format(e_f))
                #Calculo diametro e espessura rodas trasseiras
                Wwt = (MTOW * dt)/nt
                d_t = 1.51 * (Wwt**0.349)
                e_t = 0.715 * (Wwt**0.312)
                print("Wwt: {:.3f} Kg" .format(Wwt))
                print("d_t: {:.3f} cm" .format(d_t))
                print("e_t: {:.3f} cm" .format(e_t))

            elif op2 is 2:
                #Calculo diametro e espessura rodas frontais
                Wwf = (MTOW * df)/nf
                d_f = 2.69 * (Wwf**0.251)
                e_f = 1.17 * (Wwf**0.216)
                print("Wwf: {:.3f} Kg" .format(Wwf))
                print("d_f: {:.3f} in" .format(d_f))
                print("e_f: {:.3f} in" .format(e_f))
                #Calculo diametro e espessura rodas trasseiras
                Wwt = (MTOW * dt)/nt
                d_t = 2.69 * (Wwt**0.251)
                e_t = 1.17 * (Wwt**0.216)
                print("Wwt: {:.3f} Kg" .format(Wwt))
                print("d_t: {:.3f} in" .format(d_t))
                print("e_t: {:.3f} in" .format(e_t))

            elif op2 is 3:
                #Calculo diametro e espessura rodas frontais
                Wwf = (MTOW * df)/nf
                d_f = 1.63 * (Wwf**0.315)
                e_f = 0.1043 * (Wwf**0.48)
                print("Wwf: {:.3f} Kg" .format(Wwf))
                print("d_f: {:.3f} in" .format(d_f))
                print("e_f: {:.3f} in" .format(e_f))
                #Calculo diametro e espessura rodas trasseiras
                Wwt = (MTOW * dt)/nt
                d_t = 1.63* (Wwt**0.315)
                e_t = 0.1043 * (Wwt**0.48)
                print("Wwt: {:.3f} Kg" .format(Wwt))
                print("d_t: {:.3f} in" .format(d_t))
                print("e_t: {:.3f} in" .format(e_t))

            elif op2 is 4:
                #Calculo diametro e espessura rodas frontais
                Wwf = (MTOW * df)/nf
                d_f = 1.59 * (Wwf**0.302)
                e_f = 0.098 * (Wwf**0.467)
                print("Wwf: {:.3f} Kg" .format(Wwf))
                print("d_f: {:.3f} in" .format(d_f))
                print("e_f: {:.3f} in" .format(e_f))
                #Calculo diametro e espessura rodas trasseiras
                Wwt = (MTOW * dt)/nt
                d_t = 1.59 * (Wwt**0.302)
                e_t = 0.098 * (Wwt**0.467)
                print("Wwt: {:.3f} Kg" .format(Wwt))
                print("d_t: {:.3f} in" .format(d_t))
                print("e_t: {:.3f} in" .format(e_t))
                
            else:
                pop1 = False
            
    elif op is 2:
        MTOW = float(input('MTOW (kg): '))
        df = float(input('Distribuicao de peso do TP dianteiro (decimal): '))
        dt = float(input('Distribuicao de peso do TP traseiro (decimal): '))
        nf = float(input('Numero de rodas frontais: '))
        nt = float(input('Numero de rodas traseiras: '))
        pop1 = True
        
        MENU2 = """
        1 - Aviação
        2 - Business Twin
        3 - Transporte/Bombardeiro
        4- Aviao de caça
        """
        while pop1 == True:
            
            print(MENU2)
            op2 = int(input())
            if op2 is 1:
                #Calculo diametro e espessura rodas frontais
                Wwf = (MTOW * df)/nf
                d_f = 5.1 * (Wwf**0.349)
                e_f = 2.3 * (Wwf**0.312)
                print("Wwf: {:.3f} Kg" .format(Wwf))
                print("d_f: {:.3f} cm" .format(d_f))
                print("e_f: {:.3f} cm" .format(e_f))
                #Calculo diametro e espessura rodas trasseiras
                Wwt = (MTOW * dt)/nt
                d_t = 5.1 * (Wwt**0.349)
                e_t = 2.3 * (Wwt**0.312)
                print("Wwt: {:.3f} Kg" .format(Wwt))
                print("d_t: {:.3f} cm" .format(d_t))
                print("e_t: {:.3f} cm" .format(e_t))

            elif op2 is 2:
                #Calculo diametro e espessura rodas frontais
                Wwf = (MTOW * df)/nf
                d_f = 8.3 * (Wwf**0.251)
                e_f = 3.5 * (Wwf**0.216)
                print("Wwf: {:.3f} Kg" .format(Wwf))
                print("d_f: {:.3f} cm" .format(d_f))
                print("e_f: {:.3f} cm" .format(e_f))
                #Calculo diametro e espessura rodas trasseiras
                Wwt = (MTOW * dt)/nt
                d_t = 8.3 * (Wwt**0.251)
                e_t = 3.5* (Wwt**0.216)
                print("Wwt: {:.3f} Kg" .format(Wwt))
                print("d_t: {:.3f} cm" .format(d_t))
                print("e_t: {:.3f} cm" .format(e_t))

            elif op2 is 3:
                #Calculo diametro e espessura rodas frontais
                Wwf = (MTOW * df)/nf
                d_f = 5.3 * (Wwf**0.315)
                e_f = 0.39 * (Wwf**0.48)
                print("Wwf: {:.3f} Kg" .format(Wwf))
                print("d_f: {:.3f} cm" .format(d_f))
                print("e_f: {:.3f} cm" .format(e_f))
                #Calculo diametro e espessura rodas trasseiras
                Wwt = (MTOW * dt)/nt
                d_t = 5.3 * (Wwt**0.315)
                e_t = 0.39 * (Wwt**0.48)
                print("Wwt: {:.3f} Kg" .format(Wwt))
                print("d_t: {:.3f} cm" .format(d_t))
                print("e_t: {:.3f} cm" .format(e_t))
            elif op2 is 4:
                Wwf = (MTOW * df)/nf
                d_f = 5.1 * (Wwf**0.36)
                e_f = 0.302 * (Wwf**0.467)
                print("Wwf: {:.3f} Kg" .format(Wwf))
                print("d_f: {:.3f} cm" .format(d_f))
                print("e_f: {:.3f} cm" .format(e_f))
                #Calculo diametro e espessura rodas trasseiras
                Wwt = (MTOW * dt)/nt
                d_t = 5.1 * (Wwt**0.36)
                e_t = 0.302 * (Wwt**0.467)
                print("Wwt: {:.3f} Kg" .format(Wwt))
                print("d_t: {:.3f} cm" .format(d_t))
                print("e_t: {:.3f} cm" .format(e_t))

            else:
                pop1 = False
    
    elif op is 3:
        pop = False
    else:
        print("Entrada invalida")





    