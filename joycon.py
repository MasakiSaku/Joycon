import pygame
from pygame.locals import *
import time
import pyautogui

def main() :
    pygame.joystick.init()
    joystick0 = pygame.joystick.Joystick(0)
    joystick0.init()

    print ("joystick start")

    pygame.init()

    while True:
         # コントローラーの操作を取得
        eventlist = pygame.event.get()

        # イベント処理
        for e in eventlist:
            if e.type == QUIT:
                return

            #ボタンが押された時
            if e.type == pygame.locals.JOYBUTTONDOWN:
                input_button = str(e.button)
                print('button :{}'.format(input_button))
                if input_button == '0':
                    #スライドを進める
                    pyautogui.keyDown('right')
                elif input_button == '3':
                    #戻る
                    pyautogui.keyDown('left')
                

        time.sleep(0.1)

if __name__ == '__main__':
    try:
        main()
    except pygame.error:
        print ("joystickが見つかりませんでした。")
