# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 15:11:57 2021

@author: Пользователь
"""
import datetime
from termcolor import colored


def type_name():
    print('Type you nickname, dear user:')
    nickname = input()
    print(f'Hello {nickname}!')
    return nickname


class WorkWithLogs():
    my_file = 'logs1.txt'

    def write_logs(self, winner, n1, n2, sc1, sc2):
        with open(self.my_file, 'a') as logs:
            now = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
            new_log = (f'{now} | {n1} / {n2} : {sc1} - {sc2} | Winner: {winner}\n')
            logs.writelines(new_log)

    def read_logs(self):
        with open(self.my_file, 'rt') as logs:
            text = logs.read()
            return text

    def clean_logs(self):
        with open(self.my_file, 'w') as logs:
            logs.write('')


class User():
    score = 0
    last_score = score

    def __init__(self, name, sign):
        self.name = name
        self.sign = sign


class TicTacToe():
    field = []
    counter, check = 0, 0
    logs = WorkWithLogs()

    def __init__(self, user_x, user_y):
        self.user_x = user_x
        self.user_y = user_y

    def print_field(self):
        print(f"""
         0   1   2
       =============
     0 ! {self.field[0][0]} ! {self.field[0][1]} ! {self.field[0][2]} !
       =============
     1 ! {self.field[1][0]} ! {self.field[1][1]} ! {self.field[1][2]} !
       =============
     2 ! {self.field[2][0]} ! {self.field[2][1]} ! {self.field[2][2]} !
       =============
      """)
        return self.field

    def main_game(self):
        self.field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.counter = 0
        self.print_field()
        while self.check == 0:
            self.user_x.score = self.new_move(self.user_x)
            self.counter += 1
            if self.check_break() is True:
                break
            self.user_y.score = self.new_move(self.user_y)
            self.counter += 1
            if self.check_break() is True:
                break

    def check_break(self):
        if self.counter == 9:
            text = colored('Dead heat', 'green')
            print(text)
            self.user_x.score += 1
            self.user_y.score += 1
            winner = 'Dead heat'
            self.logs.write_logs(winner, self.user_x.name, self.user_y.name,
                                 self.user_x.score, self.user_y.score)
            self.user_x.last_score += 1
            self.user_y.last_score += 1
            self.counter = 0
            self.is_continue()
            return True
        elif self.user_x.score != self.user_x.last_score:
            winner = self.user_x.name
            self.logs.write_logs(winner, self.user_x.name, self.user_y.name,
                                 self.user_x.score, self.user_y.score)
            self.user_x.last_score += 1
            self.is_continue()
            return True
        elif self.user_y.score != self.user_y.last_score:
            winner = self.user_y.name
            self.logs.write_logs(winner, self.user_x.name, self.user_y.name,
                                 self.user_x.score, self.user_y.score)
            self.user_y.last_score += 1
            self.is_continue()
            return True

    def new_move(self, user):
        print(f'{user.name}, move {user.sign} (row, column):')
        row = int(input())
        column = int(input())
        if self.field[row][column] == ' ':
            if user.sign == 'x':
                self.field[row][column] = colored(f'{user.sign}', 'red')
            elif user.sign == 'o':
                self.field[row][column] = colored(f'{user.sign}', 'blue')
            user.score = self.check_win(user)
            self.print_field()
            return user.score
        else:
            text = colored('It is not empty. Try again!', 'red')
            print(text)
            self.move(user)
            return user.score

    def check_win(self, user):
        if (self.field[0][0] == self.field[0][1] == self.field[0][2] != ' '
                or self.field[1][0] == self.field[1][1] == self.field[1][2] != ' '
                or self.field[2][0] == self.field[2][1] == self.field[2][2] != ' '
                or self.field[0][0] == self.field[1][0] == self.field[2][0] != ' '
                or self.field[0][1] == self.field[1][1] == self.field[2][1] != ' '
                or self.field[0][2] == self.field[1][2] == self.field[2][2] != ' '
                or self.field[0][0] == self.field[1][1] == self.field[2][2] != ' '
                or self.field[2][0] == self.field[1][1] == self.field[0][2] != ' '):
            user.score += 1
            text = colored(f'{user.name} is win!', 'green')
            print(text)
            return user.score
        else:
            return user.score

    def is_continue(self):
        text = colored('Do you want to continue game?(y/n)', 'yellow')
        check = input(text)
        if check == 'y':
            self.main_game()


class Menu():
    options = '''
              Tic-Tac-Toe

            1) New game
            2) Open logs of wins
            3) Clean logs of wins
            4) Exit
            '''

    def __init__(self):
        Menu.check_menu(self, self.options)

    def check_menu(self, options):
        check = 0
        my_logs = WorkWithLogs()
        while check == 0:
            print(self.options)
            menu = input()
            if menu == '1':
                print('tic tac toe')
                name1, name2 = type_name(), type_name()
                gamer1, gamer2 = User(name1, 'x'), User(name2, 'o')
                game = TicTacToe(gamer1, gamer2)

                game.main_game()
            elif menu == '2':
                print('Open logs of wins')
                print(my_logs.read_logs())
            elif menu == '3':
                print('Clean logs of wins')
                my_logs.clean_logs()
            elif menu == '4':
                print('Exit')
                check = 2
            else:
                print('ooops! try again')


if __name__ == "__main__":
    menu = Menu()
