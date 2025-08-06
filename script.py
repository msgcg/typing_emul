import keyboard
import time

print('5 секунд на фокус окна...')
time.sleep(5)

with open('text.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    keyboard.write(line.rstrip('\n'), delay=0.00001)
    keyboard.press_and_release('enter')
