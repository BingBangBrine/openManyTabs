import pyautogui
import time
import webbrowser

# any input over 50 does not work too well
tabs = input("How many tabs do you want to open? Leave blank for 10. ")
if tabs == "":
    tabs = 10
tabs = int(tabs)

link = input("Type a link that you want to open many times. Leave blank for terraria wiki random page.")
if link == "":
    link = "https://terraria.wiki.gg/wiki/Special:Random"

repeat = input("How many times do you want the program to repeat? Leave blank for 0 repeats. ")
if repeat == "":
    repeat = 0
repeat = int(repeat)

count = 0
while count <= repeat:
    for i in range(tabs):
        webbrowser.open(f'{link}', new=1, autoraise=True)
        if i < 50:
            time.sleep(i*0.01)  # will sleep for longer, the more tabs that are open
        else:
            time.sleep(0.5)

    time.sleep(tabs*(10/35))  # will sleep for a longer time depending on how many tabs are inputted

    for i in range(tabs):
        pyautogui.hotkey('ctrl', 'w', interval=0.15)
    count += 1