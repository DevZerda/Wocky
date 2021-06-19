import os, sys, time


cols = 0
UpperLeft_Corner = "╔"
UpperRight_Corner = "╗"

MiddleLine = "═"
MiddleDownLine = "╦"
MiddleUpLine = "╩"
MiddleEdge = "║"
Cross = "╬"
LeftLineLeft = "╠"
RightLineRight = "╣"
BottomLeft_Corner = "╚"
BottomRight_Corner = "╝"

"""
This function argument as to be in this format
["Name of first col", length(int), "name of second col", length]
"""
def CreateFooter(footerArr):
    lol = 0
    first_col = ""
    for i in range(0, (len(footerArr))):
        print(f"{lol} | {i}")
        if isinstance(i, int):
            for u in range(0, i):
                first_col += " "
            first_col = " " + footerArr[i-1] + first_col[len(" " + footerArr[i-1]):len(first_col)] 
            print(first_col)
        lol += 2

    
