import time
import copy
import helper_file
import pygame
import GameUI


class Joc:
    NR_COLUMN = 8
    NR_LINII = 8
    NR_CONNECT = 4
    SIMBOLURI_JUC = ['w', 'b']
    JMIN = None
    JMAX = None
    GOL = '#'

    def __init__(self, tabla=None):
        self.board = tabla or copy.deepcopy(helper_file.matrice())

        # print(Test.boardice())

    def afis_daca_final(self):
        # A castigat playerul cu cele mai multe piese pe tabla
        nra = self.board.count('A')
        nrn = self.board.count('N')
        if (nra > nrn):
            print("Alb a castigat")
        if (nrn > nra):
            print("Negru a castigat")
        else:
            print("Remiza")

    def verific_final(self, line, column):
        # In aceasta functie verific daca piesa de la coordonata line,column este mutabila sau nu
        raspuns_valid = False
        okey = 0
        if self.board[line * 8 + column] == 'b':
            if not (line - 1 >= 0 and column - 1 >= 0):
                no_action = 1
            else:
                if self.board[(line - 1) * 8 + column - 1] == '#':
                    raspuns_valid = True
                    okey = 1
                elif self.board[(line - 1) * 8 + column - 1] == 'w' or self.board[
                    (line - 1) * 8 + column - 1] == 'A':
                    if line - 2 >= 0 and column - 2 >= 0 and self.board[(line - 2) * 8 + column - 2] == '#':
                        raspuns_valid = True
                        okey = 1
                        # return muta(line-2,column-2,player)
                    else:
                        no_action = 1
            if not (line - 1 >= 0 and column + 1 < 8):
                no_action = 1
            else:
                if self.board[(line - 1) * 8 + column + 1] == '#':
                    raspuns_valid = True
                    okey = 1
                elif self.board[(line - 1) * 8 + column + 1] == 'w' or self.board[
                    (line - 1) * 8 + column + 1] == 'A':
                    if line - 2 >= 0 and column + 2 < 8 and self.board[(line - 2) * 8 + column + 2] == '#':
                        raspuns_valid = True
                        okey = 1
                        # return muta(line-2,column+2,player)
                    else:
                        no_action = 1

        if self.board[line * 8 + column] == 'w':
            if not (line + 1 < 8 and column - 1 >= 0):
                no_action = 1
            else:
                if self.board[(line + 1) * 8 + column - 1] == '#':
                    raspuns_valid = True
                    okey = 1
                elif self.board[(line + 1) * 8 + column - 1] == 'b' or self.board[
                    (line + 1) * 8 + column - 1] == 'N':
                    if line + 2 < 8 and column - 2 >= 0 and self.board[(line + 2) * 8 + column - 2] == '#':
                        raspuns_valid = True
                        okey = 1
                        # return muta(line+2,column-2,player)
            if not (line + 1 < 8 and column + 1 < 8):
                no_action = 1
            else:
                if self.board[(line + 1) * 8 + column + 1] == '#':

                    raspuns_valid = True
                    okey = 1
                elif self.board[(line + 1) * 8 + column + 1] == 'b' or self.board[
                    (line + 1) * 8 + column + 1] == 'N':
                    if line + 2 <= 7 and column + 2 < 8 and self.board[(line + 2) * 8 + column + 2] == '#':

                        raspuns_valid = True
                        okey = 1
                    else:
                        no_action = 1
        elif self.board[line * 8 + column] == 'A':
            if not (line - 1 >= 0 and column - 1 >= 0):
                no_action = 1
            else:
                if self.board[(line - 1) * 8 + column - 1] == '#':

                    raspuns_valid = True
                    okey = 1
                elif self.board[(line - 1) * 8 + column - 1] == 'b' or self.board[
                    (line - 1) * 8 + column - 1] == 'N':
                    if line - 2 >= 0 and column - 2 >= 0 and self.board[(line - 2) * 8 + column - 2] == '#':

                        okey = 1
                        raspuns_valid = True
                        # return muta(line-2,column-2,player)
                    else:
                        no_action = 1
            if not (line - 1 >= 0 and column + 1 < 8):
                no_action = 1
            else:
                if self.board[(line - 1) * 8 + column + 1] == '#':

                    raspuns_valid = True
                    okey = 1
                elif self.board[(line - 1) * 8 + column + 1] == 'b' or self.board[
                    (line - 1) * 8 + column + 1] == 'N':
                    if line - 2 >= 0 and column + 2 < 8 and self.board[(line - 2) * 8 + column + 2] == '#':

                        raspuns_valid = True
                        okey = 1
                        # return muta(line-2,column+2,player)
                    else:
                        no_action = 1
            if not (line + 1 < 8 and column - 1 >= 0):
                no_action = 1
            else:
                if self.board[(line + 1) * 8 + column - 1] == '#':

                    raspuns_valid = True
                    okey = 1
                elif self.board[(line + 1) * 8 + column - 1] == 'b' or self.board[
                    (line + 1) * 8 + column - 1] == 'N':
                    if line + 2 < 8 and column - 2 >= 0 and self.board[(line + 2) * 8 + column - 2] == '#':

                        raspuns_valid = True
                        okey = 1
                        # return muta(line+2,column-2,player)
                    else:
                        no_action = 1
            if not (line + 1 < 8 and column + 1 < 8):
                no_action = 1
            else:
                if self.board[(line + 1) * 8 + column + 1] == '#':

                    raspuns_valid = True
                    okey = 1
                elif self.board[(line + 1) * 8 + column + 1] == 'b' or self.board[
                    (line + 1) * 8 + column + 1] == 'N':
                    if line + 2 <= 7 and column + 2 < 8 and self.board[(line + 2) * 8 + column + 2] == '#':

                        raspuns_valid = True
                        okey = 1
                        # return muta(line+2,column+2,player)
                    else:
                        no_action = 1
        elif self.board[line * 8 + column] == 'N':
            if not (line - 1 >= 0 and column - 1 >= 0):
                no_action = 1
            else:
                if self.board[(line - 1) * 8 + column - 1] == '#':

                    raspuns_valid = True
                    okey = 1
                elif self.board[(line - 1) * 8 + column - 1] == 'w' or self.board[
                    (line - 1) * 8 + column - 1] == 'A':
                    if line - 2 >= 0 and column - 2 >= 0 and self.board[(line - 2) * 8 + column - 2] == '#':

                        okey = 1
                        raspuns_valid = True
                    else:
                        no_action = 1
            if not (line - 1 >= 0 and column + 1 < 8):
                no_action = 1
            else:
                if self.board[(line - 1) * 8 + column + 1] == '#':

                    raspuns_valid = True
                    okey = 1
                elif self.board[(line - 1) * 8 + column + 1] == 'w' or self.board[
                    (line - 1) * 8 + column + 1] == 'A':
                    if line - 2 >= 0 and column + 2 < 8 and self.board[(line - 2) * 8 + column + 2] == '#':

                        raspuns_valid = True
                        okey = 1
                    else:
                        no_action = 1
            if not (line + 1 < 8 and column - 1 >= 0):
                no_action = 1
            else:
                if self.board[(line + 1) * 8 + column - 1] == '#':

                    raspuns_valid = True
                    okey = 1
                elif self.board[(line + 1) * 8 + column - 1] == 'w' or self.board[
                    (line + 1) * 8 + column - 1] == 'A':
                    if line + 2 < 8 and column - 2 >= 0 and self.board[(line + 2) * 8 + column - 2] == '#':

                        raspuns_valid = True
                        okey = 1
                    else:
                        no_action = 1
            if not (line + 1 < 8 and column + 1 < 8):
                no_action = 1
            else:
                if self.board[(line + 1) * 8 + column + 1] == '#':

                    raspuns_valid = True
                    okey = 1
                elif self.board[(line + 1) * 8 + column + 1] == 'w' or self.board[
                    (line + 1) * 8 + column + 1] == 'A':
                    if line + 2 <= 7 and column + 2 < 8 and self.board[(line + 2) * 8 + column + 2] == '#':

                        raspuns_valid = True
                        okey = 1
                    else:
                        no_action = 1
        return raspuns_valid

    def final(self, player):
        # Verific daca mai e posibila cel putin o mutare , pentru playerul current
        for i in range(self.NR_LINII):
            for j in range(self.NR_COLUMN):
                if self.board[i * self.NR_COLUMN + j] == player.lower() or self.board[
                    i * self.NR_COLUMN + j] == player.upper():
                    # Aici verific toate posibilitatile unei piese ce apartine de player pentru a o muta
                    # Daca cel putin una e mutabila , playerul mai poate muta , deci n-a pierdut
                    if self.verific_final(i, j) == True:
                        return 0
        return 1

    l_mutari = []

    def mutari(self, line, column, player, boardice):
        # Aici calculatorul calculeaza toate posibilitatile de mutare(l_mutari l-am scos inafara functiei)
        # Pentru a updata si atunci cand piesul are multiple posibilitati de mutare
        # in player se pasteeaza playerul current iar boardice ->boardicea currenta pentru o anumita mutare
        raspuns_valid = False
        aux = copy.deepcopy(boardice)
        if boardice[line * 8 + column] == 'b':
            if not (line - 1 >= 0 and column - 1 >= 0):  # Verific ca prin mutare sa nu ies din boardice
                no_action = 1
            else:
                if boardice[(line - 1) * 8 + column - 1] == '#':  # Vad daca piesa se paote muta la stanga
                    aux[line * 8 + column] = '#'
                    if line - 1 > 0:  # Daca inca n-am ajuns la ultima line sa transformam piesa in N , continuam cu aceeasi piesa
                        aux[(line - 1) * 8 + column - 1] = 'b'
                    else:
                        aux[(line - 1) * 8 + column - 1] = 'N'
                        # Se preiau toate mutarile posibile
                    self.l_mutari.append(Joc(aux))
                elif boardice[(line - 1) * 8 + column - 1] == 'w' or self.board[(line - 1) * 8 + column - 1] == 'A':
                    if line - 2 >= 0 and column - 2 >= 0 and aux[(line - 2) * 8 + column - 2] == '#':
                        aux[(line - 2) * 8 + column - 2] = 'b'
                        if line - 2 == 0:
                            aux[(line - 2) * 8 + column - 2] = 'N'
                        aux[line * 8 + column] = '#'
                        aux[(line - 1) * 8 + column - 1] = '#'
                        self.l_mutari.append(Joc(aux))
                        # Pentru mutarile multiple , se iau toate cazurile
                        # Parcurg recursiv la mutarile jumps pana nu mai pot efectua jump-uri
                        # Si salvez fiecare configuratie in parte
                        self.mutari(line - 2, column - 2, player, aux)
                    else:
                        no_action = 1
            aux = copy.deepcopy(boardice)
            if not (line - 1 >= 0 and column + 1 < 8):
                no_action = 1
            else:
                if boardice[(
                                    line - 1) * 8 + column + 1] == '#':  # Vad daca piesa se paote muta la dreapta,acelas mecanism ca la mutarea piesei pe stanga
                    aux[line * 8 + column] = '#'
                    if line - 1 > 0:
                        aux[(line - 1) * 8 + column + 1] = 'b'
                    else:
                        aux[(line - 1) * 8 + column + 1] = 'N'
                    self.l_mutari.append(Joc(aux))
                elif boardice[(line - 1) * 8 + column + 1] == 'w' or self.board[(line - 1) * 8 + column + 1] == 'A':
                    if line - 2 >= 0 and column + 2 < 8 and self.board[(line - 2) * 8 + column + 2] == '#':
                        aux[(line - 2) * 8 + column + 2] = 'b'
                        if line - 2 == 0:
                            aux[(line - 2) * 8 + column + 2] = 'N'
                        aux[line * 8 + column] = '#'
                        aux[(line - 1) * 8 + column + 1] = '#'
                        self.l_mutari.append(Joc(aux))
                        self.mutari(line - 2, column + 2, player, aux)
                    else:
                        no_action = 1

        if boardice[
            line * 8 + column] == 'w':  # Acelas mecanism dar pentru alb , cand doreste sa inainteze stanga pe boardice
            if not (line + 1 < 8 and column - 1 >= 0):
                no_action = 1
            else:
                if boardice[(line + 1) * 8 + column - 1] == '#':
                    aux[line * 8 + column] = '#'
                    if line + 1 < 7:
                        aux[(line + 1) * 8 + column - 1] = 'w'
                    else:
                        aux[(line + 1) * 8 + column - 1] = 'A'
                    self.l_mutari.append(Joc(aux))
                elif boardice[(line + 1) * 8 + column - 1] == 'b' or self.board[(line + 1) * 8 + column - 1] == 'N':
                    if line + 2 < 8 and column - 2 >= 0 and self.board[(line + 2) * 8 + column - 2] == '#':
                        aux[(line + 2) * 8 + column - 2] = 'w'
                        if line + 2 == 7:
                            aux[(line + 2) * 8 + column - 2] = 'A'
                        aux[line * 8 + column] = '#'
                        aux[(line + 1) * 8 + column - 1] = '#'
                        self.l_mutari.append(Joc(aux))
                        self.mutari(line + 2, column - 2, player, aux)
            aux = copy.deepcopy(boardice)
            if not (
                    line + 1 < 8 and column + 1 < 8):  # Acelas mecanism pentru alb , cand doreste sa inainteze stanga pe boardice
                no_action = 1
            else:
                if boardice[(line + 1) * 8 + column + 1] == '#':
                    aux[line * 8 + column] = '#'
                    if line + 1 < 7:
                        aux[(line + 1) * 8 + column + 1] = 'w'
                    else:
                        aux[(line + 1) * 8 + column + 1] = 'A'
                    self.l_mutari.append(Joc(aux))
                elif boardice[(line + 1) * 8 + column + 1] == 'b' or self.board[(line + 1) * 8 + column + 1] == 'N':
                    if line + 2 <= 7 and column + 2 < 8 and self.board[(line + 2) * 8 + column + 2] == '#':
                        aux[(line + 2) * 8 + column + 2] = 'w'
                        if line + 2 == 7:
                            aux[(line + 2) * 8 + column + 2] = 'A'
                        aux[line * 8 + column] = '#'
                        aux[(line + 1) * 8 + column + 1] = '#'
                        self.l_mutari.append(Joc(aux))
                        self.mutari(line + 2, column + 2, player, aux)
                    else:
                        no_action = 1
        elif boardice[
            line * 8 + column] == 'A':  # Acelas mecanism pentru alb piesa A mare , avand posibilitatea sa se deplaseze si sus si jos stanga/dreapta
            if not (line - 1 >= 0 and column - 1 >= 0):  # Cazul unde piesa doreste sa se deplaseze stanga sus
                no_action = 1
            else:
                if boardice[(line - 1) * 8 + column - 1] == '#':
                    aux[line * 8 + column] = '#'
                    aux[(line - 1) * 8 + column - 1] = 'A'
                    self.l_mutari.append(Joc(aux))
                elif boardice[(line - 1) * 8 + column - 1] == 'b' or self.board[(line - 1) * 8 + column - 1] == 'N':
                    if line - 2 >= 0 and column - 2 >= 0 and aux[(line - 2) * 8 + column - 2] == '#':
                        aux[(line - 2) * 8 + column - 2] = 'A'
                        aux[line * 8 + column] = '#'
                        aux[(line - 1) * 8 + column - 1] = '#'
                        okey = 1
                        raspuns_valid = True
                        self.l_mutari.append(Joc(aux))
                        self.mutari(line - 2, column - 2, player, aux)
                    else:
                        no_action = 1
            aux = copy.deepcopy(boardice)
            if not (line - 1 >= 0 and column + 1 < 8):  # Cazul unde piesa doreste sa se deplaseze dreapta sus
                no_action = 1
            else:
                if boardice[(line - 1) * 8 + column + 1] == '#':
                    aux[(line) * 8 + column] = '#'
                    aux[(line - 1) * 8 + column + 1] = 'A'
                    self.l_mutari.append(Joc(aux))
                elif boardice[(line - 1) * 8 + column + 1] == 'b' or self.board[(line - 1) * 8 + column + 1] == 'N':
                    if line - 2 >= 0 and column + 2 < 8 and self.board[(line - 2) * 8 + column + 2] == '#':
                        aux[(line - 2) * 8 + column + 2] = 'A'
                        aux[line * 8 + column] = '#'
                        aux[(line - 1) * 8 + column + 1] = '#'
                        self.l_mutari.append(Joc(aux))
                        self.mutari(line - 2, column + 2, player, boardice)
                    else:
                        no_action = 1
            aux = copy.deepcopy(boardice)
            if not (line + 1 < 8 and column - 1 >= 0):  # Cazul unde piesa doreste sa se deplaseze stanga jos
                no_action = 1
            else:
                if boardice[(line + 1) * 8 + column - 1] == '#':
                    aux[line * 8 + column] = '#'
                    aux[(line + 1) * 8 + column - 1] = 'A'
                    self.l_mutari.append(Joc(aux))
                elif boardice[(line + 1) * 8 + column - 1] == 'b' or self.board[(line + 1) * 8 + column - 1] == 'N':
                    if line + 2 < 8 and column - 2 >= 0 and self.board[(line + 2) * 8 + column - 2] == '#':
                        aux[(line + 2) * 8 + column - 2] = 'A'
                        aux[line * 8 + column] = '#'
                        aux[(line + 1) * 8 + column - 1] = '#'
                        self.l_mutari.append(Joc(aux))
                        self.mutari(line + 2, column - 2, player, aux)
                    else:
                        no_action = 1
            aux = copy.deepcopy(boardice)
            if not (line + 1 < 8 and column + 1 < 8):  # Cazul unde piesa doreste sa se deplaseze dreapta jos
                no_action = 1
            else:
                if boardice[(line + 1) * 8 + column + 1] == '#':
                    aux[line * 8 + column] = '#'
                    aux[(line + 1) * 8 + column + 1] = 'A'
                    self.l_mutari.append(Joc(aux))
                elif boardice[(line + 1) * 8 + column + 1] == 'b' or self.board[(line + 1) * 8 + column + 1] == 'N':
                    if line + 2 <= 7 and column + 2 < 8 and self.board[(line + 2) * 8 + column + 2] == '#':
                        aux[(line + 2) * 8 + column + 2] = 'A'
                        aux[line * 8 + column] = '#'
                        aux[(line + 1) * 8 + column + 1] = '#'
                        self.l_mutari.append(Joc(aux))
                        self.mutari(line + 2, column + 2, player, aux)
                    else:
                        no_action = 1
        elif boardice[line * 8 + column] == 'N':  # Acelas mecanism ca la piesa A
            if not (line - 1 >= 0 and column - 1 >= 0):
                no_action = 1
            else:
                if boardice[(line - 1) * 8 + column - 1] == '#':
                    aux[line * 8 + column] = '#'
                    aux[(line - 1) * 8 + column - 1] = 'N'
                    self.l_mutari.append(Joc(aux))
                elif boardice[(line - 1) * 8 + column - 1] == 'w' or self.board[(line - 1) * 8 + column - 1] == 'A':
                    if line - 2 >= 0 and column - 2 >= 0 and aux[(line - 2) * 8 + column - 2] == '#':
                        aux[(line - 2) * 8 + column - 2] = 'N'
                        aux[line * 8 + column] = '#'
                        aux[(line - 1) * 8 + column - 1] = '#'
                        okey = 1
                        raspuns_valid = True
                        self.l_mutari.append(Joc(aux))
                        self.mutari(line - 2, column - 2, player, aux)
                    else:
                        no_action = 1
            aux = copy.deepcopy(boardice)
            if not (line - 1 >= 0 and column + 1 < 8):
                no_action = 1
            else:
                if boardice[(line - 1) * 8 + column + 1] == '#':
                    aux[(line - 1) * 8 + column + 1] = 'N'
                    aux[(line) * 8 + column] = '#'
                    self.l_mutari.append(Joc(aux))
                elif boardice[(line - 1) * 8 + column + 1] == 'w' or self.board[(line - 1) * 8 + column + 1] == 'A':
                    if line - 2 >= 0 and column + 2 < 8 and self.board[(line - 2) * 8 + column + 2] == '#':
                        aux[(line - 2) * 8 + column + 2] = 'N'
                        aux[line * 8 + column] = '#'
                        aux[(line - 1) * 8 + column + 1] = '#'
                        self.l_mutari.append(Joc(aux))
                        self.mutari(line - 2, column + 2, player, aux)
                    else:
                        no_action = 1
            aux = copy.deepcopy(boardice)
            if not (line + 1 < 8 and column - 1 >= 0):
                no_action = 1
            else:
                if boardice[(line + 1) * 8 + column - 1] == '#':
                    aux[line * 8 + column] = '#'
                    aux[(line + 1) * 8 + column - 1] = 'N'
                    self.l_mutari.append(Joc(aux))
                elif boardice[(line + 1) * 8 + column - 1] == 'w' or self.board[(line + 1) * 8 + column - 1] == 'A':
                    if line + 2 < 8 and column - 2 >= 0 and self.board[(line + 2) * 8 + column - 2] == '#':
                        aux[(line + 2) * 8 + column - 2] = 'N'
                        aux[line * 8 + column] = '#'
                        aux[(line + 1) * 8 + column - 1] = '#'
                        self.l_mutari.append(Joc(aux))
                        self.mutari(line + 2, column - 2, player, aux)
                    else:
                        no_action = 1
            aux = copy.deepcopy(boardice)
            if not (line + 1 < 8 and column + 1 < 8):
                no_action = 1
            else:
                if boardice[(line + 1) * 8 + column + 1] == '#':
                    aux[line * 8 + column] = '#'
                    aux[(line + 1) * 8 + column + 1] = 'N'
                    self.l_mutari.append(Joc(aux))
                elif boardice[(line + 1) * 8 + column + 1] == 'w' or self.board[(line + 1) * 8 + column + 1] == 'A':
                    if line + 2 <= 7 and column + 2 < 8 and self.board[(line + 2) * 8 + column + 2] == '#':
                        aux[(line + 2) * 8 + column + 2] = 'N'
                        aux[line * 8 + column] = '#'
                        aux[(line + 1) * 8 + column + 1] = '#'
                        self.l_mutari.append(Joc(aux))
                        self.mutari(line + 2, column + 2, player, aux)
                    else:
                        no_action = 1

    def fct_euristica(self):
        global choice
        if choice == 1:
            return self.board.count(self.JMAX) - self.board.count(self.JMIN)
        else:
            return self.board.count(self.JMAX) - self.board.count(self.JMIN) + self.board.count(
                self.JMAX.upper()) - self.board.count(self.JMIN.upper())  # Bonus daca ai piese Queen

    def estimate_score(self, player, adancime):
        # Daca s-a terminat jocul pentru minim , ins ca e cel mai bun scor(max a castigat) , altfel viceversa
        t_final = self.final(player)
        if t_final == 1 and Joc.JMIN == player:
            return (-999 - adancime)
        elif t_final == 1 and Joc.JMAX == player:
            return (999 + adancime)
        elif t_final == 'remiza':
            return 0
        else:
            return self.fct_euristica()

    def __str__(self):
        sir = '  '
        for nr_col in range(self.NR_COLUMN):
            sir += str(nr_col) + ' '
        sir += '\n'

        for lin in range(self.NR_LINII):
            k = lin * self.NR_COLUMN
            sir += (str(lin) + " " + " ".join([str(x) for x in self.board[k: k + self.NR_COLUMN]]) + "\n")
        # Afisez boardicea , prima line/column semnifica coordonatele carteziene , pentru a identifica ce piesa dorim sa mutam
        return sir


class Stare:
    """
    Clasa folosita de algoritmii minimax si alpha-beta
    Are ca proprietate tabla de joc
    Functioneaza cu conditia ca in cadrul clasei Joc sa fie definiti JMIN si JMAX (cei doi playeri posibili)
    De asemenea cere ca in clasa Joc sa fie definita si o metoda numita mutari() care ofera lista cu
    configuratiile posibile in urma mutarii unui player
    """

    ADANCIME_MAX = None

    def init(self):

        self.ui.init_window()
        self.ui.draw(self.tabla_joc.board)
        self.ui.update()

    def __init__(self, tabla_joc, j_current, adancime, parinte=None, scor=None):
        self.tabla_joc = tabla_joc
        self.j_current = j_current
        self.ui = GameUI.GameUI(background_color=(48, 25, 52), border_color=(120, 24, 74),
                                black_cell_color=(48, 25, 52), white_cell_color=(120, 24, 74), border_size=1)
        # adancimea in arborele de stari
        self.adancime = adancime

        # scorul starii (daca e finala) sau al celei mai bune stari-fiice (pentru playerul current)
        self.scor = scor

        # lista de mutari posibile din statea currenta
        self.mutari_posibile = []

        # cea mai buna mutare din lista de mutari posibile pentru playerul current
        self.state_chosen = None

    def player_opposite(self):
        if self.j_current == Joc.JMIN:
            return Joc.JMAX
        else:
            return Joc.JMIN

    def getmutari(self):
        return self.tabla_joc.l_mutari

    def mutari(self):
        # Aici calculez toate posiblitatile de mutare pentru toate piesele mutabile pentru calculator
        for i in range(self.tabla_joc.NR_LINII):
            for j in range(self.tabla_joc.NR_COLUMN):
                if self.tabla_joc.board[i * self.tabla_joc.NR_COLUMN + j] == self.j_current.lower() or \
                        self.tabla_joc.board[i * self.tabla_joc.NR_COLUMN + j] == self.j_current.upper():
                    self.tabla_joc.mutari(i, j, self.j_current, self.tabla_joc.board)
        # Intrucat , pentru a lua toate posibilitatile de mutare si a pastra elementele din recursivitate,
        # vectorul cu mutari este in clasa , dar in afara functiei , astfel ca pentru a obtine mutarile
        # m-am folosit de functie care returneaza mutarile din clasa joc
        l_mutari = self.getmutari()
        juc_opposite = self.player_opposite()
        l_stari_mutari = [
            Stare(mutare, juc_opposite, self.adancime - 1, parinte=self) for mutare in l_mutari]

        return l_stari_mutari

    def __str__(self):
        sir = str(self.tabla_joc) + "(Juc current: " + self.j_current + ")\n"
        return sir


""" Algoritmul MinMax """


def min_max(state):
    if state.adancime == 0 or state.tabla_joc.final(state.j_current):
        state.scor = state.tabla_joc.estimate_score(state.j_current, state.adancime)
        # print(state.adancime,state.tabla_joc.final(state.j_current))
        return state

    # calculez toate mutarile posibile din statea currenta
    state.tabla_joc.l_mutari = []  # Initialzez de fiecare data vectorul deoarece starile se obtin printr-o metoda recursiva,
    # Deci vectorul cu mutarile trebuie initializat inafara metodei in clasa
    state.mutari_posibile = state.mutari()

    # aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutari_scor = [min_max(mutare) for mutare in state.mutari_posibile]

    if state.j_current == Joc.JMAX:
        # daca playerul e JMAX aleg statea-fiica cu scorul maxim
        state.state_chosen = max(mutari_scor, key=lambda x: x.scor)
    else:
        # daca playerul e JMIN aleg statea-fiica cu scorul minim
        state.state_chosen = min(mutari_scor, key=lambda x: x.scor)

    state.scor = state.state_chosen.scor
    return state


""" Algoritmul Alpha Beta """


def alpha_beta(alpha, beta, state):
    if state.adancime == 0 or state.tabla_joc.final(state.j_current):
        state.scor = state.tabla_joc.estimate_score(state.j_current, state.adancime)

        return state
    if alpha >= beta:
        return state  # este intr-un interval invalid deci nu o mai procesez
    state.tabla_joc.l_mutari = []  # Initialzez de fiecare data vectorul deoarece starile se obtin printr-o metoda recursiva,
    # Deci vectorul cu mutarile trebuie initializat inafara metodei in clasa
    state.mutari_posibile = state.mutari()

    if state.j_current == Joc.JMAX:  # Cazul in care piesa currenta face parte din playerul actual , incercand sa maximinizeze scorul
        scor_current = float('-inf')  # Initializam scorul maxim incipient
        for mutare in state.mutari_posibile:  # Preluam toate mutrile posibile , incercam sa gasim cel mai bun scor
            state_noua = alpha_beta(alpha, beta, mutare)
            if (scor_current < state_noua.scor):
                state.state_chosen = state_noua
                scor_current = state_noua.scor
            if (
                    alpha < state_noua.scor):  # In cazul in care alfa are un nou maxim , verificam sa respecte conditia de pe nivelul parinte , acela de a nu depasi
                alpha = state_noua.scor  # Scorul minim dorit de oponent
                if alpha >= beta:
                    break

    elif state.j_current == Joc.JMIN:
        scor_current = float('inf')
        for mutare in state.mutari_posibile:
            state_noua = alpha_beta(alpha, beta, mutare)

            if scor_current > state_noua.scor:
                state.state_chosen = state_noua
                scor_current = state_noua.scor

            if beta > state_noua.scor:
                beta = state_noua.scor
                if alpha >= beta:
                    break
    if state.state_chosen is None:
        print("overflow")
        return
    state.scor = state.state_chosen.scor  # Preluam scorul copilului si il atribuim nodului parinte
    return state


tip_algoritm = None
choice = None  # Variabila fol pentru ce timp de estimare a scorului dorim sa fol
game = None
current_state = None
move_sound = None


def main():
    pygame.init()
    move_sound = pygame.mixer.Sound("move.wav")
    # initializare algoritm
    raspuns_valid = False
    while not raspuns_valid:
        tip_algoritm = input(
            "Algorimul folosit? (raspundeti cu 1 sau 2)\n 1.Minimax\n 2.Alpha-beta\n ")
        if tip_algoritm in ['1', '2']:
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")
    raspuns_valid = False
    while not raspuns_valid:
        choice = int(input(
            "Euristica folosita? (raspundeti cu 1 sau 2)\n 1.Numarul pieselor mele-numarul pieselor oponentului\n 2.Numarul pieselor mele-numarul pieselor oponentului+bonus puncte piesa tip Queen\n "))
        if choice in [1, 2]:
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")

    # initializare ADANCIME_MAX
    raspuns_valid = False
    while not raspuns_valid:
        n = input("Alege dificultatea algoritmului (incepator / mediu / avansat) : \n")
        if n in ["incepator", "mediu", "avansat"]:
            if n.lower() == "incepator":
                Stare.ADANCIME_MAX = 1
            elif n.lower() == "mediu":
                Stare.ADANCIME_MAX = 3
            elif n.lower() == "avansat":
                Stare.ADANCIME_MAX = 5
            raspuns_valid = True
        else:
            print("Trebuie sa introduceti o alegere dintre cele prezentate")

    # initializare playeri
    [s1, s2] = Joc.SIMBOLURI_JUC.copy()  # lista de simboluri posibile
    print(s1, s2)
    raspuns_valid = False
    while not raspuns_valid:
        Joc.JMIN = str(
            input("Doriti sa jucati cu {} sau cu {}? ".format(s1, s2)))
        # print(Joc.JMIN)
        if (Joc.JMIN in ['w', 'b']):
            raspuns_valid = True
        else:
            print("Raspunsul trebuie sa fie {} sau {}.".format(s1, s2))
    Joc.JMAX = s1 if Joc.JMIN == s2 else s2

    # initializare tabla
    tabla_currenta = Joc()
    print("Tabla initiala")
    print(str(tabla_currenta))

    # creare state initiala
    current_state = Stare(
        tabla_currenta, 'b', Stare.ADANCIME_MAX)
    current_state.init()
    exitprog = None
    line = -1
    column = -1
    finish = 0
    global timpInitial
    global nrMutari
    nrMutari = 0
    timpInitial = int(round(time.time() * 1000))
    run = True
    selected = None  # for mouse moves
    force_pawn = None  # for jump seq
    player = True
    pc_thread = None
    game_over = None
    while run:
        if (current_state.j_current == Joc.JMIN):
            if current_state.tabla_joc.final(Joc.JMIN):
                print("FACI CEVA?")
                current_state.ui.draw_winner(current_state.player_opposite())
                current_state.ui.update()
                game_over = 1
                break
            t_inainte = int(round(time.time() * 1000))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    print("Miau")

                    pos = current_state.ui.mapCoordToIndex(*pygame.mouse.get_pos())
                    print("POZITIIAAAA " + str(pos))
                    if pos is not None:
                        line = pos[0]
                        column = pos[1]
                        print(line, column)
                        print("NEGAMAX")
                        # Verific daca mai sunt mutari valabile pentru player
                        helper_file.okey = 0  # Initializez variabila globala folosita pentru a verifica recurrentele
                        print("SUNT")
                        helper_file.muta(line, column, current_state)
                        print("Trecut")
                        # Daca da , fac mutarea pentru input-ul ales

                        print("pana aici")

                        print("Incercati alta piesa")
                        nrMutari += 1
                        t_dupa = int(round(time.time() * 1000))
                        print("Ai \"gandit\" timp de " +
                              str(t_dupa - t_inainte) + " milisecunde.")
                        # dupa iesirea din while sigur am valida column
                        # deci pot plasa simbolul pe "tabla de joc"
                        # pozitie = line * Joc.NR_COLUMN + column
                        # current_state.tabla_joc.board[pozitie] = Joc.JMIN

                        # afisarea starii jocului in urma mutarii utilizatorului
                        print("\nTabla dupa mutarea playerului")
                        print(str(current_state))
                        # testez daca jocul a ajuns intr-o state finala
                        # si afisez un mesaj corespunzator in caz ca da
                        move_sound.play()
                        current_state.j_current = current_state.player_opposite()
                        current_state.ui.display.fill((0, 0, 0))
                        current_state.ui.draw(current_state.tabla_joc.board)
                        current_state.ui.update()
                        selected = None

        if current_state.j_current != Joc.JMIN:
            current_state.tabla_joc.l_mutari = []
            t_inainte = int(round(time.time() * 1000))
            if tip_algoritm == '1':
                state_actualizata = min_max(current_state)
            else:  # tip_algoritm==2
                state_actualizata = alpha_beta(-5000, 5000, current_state)
            if state_actualizata.state_chosen is None:
                current_state.ui.draw_winner(current_state.player_opposite())
                current_state.ui.update()
                game_over = 1
                break
            else:
                move_sound.play()
                current_state.tabla_joc = state_actualizata.state_chosen.tabla_joc
            nrMutari += 1
            current_state.j_current = current_state.player_opposite()
        if game_over == 1:
            break

        current_state.ui.display.fill((0, 0, 0))
        current_state.ui.draw(current_state.tabla_joc.board)
        current_state.ui.update()

        current_state.ui.clock.tick(30)
    time.sleep(11)
    pygame.quit()



if __name__ == "__main__":
    main()
