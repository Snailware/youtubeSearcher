# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Adam Lancaster                                             youtube searcher #
# 9/17/2020                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# program will open a google chrome browser window, navigate to youtube and   #
# then prompt user to enter a term to search for. once use enters topic,      #
# program will enter user input and initiate a search.                        #
#                                                                             #
# NOTE program was made specifically for my computer, if you intend to run    #
# this on your own machine, you will need to change the coordinates and pics  #
# that pyautogui uses.                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import pyautogui as PAG

PAG.FAILSAFE = True
    # FAILSAFE should never be disabled, and will abort program if cursor goes 
    # to top left corner of screen.
PAG.PAUSE = 2
    # PAUSE adds delay between calls to allow loading time and prevent errors. 
moveTime = 1
    # moveTime determines how long (in seconds) it takes for the cursor to
    # reach the desired position. 

def main():

    launchChrome()
    navigateToYoutube()
    promptAndSearch()

def launchChrome():
# find and launch chrome.

    PAG.moveTo(587, 1055, moveTime)
    PAG.click()
    # this is done with coordinates instead of a png because the chrome icon
    # will always be in the same place in the taskbar. this also saves space
    # in the overall program size. 

def navigateToYoutube():
# navigate to the youtube website.

    xPosition, yPosition = PAG.locateCenterOnScreen('yticon.PNG')
    PAG.moveTo(xPosition, yPosition, moveTime)
    PAG.click()

def promptAndSearch():
# prompt user for search term, then enter term into youtube and search. 
    searchTerm = PAG.prompt('Enter Desired Search Term')
    xPosition, yPosition = PAG.locateCenterOnScreen('ytsearchicon.PNG')
    PAG.moveTo(xPosition, yPosition, moveTime)
    PAG.click()
    PAG.typewrite(searchTerm, 0.2)
    PAG.press('enter')

main()
