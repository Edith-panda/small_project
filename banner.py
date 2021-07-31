# creating a banner in python
from core.colors import colors
import os
def banner():
    picture = """ 
    ####################
    ####################
        ##       ##
         ##     ##
          ##   ##  
           ####
            ##
            ##
            ##
    ####################
    ####################
    """
    pic = picture.split('\n')
    for line in pic:
        centered = line.center(os.get_terminal_size().columns)
        print(colors.BOLD + centered + colors.end)



class colors:
    
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    G, Y, R, W, V, B, end = '\033[92m', '\033[93m', '\033[91m', '\x1b[37m', '\033[95m', '\033[94m', '\033[0m'
    info = end + W + "[-]" + W
    good = end + G + "[+]" + B
    bad = end + R + "[" + W + "!" + R + "]"