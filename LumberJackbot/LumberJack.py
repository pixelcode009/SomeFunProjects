from pyautogui import press, pixelMatchesColor
flag = 0



while True:
    if pixelMatchesColor(889, 393, (161, 116, 56), 1):
        flag = 1
    elif pixelMatchesColor(1026, 391, (161, 116, 56), 1):
        flag =0

    if flag:
        press("right")
    else:
        press("left")


##you have to install pyautogui
##Plus you might have to configure according to your screen I mean the coordinates

##889, 393 is for the left branch wood
##1026 , 391 is for the right branch wood

##(211, 247, 255)  Sky

##(161, 116, 56) Wood


##Score totally depends upon you system
