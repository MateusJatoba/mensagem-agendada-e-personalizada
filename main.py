import apscheduler
import apscheduler.schedulers
import apscheduler.schedulers.blocking

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


aplicacao()

# scheuler = apscheduler.schedulers.blocking.BlockingScheduler()

# scheuler.add_job(aplicacao, 'cron', day=3 , hour=16, minute=23)

# try:
#     print("Agendamento iniciado. A tarefa será executada no dia 3 de cada mês.")
#     scheuler.start()  
# except (KeyboardInterrupt, SystemExit):
#     print("Agendamento interrompido.")


