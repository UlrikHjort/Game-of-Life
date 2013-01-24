########################################################################
#                                                                           
#                              Game of Life                                      
#                                                                           
#                                life.py                                    
#                                                                           
#                                 MAIN                                      
#                                                                           
#                   Copyright (C) 1995 Ulrik Hoerlyk Hjort                   
#                                                                           
#  Game of Life is free software;  you can  redistribute it                          
#  and/or modify it under terms of the  GNU General Public License          
#  as published  by the Free Software  Foundation;  either version 2,       
#  or (at your option) any later version.                                   
#  Game of Life is distributed in the hope that it will be                           
#  useful, but WITHOUT ANY WARRANTY;  without even the  implied warranty    
#  of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                  
#  See the GNU General Public License for  more details.                    
#  You should have  received  a copy of the GNU General                     
#  Public License  distributed with Yolk.  If not, write  to  the  Free     
#  Software Foundation,  51  Franklin  Street,  Fifth  Floor, Boston,       
#  MA 02110 - 1301, USA.                                                    
########################################################################                                                                          




###################################################################################
#
#
#
###################################################################################
from copy import copy, deepcopy
from time import *
import os

dimension = 20
world = [[' ' for col in range(dimension)] for row in range(dimension)]



###################################################################################
#
#
#
###################################################################################
def clear_screen():
    if (os.name in ('ce', 'nt', 'dos')):
        os.system('cls')
    elif ('posix' in os.name):
        os.system('clear')


###################################################################################
#
#
#
###################################################################################
def init_pattern_occ1():
    world[10][10] = '*'
    world[10][11] = '*'
    world[10][12] = '*'



###################################################################################
#
#
#
###################################################################################
def init_pattern():
    world[10][9] = '*'
    world[10][10] = '*'
    world[10][11] = '*'
    world[10][12] = '*'
    world[11][12] = '*'


###################################################################################
#
#
#
###################################################################################
def print_world(w):
    for i in range(dimension):
        for j in range(dimension):
            print w[i][j] + " ",
        print




###################################################################################
#
#
#
###################################################################################
def run_world(world):

    new_world = [[' ' for col in range(dimension)] for row in range(dimension)]
    #global world
    for i in range(dimension):

        for j in range(dimension):
            alive = 0
            if world[(i-1) % dimension][j] == '*':
                alive += 1
            if world[(i+1) % dimension][j] == '*':
                alive += 1
            if world[i][(j+1) % dimension] == '*':
                alive += 1
            if world[i][(j-1) % dimension] == '*':
                alive += 1
            if world[(i-1) % dimension][(j-1) % dimension] == '*':
                alive += 1
            if world[(i+1) % dimension][(j-1) % dimension] == '*':
                alive += 1
            if world[(i-1) % dimension][(j+1) % dimension] == '*':
                alive += 1
            if world[(i+1) % dimension][(j+1) % dimension] == '*':
                alive += 1

            
            if world[i][j] == '*':
                if alive < 2 or alive > 3:
                    new_world[i][j] = ' '
                else:
                    new_world[i][j] = '*'
            else:
                if alive == 3:
                    new_world[i][j] = '*'

    return new_world

###################################################################################
#
#
#
###################################################################################


init_pattern()



while 1:
    print_world(world)
    world = deepcopy(run_world(world))
    sleep(1)
    clear_screen()
