'''
Created on Jul 1, 2010

@author: andrew
'''
import pygame,sys,math
from lib import *

import lib

def main():
    Game.main()
if __name__ == '__main__':  
    try:
        main()
    except Exception, e:
        tb = sys.exc_info()[2]
        #traceback.print_exception(e.__class__, e, tb)
    pygame.quit()