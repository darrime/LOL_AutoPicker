import pyautogui
import keyboard

want = input('원하는 포지션 입력 : ')
print('-:마우스 좌표 입력받기')
print('=:매크로 실행')
location = (0,0)
while True:
    if keyboard.is_pressed('-'):
        location = pyautogui.position()
        print(location)
    if keyboard.is_pressed('='):
        for i in range(10):
            pyautogui.click(location)
            keyboard.write(want)
            keyboard.press('enter')
        break;