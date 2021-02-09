import pygame
from GameUI import *
input=None
def matrix():		#Initializam board
    board=['#']*64
    for i in range(1,8,2):
        board[i]='w'
    for i in range(0,8,2):
        board[8+i]='w'
    for i in range(1,8,2):
        board[16+i]='w'
    for i in range(0,8,2):
        board[5*8+i]='b'
    for i in range(1,8,2):
        board[6*8+i]='b'
    for i in range(0,8,2):
        board[7*8+i]='b'
    return board
board=matrix()
def show(board):

    print(" ",end=" ")
    for i in range(8):
        print(i,end=" ")
    print("")
    for i in range(8):
        print(i,end=" ")
        for j in range(8):
            print(board[i*8+j],end=" ")
        print("")
board[8*0+4]='W'
board[8*3+5]='B'
board[8*5+5]='b'
okey =0
#afis()
def move(line,column,current_state):	#Metoda folosita pentru a face o mutare a jucatorului
    global input
    matrix=current_state.board_game.board
    current_state.ui.display.fill((0, 0, 0))
    current_state.ui.draw(current_state.board_game.board)
    current_state.ui.update()
    current_state.ui.clock.tick(30)
    #Functie pentru a muta dedicata jucatorului(in care poate alege ce mutare sa mute)
    for i in range(8):
        for j in range(8):
            print(matrix[8*i+j],end=" ")
        print(" ")
    valid_response=False	#Folosit pentru check daca jucatorul a putut efectua o mutare
    global okey #Variabila pentru a observa , in cazul mutarilor multiple , daca s-a putut efectua vreo mutare
    okey=0
    nr=0	#Variabila folosita pentru a verifica daca jucatorul a incercat deja toate mutarile
		#2 mutari valabile au piesele a si n , si 4 mutari A si N
    print(line,column)
    if matrix[line*8+column]=='b':	#piesa aleasa este neagra
        while not valid_response:
            if nr==2:		#Are posibile 2 mutari de facut , daca niciuna nu e valabila , at piesa e imutabila
                print("It seems like any movement isn't available .")
                if okey==1: #Daca , in momentul de fata ne aflam intr-o recursivitate , atunci jucatorul deja a mutat prin mutari multiple(okey=1),altfel
                            #Inseamna ca n-a putut efectua nicio mutare si returnam -1 , pentru a remuta
                    return 1
                else:
                    return -1
              #Crestem numarul de alegeri deja facute si imposibile de efectuat
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = current_state.ui.mapCoordToIndex(*pygame.mouse.get_pos())
                    nr += 1
                    if(pos[0]==line-1 and pos[1]==column-1) or (pos[0] == line - 2 and pos[1] == column - 2):
                        input=1
                    elif (pos[0]==line-1 and pos[1]==column+1) or (pos[0] == line - 2 and pos[1] == column + 2):
                        input=2
                    print(input)
                    choose=input #Alegem ce mutare vrem sa efectuam
                    if(choose)==1:  #Incercam sa mutam piesa la stanga sus
                        if not (line-1>=0 and column-1>=0):   #Verificam sa nu iesim din matrix
                            print("Impossible movement.Try another one.")
                        else:
                            if matrix[(line-1)*8+column-1]=='#': #Verificam disponibilitatea de mutare a piesei
                                matrix[line*8+column]='#'
                                if line-1>0:
                                    matrix[(line-1)*8+column-1]='b'
                                else:
                                    matrix[(line-1)*8+column-1]='B'
                                valid_response=True  #Daca mutarea s-a validat , atunci nu mai e nevoie sa reluam procesul de alegere a unei piese de mutat
                                okey=1  #Variabila okey a verificat ca cel putin o mutare este efectuata , iar in cazul recursivitatii avem instiintarea ca s-a putut efectua cel putin o mutare
                            elif matrix[(line-1)*8+column-1]=='w' or matrix[(line-1)*8+column-1]=='W':    #Jump conditions , verificam daca piesa pe care o putem prelua e a inamicului
                                if line-2>=0 and column-2>=0 and matrix[(line-2)*8+column-2]=='#': #Verificam daca ,sarind peste piesa putem ajunge intr-un loc valid
                                    matrix[(line-2)*8+column-2]='b'
                                    if line-2==0:
                                        matrix[(line-2)*8+column-2]='B'  #Daca am inaintat pana la final cu o piesa mica , o putem transforma in queen
                                    matrix[line*8+column]='#'
                                    matrix[(line-1)*8+column-1]='#'
                                    valid_response=True
                                    okey=1
                                    return move(line-2,column-2,current_state)  #Fiind o mutare jump , mai avem voie sa efectuam mutare
                                else:
                                    print("Impossible movement")
                            else:
                                print("Impossible movement.Try another one.")
                    elif choose==2: #La fel pentru o alegere de mutare la dreapta
                        if not (line-1>=0 and column+1<8):
                            print("Impossible movement.Try another one.")
                        else:
                            if matrix[(line-1)*8+column+1]=='#':
                                matrix[line*8+column]='#'
                                if line-1>0:
                                    matrix[(line-1)*8+column+1]='b'
                                else:
                                    matrix[(line-1)*8+column+1]='B'
                                valid_response=True
                                okey=1
                            elif matrix[(line-1)*8+column+1]=='w' or matrix[(line-1)*8+column+1]=='W':
                                if line-2>=0 and column+2<8 and matrix[(line-2)*8+column+2]=='#':
                                    matrix[(line-2)*8+column+2]='b'
                                    if line-2==0:
                                        matrix[(line-2)*8+column+2]='B'
                                    matrix[line*8+column]='#'
                                    matrix[(line-1)*8+column+1]='#'
                                    valid_response=True
                                    okey=1
                                    return move(line-2,column+2,current_state)
                                else:
                                    print("Impossible movement")
                            else:
                                print("Impossible movement.Try another one.")

    if matrix[line*8+column]=='w':   #Procedam aidoma in cazul in care jucam cu albul,piesa inaintand in directia opusa piesei n si avand obiectiv sa preluam piese negre
        print(line,column)
        while not valid_response:

            if nr==2:
                print("It seems like any movement isn't available .")
                if okey==1:
                    return 1
                else:
                    return -1
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = current_state.ui.mapCoordToIndex(*pygame.mouse.get_pos())
                    nr += 1
                    if (pos[0] == line + 1 and pos[1] == column - 1) or (pos[0] == line + 2 and pos[1] == column - 2):
                        input = 1
                    elif (pos[0] == line + 1 and pos[1] == column + 1) or (pos[0] == line + 2 and pos[1] == column +2):
                        input = 2
                    choose=input
                    if(choose)==1:
                        if not (line+1<8 and column-1>=0):
                            print("Impossible movement.Try another one.")
                        else:
                            if matrix[(line+1)*8+column-1]=='#':
                                matrix[line*8+column]='#'
                                if line+1<7:
                                    matrix[(line+1)*8+column-1]='w'
                                else:
                                    matrix[(line+1)*8+column-1]='W'
                                valid_response=True
                                okey=1
                            elif matrix[(line+1)*8+column-1]=='b' or matrix[(line+1)*8+column-1]=='B':
                                if line+2<8 and column-2>=0 and matrix[(line+2)*8+column-2]=='#':
                                    matrix[(line+2)*8+column-2]='w'
                                    if line+2==7:
                                        matrix[(line+2)*8+column-2]='W'
                                    matrix[line*8+column]='#'
                                    matrix[(line+1)*8+column-1]='#'
                                    valid_response=True
                                    okey=1
                                    return move(line+2,column-2,current_state)
                                else:
                                    print("Impossible movement")
                            else:
                                print("Impossible movement.Try another one.")
                    elif choose==2:
                        if not (line+1<8 and column+1<8):
                            print("Impossible movement.Try another one.")
                        else:
                            if matrix[(line+1)*8+column+1]=='#':
                                matrix[line*8+column]='#'
                                if line+1<7:
                                    matrix[(line+1)*8+column+1]='w'
                                else:
                                    matrix[(line+1)*8+column+1]='W'
                                valid_response=True
                                okey=1
                            elif matrix[(line+1)*8+column+1]=='b' or matrix[(line+1)*8+column+1]=='B':
                                if line+2<=7 and column+2<8 and matrix[(line+2)*8+column+2]=='#':
                                    matrix[(line+2)*8+column+2]='w'
                                    if line+2==7:
                                        matrix[(line+2)*8+column+2]='W'
                                    matrix[line*8+column]='#'
                                    matrix[(line+1)*8+column+1]='#'
                                    valid_response=True
                                    okey=1
                                    return move(line+2,column+2,current_state)
                                else:
                                    print("Impossible movement")
                            else:
                                print("Impossible movement.Try another one.")
                    if valid_response==False:
                        print("Try another move")
    elif matrix[line*8+column]=='W': #Piesa Queen
        while not valid_response:
            if nr==4:   #Are 4 modalitati de mutare , deci 4 posibilitati de a verifica daca piesa e mutabila , se incearca fiecare mutare posibila
                print("It seems like any movement isn't available .")
                if okey==1:
                    return 1
                else:
                    return -1
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = current_state.ui.mapCoordToIndex(*pygame.mouse.get_pos())
                    nr += 1
                    if (pos[0] == line - 1 and pos[1] == column - 1) or (pos[0] == line -2 and pos[1] == column - 2):
                        input = 1
                    elif (pos[0] == line - 1 and pos[1] == column + 1) or (pos[0] == line - 2 and pos[1] == column + 2):
                        input = 2
                    elif (pos[0] == line + 1 and pos[1] == column - 1) or (pos[0] == line + 2 and pos[1] == column - 2):
                        input = 3
                    elif (pos[0] == line + 1 and pos[1] == column + 1) or (pos[0] == line + 2 and pos[1] == column + 2):
                        input = 4
                    choose=input
                    #choose=int(input("1 stanga sus 2 dreapta sus 3 stanga jos 4 dreapta jos"))  #Piesa se muta aidoma pieselor a si n combinate
                    if(choose)==1:
                        if not (line-1>=0 and column-1>=0):
                            print("Impossible movement.Try another one.")
                        else:
                            if matrix[(line-1)*8+column-1]=='#':
                                matrix[line*8+column]='#'
                                matrix[(line-1)*8+column-1]='W'
                                valid_response=True
                                okey=1
                            elif matrix[(line-1)*8+column-1]=='b' or matrix[(line-1)*8+column-1]=='B':
                                if line-2>=0 and column-2>=0 and matrix[(line-2)*8+column-2]=='#':
                                    matrix[(line-2)*8+column-2]='W'
                                    matrix[line*8+column]='#'
                                    matrix[(line-1)*8+column-1]='#'
                                    okey=1
                                    valid_response=True
                                    #In cazul in care o piesa a facut jump , ea va fi capabila sa faca o inca mutare
                                    return move(line-2,column-2,current_state)
                                else:
                                    print("Impossible movement")
                            else:
                                print("Impossible movement.Try another one.")
                    elif choose==2:
                        if not (line-1>=0 and column+1<8):
                            print("Impossible movement.Try another one.")
                        else:
                            if matrix[(line-1)*8+column+1]=='#':
                                matrix[(line)*8+column]='#'
                                matrix[(line-1)*8+column+1]='W'
                                valid_response=True
                                okey=1
                            elif matrix[(line-1)*8+column+1]=='b' or matrix[(line-1)*8+column+1]=='B':
                                if line-2>=0 and column+2<8 and matrix[(line-2)*8+column+2]=='#':
                                    matrix[(line-2)*8+column+2]='W'
                                    matrix[line*8+column]='#'
                                    matrix[(line-1)*8+column+1]='#'
                                    valid_response=True
                                    okey=1
                                    return move(line-2,column+2,current_state)
                                else:
                                    print("Impossible movement")
                            else:
                                print("Impossible movement.Try another one.")
                    elif(choose)==3:
                        if not (line+1<8 and column-1>=0):
                            print("Impossible movement.Try another one.")
                        else:
                            if matrix[(line+1)*8+column-1]=='#':
                                matrix[line*8+column]='#'
                                matrix[(line+1)*8+column-1]='W'
                                valid_response=True
                                okey=1
                            elif matrix[(line+1)*8+column-1]=='b' or matrix[(line+1)*8+column-1]=='B':
                                if line+2<8 and column-2>=0 and matrix[(line+2)*8+column-2]=='#':
                                    matrix[(line+2)*8+column-2]='W'
                                    matrix[line*8+column]='#'
                                    matrix[(line+1)*8+column-1]='#'
                                    valid_response=True
                                    okey=1
                                    return move(line+2,column-2,current_state)
                                else:
                                    print("Impossible movement")
                            else:
                                print("Impossible movement.Try another one.")
                    elif choose==4:
                        if not (line+1<8 and column+1<8):
                            print("Impossible movement.Try another one.")
                        else:
                            if matrix[(line+1)*8+column+1]=='#':
                                matrix[line*8+column]='#'
                                matrix[(line+1)*8+column+1]='W'
                                valid_response=True
                                okey=1
                            elif matrix[(line+1)*8+column+1]=='b' or matrix[(line+1)*8+column+1]=='B':
                                if line+2<=7 and column+2<8 and matrix[(line+2)*8+column+2]=='#':
                                    matrix[(line+2)*8+column+2]='W'
                                    matrix[line*8+column]='#'
                                    matrix[(line+1)*8+column+1]='#'
                                    valid_response=True
                                    okey=1
                                    return move(line+2,column+2,current_state)
                                else:
                                    print("Impossible movement")
                            else:
                                print("Impossible movement.Try another one.")
    elif matrix[line*8+column]=='B': #Acelas principiu ca la piesa A , avand obiectiv sa preluam piese albe
        while not valid_response:
            if nr==4:
                print("It seems like any movement isn't available .")
                if okey==1:
                    return 1
                else:
                    return -1
            for event in pygame.event.get():
                pos = current_state.ui.mapCoordToIndex(*pygame.mouse.get_pos())
                if event.type == pygame.MOUSEBUTTONUP:
                    if (pos[0] == line - 1 and pos[1] == column - 1) or (pos[0] == line - 2 and pos[1] == column - 2):
                        input = 1
                    elif (pos[0] == line - 1 and pos[1] == column + 1) or (pos[0] == line - 2 and pos[1] == column + 2):
                        input = 2
                    elif (pos[0] == line + 1 and pos[1] == column - 1) or (pos[0] == line + 2 and pos[1] == column - 2):
                        input = 3
                    elif (pos[0] == line + 1 and pos[1] == column + 1) or (pos[0] == line + 2 and pos[1] == column + 2):
                        input = 4
                    choose=input
                    #choose=int(input("1 stanga sus 2 dreapta sus 3 stanga jos 4 dreapta jos"))
                    if(choose)==1:
                        if not (line-1>=0 and column-1>=0):
                            print("Impossible movement.Try another one.")
                        else:
                            if matrix[(line-1)*8+column-1]=='#':
                                matrix[line*8+column]='#'
                                matrix[(line-1)*8+column-1]='B'
                                valid_response=True
                                okey=1
                            elif matrix[(line-1)*8+column-1]=='w' or matrix[(line-1)*8+column-1]=='W':
                                if line-2>=0 and column-2>=0 and matrix[(line-2)*8+column-2]=='#':
                                    matrix[(line-2)*8+column-2]='B'
                                    matrix[line*8+column]='#'
                                    matrix[(line-1)*8+column-1]='#'
                                    okey=1
                                    valid_response=True
                                    return move(line-2,column-2,current_state)
                                else:
                                    print("Impossible movement")
                            else:
                                print("Impossible movement.Try another one.")
                    elif choose==2:
                        if not (line-1>=0 and column+1<8):
                            print("Impossible movement.Try another one.")
                        else:
                            if matrix[(line-1)*8+column+1]=='#':
                                matrix[(line)*8+column]='#'
                                matrix[(line-1)*8+column+1]='B'
                                valid_response=True
                                okey=1
                            elif matrix[(line-1)*8+column+1]=='w' or matrix[(line-1)*8+column+1]=='W':
                                if line-2>=0 and column+2<8 and matrix[(line-2)*8+column+2]=='#':
                                    matrix[(line-2)*8+column+2]='B'
                                    matrix[line*8+column]='#'
                                    matrix[(line-1)*8+column+1]='#'
                                    valid_response=True
                                    okey=1
                                    return move(line-2,column+2,current_state)
                                else:
                                    print("Impossible movement")
                            else:
                                print("Impossible movement.Try another one.")
                    elif(choose)==3:
                        if not (line+1<8 and column-1>=0):
                            print("Impossible movement.Try another one.")
                        else:
                            if matrix[(line+1)*8+column-1]=='#':
                                matrix[line*8+column]='#'
                                matrix[(line+1)*8+column-1]='B'
                                valid_response=True
                                okey=1
                            elif matrix[(line+1)*8+column-1]=='w' or matrix[(line+1)*8+column-1]=='W':
                                if line+2<8 and column-2>=0 and matrix[(line+2)*8+column-2]=='#':
                                    matrix[(line+2)*8+column-2]='B'
                                    matrix[line*8+column]='#'
                                    matrix[(line+1)*8+column-1]='#'
                                    valid_response=True
                                    okey=1
                                    return move(line+2,column-2,current_state)
                                else:
                                    print("Impossible movement")
                            else:
                                print("Impossible movement.Try another one.")
                    elif choose==4:
                        if not (line+1<8 and column+1<8):
                            print("Impossible movement.Try another one.")
                        else:
                            if matrix[(line+1)*8+column+1]=='#':
                                matrix[line*8+column]='#'
                                matrix[(line+1)*8+column+1]='B'
                                #Mutare normala
                                valid_response=True
                                okey=1
                            elif matrix[(line+1)*8+column+1]=='w' or matrix[(line+1)*8+column+1]=='W':
                                if line+2<=7 and column+2<8 and matrix[(line+2)*8+column+2]=='#':
                                    matrix[(line+2)*8+column+2]='B'
                                    matrix[line*8+column]='#'
                                    matrix[(line+1)*8+column+1]='#'
                                    valid_response=True
                                    okey=1
                                    #Mutare jump , mai pot face miscari
                                    return move(line+2,column+2,current_state)
                                else:
                                    print("Impossible movement")
                            else:
                                print("Impossible movement.Try another one.")
#print(move(0,4,board))




