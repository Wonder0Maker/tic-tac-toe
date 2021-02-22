# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 11:58:43 2021

@author: Пользователь
"""
from termcolor import colored
import datetime


def Menu():
    """  """
    check = 0
    while check == 0:
        print('''
              Tic-Tac-Toe

            1) New game
            2) Open logs of wins
            3) Clean logs of wins
            4) Exit
            ''')
        menu = int(input())
        if menu == 1:
            print('tic tac toe')
            user1, user2 = type_name()
            score1, score2 = 0, 0
            tic_tac_toe(user1, user2, score1, score2)
        elif menu == 2:
            print('Open logs of wins')
            print(read_logs())
        elif menu == 3:
            print('Clean logs of wins')
            clean_logs()
        elif menu == 4:
            print('Exit')
            check = 2
        else:
            print('ooops! try again')
            Menu()


def print_field(a):
    print(f"""
         0   1   2
       =============
     0 ! {a[0][0]} ! {a[0][1]} ! {a[0][2]} !
       =============
     1 ! {a[1][0]} ! {a[1][1]} ! {a[1][2]} !
       =============
     2 ! {a[2][0]} ! {a[2][1]} ! {a[2][2]} !
       =============
      """)
    return a


def tic_tac_toe(name1, name2, score1, score2):
    field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    counter, check = 0, 0
    last1, last2 = score1, score2
    print_field(field)
    while check == 0:
        score1 = move_x(field, name1, score1)
        counter += 1
        check2 = check_break(counter, last1, last2,
                             name1, name2, score1, score2)
        if check2 is True:
            break
        score2 = move_o(field, name2, score2)
        counter += 1
        check2 = check_break(counter, last1, last2,
                             name1, name2, score1, score2)
        if check2 is True:
            break


def check_break(counter, last1, last2, name1,
                name2, score1, score2):
    if counter == 9:
        text = colored('Dead heat', 'green')
        print(text)
        score1 += 1
        score2 += 1
        winner = 'Dead heat'
        write_logs(name1, name2, score1, score2, winner)
        is_continue(name1, name2, score1, score2)
        return True
    elif score1 != last1:
        winner = name1
        write_logs(name1, name2, score1, score2, winner)
        is_continue(name1, name2, score1, score2)
        return True
    elif score2 != last2:
        winner = name2
        write_logs(name1, name2, score1, score2, winner)
        is_continue(name1, name2, score1, score2)
        return True


def is_continue(name1, name2, score1, score2):
    text = colored('Do you want to continue game?(y/n)', 'yellow')
    check = input(text)
    if check == 'y':
        tic_tac_toe(name1, name2, score1, score2)


def move_x(field, name, score):
    print(f'{name}, move X (row, column):')
    row = int(input())
    column = int(input())
    if field[row][column] == ' ':
        field[row][column] = colored('x', 'red')
        score = check_win(field, name, score)
        print_field(field)
        return score
    else:
        text = colored('It is not empty. Try again!', 'red')
        print(text)
        move_x(field, name, score)
        return score


def move_o(field, name, score):
    print(f'{name}, move O (row, column):')
    row = int(input())
    column = int(input())
    if field[row][column] == ' ':
        field[row][column] = colored('o', 'blue')
        score = check_win(field, name, score)
        print_field(field)
        return score
    else:
        text = colored('It is not empty. Try again!', 'red')
        print(text)
        move_o(field, name, score)
        return score


def check_win(a, name, score):
    if (a[0][0] == a[0][1] == a[0][2] != ' '
            or a[1][0] == a[1][1] == a[1][2] != ' '
            or a[2][0] == a[2][1] == a[2][2] != ' '
            or a[0][0] == a[1][0] == a[2][0] != ' '
            or a[0][1] == a[1][1] == a[2][1] != ' '
            or a[0][2] == a[1][2] == a[2][2] != ' '
            or a[0][0] == a[1][1] == a[2][2] != ' '
            or a[2][0] == a[1][1] == a[0][2] != ' '):
        score += 1
        text = colored(f'{name} is win!', 'green')
        print(text)
        return score
    else:
        return score


def type_name():
    print('Type you nicknames, dear users:')
    nickname1, nickname2 = input(), input()
    print(f'Hello {nickname1} and {nickname2}!')
    return nickname1, nickname2


def write_logs(n1, n2, sc1, sc2, winner):
    with open('logs.txt', 'a') as logs:
        now = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
        new_log = (
            f'{now} | {n1} / {n2} : {sc1} - {sc2} | Winner: {winner}\n')
        logs.writelines(new_log)


def read_logs():
    with open('logs.txt', 'rt') as logs:
        text = logs.read()
        return text


def clean_logs():
    with open('logs.txt', 'w') as logs:
        logs.write('')


if __name__ == "__main__":
    Menu()
