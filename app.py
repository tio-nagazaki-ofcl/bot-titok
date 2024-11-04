#-passos-manuais-em-sequencia,-dps-tonar-cada-passo- em-um-codigo-python
#quais-são-os-passo-manuas
#1- navegar-ate-o-site-tiktiok = "https://www.tiktok.com/@achados.shopee.hirosh?lang=en"
import webbrowser, pyautogui
from time import sleep
webbrowser.open("https://www.tiktok.com/foryou")
sleep(5)
#2- clicar-em-login
pyautogui.click(1780,149,duration=2)
sleep(3)
#3- cliacar-em-logar-com-email
pyautogui.click(1370,469,duration=3)
sleep(3)
#4- clicar-em-logar-com/usarname
pyautogui.click(1408,388,duration=2)
sleep(3)
#5- digitar-email/usarname-e-senha
pyautogui.click(1271,432,duration=2)
pyautogui.write('thionagazaki@gmail.com')
sleep(4)
pyautogui.click(1267,484,duration=2)
pyautogui.write('F9:kdK7N6c;n27|')
sleep(4)
#6- clicar-em-login
pyautogui.click(1282,581,duration=2)
sleep(30)
#7- navegar-ate-a-pagina = "https://www.tiktok.com/@achados.shopee.hirosh?lang=en"
webbrowser.open('https://www.tiktok.com/@thio_nagazaki')
sleep(5)
#8- clicar na postagem mais recente
pyautogui.click(1143,636,duration=2)
sleep(5)
#9- verificar se o videos foi curtido
for video in range(24):
    imagem = pyautogui.ImageNotFoundException('curtida.png')
    if imagem:
        #pule para o proximo video
        pyautogui.click(1607,355,duration=2)
        sleep(5)
        pyautogui.click(1516,578,duration=2)
    else:
        # codigo para curtir o videos
        sleep(5)
        pyautogui.click(1607,355,duration=2)
        pyautogui.click(1516,578,duration=2)
#se foi curtido passar para o proximo video
#se não foi curtido, curtir este video e passar para o proximo video
#10- repitir por quantas vezes quiser