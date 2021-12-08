import pyautogui
import time
import pyperclip
import keyboard

time.sleep(5) #Время - через сколько начнётся спам

def spam(text: str, amount: int):
    pyperclip.copy(text)
    for _ in range(amount):
        time.sleep(0.2) #скорость вставки сообщений
        keyboard.press_and_release('ctrl + v')
        pyautogui.press("enter")
spam(" Я НАШЕЛ СПОСОБ ВСЕХ ЗАЕБАТЬ", 100) #пишем сообщение и кол-во повторов