import pyautogui, time
time.sleep(100)
f = open("spamwords.cfg", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")