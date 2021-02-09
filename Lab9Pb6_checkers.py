import time
import copy
import helper_file
import pygame
import GameUI


class Game:
    NR_COLUMN = 8
    NR_LINII = 8
    NR_CONNECT = 4
    SIMBOLS_GAM = ['w', 'b']
    JMIN = None
    JMAX = None
    GOL = '#'

    def __init__(self, tabla=None):
        self.board = tabla or copy.deepcopy(helper_file.matrix())

        # print(Test.matrix())

    def afis_daca_final(self):
        # A castigat playerul cu cele mai multe piese pe tabla
        nra = self.board.count('W')
        nrn = self.board.count('B')
        if (nra > nrn):
            print("White wins")
        if (nrn > nra):
            print("Black wins")
        else:
            print("Draw")

    def verific_final(self, line, column):
        # In aceasta functie verific daca piesa de la coordonata line,column este mutabila sau nu
        valid_response = False
        okey = 0
        if self.board[line * 8 + column] == 'b':
            if not (line - 1 >= 0 and column - 1 >= 0):
                no_action = 1
            else:
                if self.board[(line - 1) * 8 + column - 1] == '#':
                    valid_response = True
                    okey = 1
                elif self.board[(line - 1) * 8 + column - 1] == 'w' or self.board[
                    (line - 1) * 8 + column - 1] == 'W':
                    if line - 2 >= 0 and column - 2 >= 0 and self.board[(line - 2) * 8 + column - 2] == '#':
                        valid_response = True
                        okey = 1
                        # return muta(line-2,column-2,player)
                    else:
                        no_action = 1
            if not (line - 1 >= 0 and column + 1 < 8):
                no_action = 1
            else:
                if self.board[(line - 1) * 8 + column + 1] == '#':
                    valid_response = True
                    okey = 1
                elif self.board[(line - 1) * 8 + column + 1] == 'w' or self.board[
                    (line - 1) * 8 + column + 1] == 'W':
                    if line - 2 >= 0 and column + 2 < 8 and self.board[(line - 2) * 8 + column + 2] == '#':
                        valid_response = True
                        okey = 1
                    else:
                        no_action = 1

        if self.board[line * 8 + column] == 'w':
            if not (line + 1 < 8 and column - 1 >= 0):
                no_action = 1
            else:
                if self.board[(line + 1) * 8 + column - 1] == '#':
                    valid_response = True
                    okey = 1
                elif self.board[(line + 1) * 8 + column - 1] == 'b' or self.board[
                    (line + 1) * 8 + column - 1] == 'B':
                    if line + 2 < 8 and column - 2 >= 0 and self.board[(line + 2) * 8 + column - 2] == '#':
                        valid_response = True
                        okey = 1
            if not (line + 1 < 8 and column + 1 < 8):
                no_action = 1
            else:
                if self.board[(line + 1) * 8 + column + 1] == '#':

                    valid_response = True
                    okey = 1
                elif self.board[(line + 1) * 8 + column + 1] == 'b' or self.board[
                    (line + 1) * 8 + column + 1] == 'B':
                    if line + 2 <= 7 and column + 2 < 8 and self.board[(line + 2) * 8 + column + 2] == '#':

                        valid_response = True
                        okey = 1
                    else:
                        no_action = 1
        elif self.board[line * 8 + column] == 'W':
            if not (line - 1 >= 0 and column - 1 >= 0):
                no_action = 1
            else:
                if self.board[(line - 1) * 8 + column - 1] == '#':

                    valid_response = True
                    okey = 1
                elif self.board[(line - 1) * 8 + column - 1] == 'b' or self.board[
                    (line - 1) * 8 + column - 1] == 'B':
                    if line - 2 >= 0 and column - 2 >= 0 and self.board[(line - 2) * 8 + column - 2] == '#':

                        okey = 1
                        valid_response = True
                    else:
                        no_action = 1
            if not (line - 1 >= 0 and column + 1 < 8):
                no_action = 1
            else:
                if self.board[(line - 1) * 8 + column + 1] == '#':

                    valid_response = True
                    okey = 1
                elif self.board[(line - 1) * 8 + column + 1] == 'b' or self.board[
                    (line - 1) * 8 + column + 1] == 'B':
                    if line - 2 >= 0 and column + 2 < 8 and self.board[(line - 2) * 8 + column + 2] == '#':

                        valid_response = True
                        okey = 1
                    else:
                        no_action = 1
            if not (line + 1 < 8 and column - 1 >= 0):
                no_action = 1
            else:
                if self.board[(line + 1) * 8 + column - 1] == '#':

                    valid_response = True
                    okey = 1
                elif self.board[(line + 1) * 8 + column - 1] == 'b' or self.board[
                    (line + 1) * 8 + column - 1] == 'B':
                    if line + 2 < 8 and column - 2 >= 0 and self.board[(line + 2) * 8 + column - 2] == '#':

                        valid_response = True
                        okey = 1
                    else:
                        no_action = 1
            if not (line + 1 < 8 and column + 1 < 8):
                no_action = 1
            else:
                if self.board[(line + 1) * 8 + column + 1] == '#':

                    valid_response = True
                    okey = 1
                elif self.board[(line + 1) * 8 + column + 1] == 'b' or self.board[
                    (line + 1) * 8 + column + 1] == 'B':
                    if line + 2 <= 7 and column + 2 < 8 and self.board[(line + 2) * 8 + column + 2] == '#':

                        valid_response = True
                        okey = 1
                    else:
                        no_action = 1
        elif self.board[line * 8 + column] == 'B':
            if not (line - 1 >= 0 and column - 1 >= 0):
                no_action = 1
            else:
                if self.board[(line - 1) * 8 + column - 1] == '#':

                    valid_response = True
                    okey = 1
                elif self.board[(line - 1) * 8 + column - 1] == 'w' or self.board[
                    (line - 1) * 8 + column - 1] == 'W':
                    if line - 2 >= 0 and column - 2 >= 0 and self.board[(line - 2) * 8 + column - 2] == '#':

                        okey = 1
                        valid_response = True
                    else:
                        no_action = 1
            if not (line - 1 >= 0 and column + 1 < 8):
                no_action = 1
            else:
                if self.board[(line - 1) * 8 + column + 1] == '#':

                    valid_response = True
                    okey = 1
                elif self.board[(line - 1) * 8 + column + 1] == 'w' or self.board[
                    (line - 1) * 8 + column + 1] == 'W':
                    if line - 2 >= 0 and column + 2 < 8 and self.board[(line - 2) * 8 + column + 2] == '#':

                        valid_response = True
                        okey = 1
                    else:
                        no_action = 1
            if not (line + 1 < 8 and column - 1 >= 0):
                no_action = 1
            else:
                if self.board[(line + 1) * 8 + column - 1] == '#':

                    valid_response = True
                    okey = 1
                elif self.board[(line + 1) * 8 + column - 1] == 'w' or self.board[
                    (line + 1) * 8 + column - 1] == 'W':
                    if line + 2 < 8 and column - 2 >= 0 and self.board[(line + 2) * 8 + column - 2] == '#':

                        valid_response = True
                        okey = 1
                    else:
                        no_action = 1
            if not (line + 1 < 8 and column + 1 < 8):
                no_action = 1
            else:
                if self.board[(line + 1) * 8 + column + 1] == '#':

                    valid_response = True
                    okey = 1
                elif self.board[(line + 1) * 8 + column + 1] == 'w' or self.board[
                    (line + 1) * 8 + column + 1] == 'W':
                    if line + 2 <= 7 and column + 2 < 8 and self.board[(line + 2) * 8 + column + 2] == '#':

                        valid_response = True
                        okey = 1
                    else:
                        no_action = 1
        return valid_response

    def final(self, player):
        # Verific daca mai e posibila cel putin o move , pentru playerul current
        for i in range(self.NR_LINII):
            for j in range(self.NR_COLUMN):
                if self.board[i * self.NR_COLUMN + j] == player.lower() or self.board[
                    i * self.NR_COLUMN + j] == player.upper():
                    # Aici verific toate posibilitatile unei piese ce apartine de player pentru a o muta
                    # Daca cel putin una e mutabila , playerul mai poate muta , deci n-a pierdut
                    if self.verific_final(i, j) == True:
                        return 0
        return 1

    l_moves = []

    def moves(self, line, column, player, matrix):
        # Aici calculatorul calculeaza toate posibilitatile de move(l_moves l-am scos inafara functiei)
        # Pentru a updata si atunci cand piesul are multiple posibilitati de move
        # in player se pasteeaza playerul current iar matrix ->matrixa currenta pentru o anumita move
        valid_response = False
        aux = copy.deepcopy(matrix)
        if matrix[line * 8 + column] == 'b':
            if not (line - 1 >= 0 and column - 1 >= 0):  # Verific ca prin move sa nu ies din matrix
                no_action = 1
            else:
                if matrix[(line - 1) * 8 + column - 1] == '#':  # Vad daca piesa se paote muta la stanga
                    aux[line * 8 + column] = '#'
                    if line - 1 > 0:  # Daca inca n-am ajuns la ultima line sa transformam piesa in N , continuam cu aceeasi piesa
                        aux[(line - 1) * 8 + column - 1] = 'b'
                    else:
                        aux[(line - 1) * 8 + column - 1] = 'B'
                        # Se preiau toate movesle posibile
                    self.l_moves.append(Game(aux))
                elif matrix[(line - 1) * 8 + column - 1] == 'w' or self.board[(line - 1) * 8 + column - 1] == 'W':
                    if line - 2 >= 0 and column - 2 >= 0 and aux[(line - 2) * 8 + column - 2] == '#':
                        aux[(line - 2) * 8 + column - 2] = 'b'
                        if line - 2 == 0:
                            aux[(line - 2) * 8 + column - 2] = 'B'
                        aux[line * 8 + column] = '#'
                        aux[(line - 1) * 8 + column - 1] = '#'
                        self.l_moves.append(Game(aux))
                        # Pentru movesle multiple , se iau toate cazurile
                        # Parcurg recursiv la movesle jumps pana nu mai pot efectua jump-uri
                        # Si salvez fiecare configuratie in parte
                        self.moves(line - 2, column - 2, player, aux)
                    else:
                        no_action = 1
            aux = copy.deepcopy(matrix)
            if not (line - 1 >= 0 and column + 1 < 8):
                no_action = 1
            else:
                if matrix[(
                                    line - 1) * 8 + column + 1] == '#':  # Vad daca piesa se paote muta la dreapta,acelas mecanism ca la movea piesei pe stanga
                    aux[line * 8 + column] = '#'
                    if line - 1 > 0:
                        aux[(line - 1) * 8 + column + 1] = 'b'
                    else:
                        aux[(line - 1) * 8 + column + 1] = 'B'
                    self.l_moves.append(Game(aux))
                elif matrix[(line - 1) * 8 + column + 1] == 'w' or self.board[(line - 1) * 8 + column + 1] == 'W':
                    if line - 2 >= 0 and column + 2 < 8 and self.board[(line - 2) * 8 + column + 2] == '#':
                        aux[(line - 2) * 8 + column + 2] = 'b'
                        if line - 2 == 0:
                            aux[(line - 2) * 8 + column + 2] = 'B'
                        aux[line * 8 + column] = '#'
                        aux[(line - 1) * 8 + column + 1] = '#'
                        self.l_moves.append(Game(aux))
                        self.moves(line - 2, column + 2, player, aux)
                    else:
                        no_action = 1

        if matrix[
            line * 8 + column] == 'w':  # Acelas mecanism dar pentru alb , cand doreste sa inainteze stanga pe matrix
            if not (line + 1 < 8 and column - 1 >= 0):
                no_action = 1
            else:
                if matrix[(line + 1) * 8 + column - 1] == '#':
                    aux[line * 8 + column] = '#'
                    if line + 1 < 7:
                        aux[(line + 1) * 8 + column - 1] = 'w'
                    else:
                        aux[(line + 1) * 8 + column - 1] = 'W'
                    self.l_moves.append(Game(aux))
                elif matrix[(line + 1) * 8 + column - 1] == 'b' or self.board[(line + 1) * 8 + column - 1] == 'B':
                    if line + 2 < 8 and column - 2 >= 0 and self.board[(line + 2) * 8 + column - 2] == '#':
                        aux[(line + 2) * 8 + column - 2] = 'w'
                        if line + 2 == 7:
                            aux[(line + 2) * 8 + column - 2] = 'W'
                        aux[line * 8 + column] = '#'
                        aux[(line + 1) * 8 + column - 1] = '#'
                        self.l_moves.append(Game(aux))
                        self.moves(line + 2, column - 2, player, aux)
            aux = copy.deepcopy(matrix)
            if not (
                    line + 1 < 8 and column + 1 < 8):  # Acelas mecanism pentru alb , cand doreste sa inainteze stanga pe matrix
                no_action = 1
            else:
                if matrix[(line + 1) * 8 + column + 1] == '#':
                    aux[line * 8 + column] = '#'
                    if line + 1 < 7:
                        aux[(line + 1) * 8 + column + 1] = 'w'
                    else:
                        aux[(line + 1) * 8 + column + 1] = 'W'
                    self.l_moves.append(Game(aux))
                elif matrix[(line + 1) * 8 + column + 1] == 'b' or self.board[(line + 1) * 8 + column + 1] == 'B':
                    if line + 2 <= 7 and column + 2 < 8 and self.board[(line + 2) * 8 + column + 2] == '#':
                        aux[(line + 2) * 8 + column + 2] = 'w'
                        if line + 2 == 7:
                            aux[(line + 2) * 8 + column + 2] = 'W'
                        aux[line * 8 + column] = '#'
                        aux[(line + 1) * 8 + column + 1] = '#'
                        self.l_moves.append(Game(aux))
                        self.moves(line + 2, column + 2, player, aux)
                    else:
                        no_action = 1
        elif matrix[
            line * 8 + column] == 'W':  # Acelas mecanism pentru alb piesa A mare , avand posibilitatea sa se deplaseze si sus si jos stanga/dreapta
            if not (line - 1 >= 0 and column - 1 >= 0):  # Cazul unde piesa doreste sa se deplaseze stanga sus
                no_action = 1
            else:
                if matrix[(line - 1) * 8 + column - 1] == '#':
                    aux[line * 8 + column] = '#'
                    aux[(line - 1) * 8 + column - 1] = 'W'
                    self.l_moves.append(Game(aux))
                elif matrix[(line - 1) * 8 + column - 1] == 'b' or self.board[(line - 1) * 8 + column - 1] == 'B':
                    if line - 2 >= 0 and column - 2 >= 0 and aux[(line - 2) * 8 + column - 2] == '#':
                        aux[(line - 2) * 8 + column - 2] = 'W'
                        aux[line * 8 + column] = '#'
                        aux[(line - 1) * 8 + column - 1] = '#'
                        okey = 1
                        valid_response = True
                        self.l_moves.append(Game(aux))
                        self.moves(line - 2, column - 2, player, aux)
                    else:
                        no_action = 1
            aux = copy.deepcopy(matrix)
            if not (line - 1 >= 0 and column + 1 < 8):  # Cazul unde piesa doreste sa se deplaseze dreapta sus
                no_action = 1
            else:
                if matrix[(line - 1) * 8 + column + 1] == '#':
                    aux[(line) * 8 + column] = '#'
                    aux[(line - 1) * 8 + column + 1] = 'W'
                    self.l_moves.append(Game(aux))
                elif matrix[(line - 1) * 8 + column + 1] == 'b' or self.board[(line - 1) * 8 + column + 1] == 'B':
                    if line - 2 >= 0 and column + 2 < 8 and self.board[(line - 2) * 8 + column + 2] == '#':
                        aux[(line - 2) * 8 + column + 2] = 'W'
                        aux[line * 8 + column] = '#'
                        aux[(line - 1) * 8 + column + 1] = '#'
                        self.l_moves.append(Game(aux))
                        self.moves(line - 2, column + 2, player, matrix)
                    else:
                        no_action = 1
            aux = copy.deepcopy(matrix)
            if not (line + 1 < 8 and column - 1 >= 0):  # Cazul unde piesa doreste sa se deplaseze stanga jos
                no_action = 1
            else:
                if matrix[(line + 1) * 8 + column - 1] == '#':
                    aux[line * 8 + column] = '#'
                    aux[(line + 1) * 8 + column - 1] = 'W'
                    self.l_moves.append(Game(aux))
                elif matrix[(line + 1) * 8 + column - 1] == 'b' or self.board[(line + 1) * 8 + column - 1] == 'B':
                    if line + 2 < 8 and column - 2 >= 0 and self.board[(line + 2) * 8 + column - 2] == '#':
                        aux[(line + 2) * 8 + column - 2] = 'W'
                        aux[line * 8 + column] = '#'
                        aux[(line + 1) * 8 + column - 1] = '#'
                        self.l_moves.append(Game(aux))
                        self.moves(line + 2, column - 2, player, aux)
                    else:
                        no_action = 1
            aux = copy.deepcopy(matrix)
            if not (line + 1 < 8 and column + 1 < 8):  # Cazul unde piesa doreste sa se deplaseze dreapta jos
                no_action = 1
            else:
                if matrix[(line + 1) * 8 + column + 1] == '#':
                    aux[line * 8 + column] = '#'
                    aux[(line + 1) * 8 + column + 1] = 'W'
                    self.l_moves.append(Game(aux))
                elif matrix[(line + 1) * 8 + column + 1] == 'b' or self.board[(line + 1) * 8 + column + 1] == 'B':
                    if line + 2 <= 7 and column + 2 < 8 and self.board[(line + 2) * 8 + column + 2] == '#':
                        aux[(line + 2) * 8 + column + 2] = 'W'
                        aux[line * 8 + column] = '#'
                        aux[(line + 1) * 8 + column + 1] = '#'
                        self.l_moves.append(Game(aux))
                        self.moves(line + 2, column + 2, player, aux)
                    else:
                        no_action = 1
        elif matrix[line * 8 + column] == 'B':  # Acelas mecanism ca la piesa A
            if not (line - 1 >= 0 and column - 1 >= 0):
                no_action = 1
            else:
                if matrix[(line - 1) * 8 + column - 1] == '#':
                    aux[line * 8 + column] = '#'
                    aux[(line - 1) * 8 + column - 1] = 'B'
                    self.l_moves.append(Game(aux))
                elif matrix[(line - 1) * 8 + column - 1] == 'w' or self.board[(line - 1) * 8 + column - 1] == 'W':
                    if line - 2 >= 0 and column - 2 >= 0 and aux[(line - 2) * 8 + column - 2] == '#':
                        aux[(line - 2) * 8 + column - 2] = 'B'
                        aux[line * 8 + column] = '#'
                        aux[(line - 1) * 8 + column - 1] = '#'
                        okey = 1
                        valid_response = True
                        self.l_moves.append(Game(aux))
                        self.moves(line - 2, column - 2, player, aux)
                    else:
                        no_action = 1
            aux = copy.deepcopy(matrix)
            if not (line - 1 >= 0 and column + 1 < 8):
                no_action = 1
            else:
                if matrix[(line - 1) * 8 + column + 1] == '#':
                    aux[(line - 1) * 8 + column + 1] = 'B'
                    aux[(line) * 8 + column] = '#'
                    self.l_moves.append(Game(aux))
                elif matrix[(line - 1) * 8 + column + 1] == 'w' or self.board[(line - 1) * 8 + column + 1] == 'W':
                    if line - 2 >= 0 and column + 2 < 8 and self.board[(line - 2) * 8 + column + 2] == '#':
                        aux[(line - 2) * 8 + column + 2] = 'B'
                        aux[line * 8 + column] = '#'
                        aux[(line - 1) * 8 + column + 1] = '#'
                        self.l_moves.append(Game(aux))
                        self.moves(line - 2, column + 2, player, aux)
                    else:
                        no_action = 1
            aux = copy.deepcopy(matrix)
            if not (line + 1 < 8 and column - 1 >= 0):
                no_action = 1
            else:
                if matrix[(line + 1) * 8 + column - 1] == '#':
                    aux[line * 8 + column] = '#'
                    aux[(line + 1) * 8 + column - 1] = 'B'
                    self.l_moves.append(Game(aux))
                elif matrix[(line + 1) * 8 + column - 1] == 'w' or self.board[(line + 1) * 8 + column - 1] == 'W':
                    if line + 2 < 8 and column - 2 >= 0 and self.board[(line + 2) * 8 + column - 2] == '#':
                        aux[(line + 2) * 8 + column - 2] = 'B'
                        aux[line * 8 + column] = '#'
                        aux[(line + 1) * 8 + column - 1] = '#'
                        self.l_moves.append(Game(aux))
                        self.moves(line + 2, column - 2, player, aux)
                    else:
                        no_action = 1
            aux = copy.deepcopy(matrix)
            if not (line + 1 < 8 and column + 1 < 8):
                no_action = 1
            else:
                if matrix[(line + 1) * 8 + column + 1] == '#':
                    aux[line * 8 + column] = '#'
                    aux[(line + 1) * 8 + column + 1] = 'B'
                    self.l_moves.append(Game(aux))
                elif matrix[(line + 1) * 8 + column + 1] == 'w' or self.board[(line + 1) * 8 + column + 1] == 'W':
                    if line + 2 <= 7 and column + 2 < 8 and self.board[(line + 2) * 8 + column + 2] == '#':
                        aux[(line + 2) * 8 + column + 2] = 'B'
                        aux[line * 8 + column] = '#'
                        aux[(line + 1) * 8 + column + 1] = '#'
                        self.l_moves.append(Game(aux))
                        self.moves(line + 2, column + 2, player, aux)
                    else:
                        no_action = 1

    def heuristic_method(self):
        global choice
        if choice == 1:
            return self.board.count(self.JMAX) - self.board.count(self.JMIN)
        else:
            return self.board.count(self.JMAX) - self.board.count(self.JMIN) + self.board.count(
                self.JMAX.upper()) - self.board.count(self.JMIN.upper())  # Bonus daca ai piese Queen

    def estimate_score(self, player, depth):
        # Daca s-a terminat jocul pentru minim , ins ca e cel mai bun scor(max a castigat) , altfel viceversa
        t_final = self.final(player)
        if t_final == 1 and Game.JMIN == player:
            return (-999 - depth)
        elif t_final == 1 and Game.JMAX == player:
            return (999 + depth)
        elif t_final == 'remiza':
            return 0
        else:
            return self.heuristic_method()

    def __str__(self):
        sir = '  '
        for nr_col in range(self.NR_COLUMN):
            sir += str(nr_col) + ' '
        sir += '\n'

        for lin in range(self.NR_LINII):
            k = lin * self.NR_COLUMN
            sir += (str(lin) + " " + " ".join([str(x) for x in self.board[k: k + self.NR_COLUMN]]) + "\n")
        # Afisez matrixa , prima line/column semnifica coordonatele carteziene , pentru a identifica ce piesa dorim sa mutam
        return sir


class State:
    """
    Clasa folosita de algoritmii minimax si alpha-beta
    Are ca proprietate tabla de joc
    Functioneaza cu conditia ca in cadrul clasei Game sa fie definiti JMIN si JMAX (cei doi playeri posibili)
    De asemenea cere ca in clasa Game sa fie definita si o metoda numita moves() care ofera lista cu
    configuratiile posibile in urma movesi unui player
    """

    ADANCIME_MAX = None

    def init(self):

        self.ui.init_window()
        self.ui.draw(self.board_game.board)
        self.ui.update()

    def __init__(self, board_game, j_current, depth, parinte=None, scor=None):
        self.board_game = board_game
        self.j_current = j_current
        self.ui = GameUI.GameUI(background_color=(48, 25, 52), border_color=(120, 24, 74),
                                black_cell_color=(48, 25, 52), white_cell_color=(120, 24, 74), border_size=1)
        # deptha in arborele de stari
        self.depth = depth

        # scorul starii (daca e finala) sau al celei mai bune stari-fiice (pentru playerul current)
        self.scor = scor

        # lista de moves posibile din statea currenta
        self.possible_moves = []

        # cea mai buna move din lista de moves posibile pentru playerul current
        self.state_chosen = None

    def player_opposite(self):
        if self.j_current == Game.JMIN:
            return Game.JMAX
        else:
            return Game.JMIN

    def getmoves(self):
        return self.board_game.l_moves

    def moves(self):
        # Aici calculez toate posiblitatile de move pentru toate piesele mutabile pentru calculator
        for i in range(self.board_game.NR_LINII):
            for j in range(self.board_game.NR_COLUMN):
                if self.board_game.board[i * self.board_game.NR_COLUMN + j] == self.j_current.lower() or \
                        self.board_game.board[i * self.board_game.NR_COLUMN + j] == self.j_current.upper():
                    self.board_game.moves(i, j, self.j_current, self.board_game.board)
        # Intrucat , pentru a lua toate posibilitatile de move si a pastra elementele din recursivitate,
        # vectorul cu moves este in clasa , dar in afara functiei , astfel ca pentru a obtine movesle
        # m-am folosit de functie care returneaza movesle din clasa joc
        l_moves = self.getmoves()
        part_opposite = self.player_opposite()
        l_stari_moves = [
            State(move, part_opposite, self.depth - 1, parinte=self) for move in l_moves]

        return l_stari_moves

    def __str__(self):
        sir = str(self.board_game) + "(Juc current: " + self.j_current + ")\n"
        return sir


""" Algoritmul MinMax """


def min_max(state):
    if state.depth == 0 or state.board_game.final(state.j_current):
        state.scor = state.board_game.estimate_score(state.j_current, state.depth)
        # print(state.depth,state.board_game.final(state.j_current))
        return state

    # calculez toate movesle posibile din statea currenta
    state.board_game.l_moves = []  # Initialzez de fiecare data vectorul deoarece starile se obtin printr-o metoda recursiva,
    # Deci vectorul cu movesle trebuie initializat inafara metodei in clasa
    state.possible_moves = state.moves()

    # aplic algoritmul minimax pe toate movesle posibile (calculand astfel subarborii lor)
    moves_scor = [min_max(move) for move in state.possible_moves]

    if state.j_current == Game.JMAX:
        # daca playerul e JMAX aleg statea-fiica cu scorul maxim
        state.state_chosen = max(moves_scor, key=lambda x: x.scor)
    else:
        # daca playerul e JMIN aleg statea-fiica cu scorul minim
        state.state_chosen = min(moves_scor, key=lambda x: x.scor)

    state.scor = state.state_chosen.scor
    return state


""" Algoritmul Alpha Beta """


def alpha_beta(alpha, beta, state):
    if state.depth == 0 or state.board_game.final(state.j_current):
        state.scor = state.board_game.estimate_score(state.j_current, state.depth)

        return state
    if alpha >= beta:
        return state  # este intr-un interval invalid deci nu o mai procesez
    state.board_game.l_moves = []  # Initialzez de fiecare data vectorul deoarece starile se obtin printr-o metoda recursiva,
    # Deci vectorul cu movesle trebuie initializat inafara metodei in clasa
    state.possible_moves = state.moves()

    if state.j_current == Game.JMAX:  # Cazul in care piesa currenta face parte din playerul actual , incercand sa maximinizeze scorul
        current_score = float('-inf')  # Initializam scorul maxim incipient
        for move in state.possible_moves:  # Preluam toate mutrile posibile , incercam sa gasim cel mai bun scor
            state_noua = alpha_beta(alpha, beta, move)
            if (current_score < state_noua.scor):
                state.state_chosen = state_noua
                current_score = state_noua.scor
            if (
                    alpha < state_noua.scor):  # In cazul in care alfa are un nou maxim , verificam sa respecte conditia de pe nivelul parinte , acela de a nu depasi
                alpha = state_noua.scor  # Scorul minim dorit de oponent
                if alpha >= beta:
                    break

    elif state.j_current == Game.JMIN:
        current_score = float('inf')
        for move in state.possible_moves:
            state_noua = alpha_beta(alpha, beta, move)

            if current_score > state_noua.scor:
                state.state_chosen = state_noua
                current_score = state_noua.scor

            if beta > state_noua.scor:
                beta = state_noua.scor
                if alpha >= beta:
                    break
    if state.state_chosen is None:
        print("overflow")
        return
    state.scor = state.state_chosen.scor
    return state


tip_algoritm = None
choice = None  
game = None
current_state = None
move_sound = None


def main():
    pygame.init()
    move_sound = pygame.mixer.Sound("move.wav")
    # initializare algoritm
    valid_response = False
    while not valid_response:
        tip_algoritm = input(
            "Algorithm used? (respond with 1 or 2)\n 1.Minimax\n 2.Alpha-beta\n ")
        if tip_algoritm in ['1', '2']:
            valid_response = True
        else:
            print("You didn't choose a correct option.")
    valid_response = False
    while not valid_response:
        choice = int(input(
            "Heuristics used? (answer with 1 or 2) \n 1.Number of my pieces-number of opponent's pieces \n 2.Number of my pieces-number of opponent's pieces + bonus points Queen type piece \n"))
        if choice in [1, 2]:
            valid_response = True
        else:
            print("You didn't choose a correct option.")

    # initializare ADANCIME_MAX
    valid_response = False
    while not valid_response:
        n = input("Choose algorithm difficulty (begginer / intermediate / advanced) : \n")
        if n in ["begginer", "intermediate", "avansat"]:
            if n.lower() == "begginer":
                State.ADANCIME_MAX = 1
            elif n.lower() == "intermediate":
                State.ADANCIME_MAX = 3
            elif n.lower() == "advanced":
                State.ADANCIME_MAX = 5
            valid_response = True
        else:
            print("You have to choose an option between those presented")

    # initializare playeri
    [s1, s2] = Game.SIMBOLS_GAM.copy()  # lista de simboluri posibile
    valid_response = False
    while not valid_response:
        Game.JMIN = str(
            input("Do you want to play with {} or {}?? ".format(s1, s2)))
        # print(Game.JMIN)
        if (Game.JMIN in ['w', 'b']):
            valid_response = True
        else:
            print("Response should be {} or {}..".format(s1, s2))
    Game.JMAX = s1 if Game.JMIN == s2 else s2

    # initializare tabla
    current_table = Game()
    print("Initial Table")
    print(str(current_table))

    # creare state initiala
    current_state = State(
        current_table, 'b', State.ADANCIME_MAX)
    current_state.init()
    exitprog = None
    line = -1
    column = -1
    finish = 0
    global timpInitial
    global nrMutari
    timpInitial = int(round(time.time() * 1000))
    run = True
    selected = None  # for mouse moves
    force_pawn = None  # for jump seq
    player = True
    pc_thread = None
    game_over = None
    while run:
        if (current_state.j_current == Game.JMIN):
            if current_state.board_game.final(Game.JMIN):
                current_state.ui.draw_winner(current_state.player_opposite())
                current_state.ui.update()
                game_over = 1
                break
            t_inainte = int(round(time.time() * 1000))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = current_state.ui.mapCoordToIndex(*pygame.mouse.get_pos())
                    if pos is not None:
                        line = pos[0]
                        column = pos[1]
                        helper_file.okey = 0
                        helper_file.move(line, column, current_state)
                        move_sound.play()
                        current_state.j_current = current_state.player_opposite()
                        current_state.ui.display.fill((0, 0, 0))
                        current_state.ui.draw(current_state.board_game.board)
                        current_state.ui.update()
                        selected = None

        if current_state.j_current != Game.JMIN:
            current_state.board_game.l_moves = []
            t_inainte = int(round(time.time() * 1000))
            if tip_algoritm == '1':
                state_updated = min_max(current_state)
            else:  # tip_algoritm==2
                state_updated = alpha_beta(-5000, 5000, current_state)
            if state_updated.state_chosen is None:
                current_state.ui.draw_winner(current_state.player_opposite())
                current_state.ui.update()
                game_over = 1
                break
            else:
                move_sound.play()
                current_state.board_game = state_updated.state_chosen.board_game
            current_state.j_current = current_state.player_opposite()
        if game_over == 1:
            break

        current_state.ui.display.fill((0, 0, 0))
        current_state.ui.draw(current_state.board_game.board)
        current_state.ui.update()

        current_state.ui.clock.tick(30)
    time.sleep(11)
    pygame.quit()



if __name__ == "__main__":
    main()
