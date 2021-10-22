S = input()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
q = S[0]
if q == vowels:
    s = S+'way'
    print(s)
else:
    print(S[1::]+q+'ay')




























































































































import time
from random import randint
import pyautogui
for i in range(500):
    vertical = randint(0, 1000)
    horizontal = randint(0, 1900)
    pyautogui.moveTo(horizontal, vertical)