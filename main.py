import datetime

def aplicacao():
    from time import sleep

    import pyautogui
    import webbrowser
    from urllib.parse import quote

    TELEFONE = 999999999
    mensagem = 'Pagar o INSS de Val'
    MENSAGEM = quote(mensagem)
    url = f'https://web.whatsapp.com/send?phone=55{TELEFONE}&text={MENSAGEM}'

    webbrowser.open(url=url)
    sleep(8)
    pyautogui.press('enter')
    sleep(5)
    pyautogui.hotkey('ctrl' , 'w')
    sleep(3)
    pyautogui.hotkey('ctrl' , 'w')


def checar_dia():
    dia = datetime.datetime.today()

    if dia == 5:
        aplicacao()


if __name__ == '__main__':
    checar_dia()

