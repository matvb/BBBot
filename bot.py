from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

# setup variables
f = open("variables.txt", "r")
pathWD = f.readline().replace('\n','')
linkVotacao = f.readline().replace('\n','')
nomeDoMeuVoto = f.readline().replace('\n','').title()
login = f.readline().replace('\n','')
password = f.readline().replace('\n','')
f.close()

browser = webdriver.Chrome(pathWD)
browser.get(linkVotacao)

AllParedados = browser.find_elements_by_class_name("_18p_tzl-nqcb9ABOQXokP0")
print(AllParedados)
for x in AllParedados:
    if x.text == nomeDoMeuVoto:
        meuVoto = x
print(meuVoto.text)
time.sleep(1)
meuVoto.click()

# only first time!

time.sleep(1)
iframe = browser.find_element_by_xpath("//iframe[@src='https://login.globo.com/login/6694?url=https://gshow.globo.com/realities/bbb/bbb20/votacao/paredao-bbb20-quem-voce-quer-eliminar-felipe-manu-ou-mari-a9f49f90-84e2-4c12-a9af-b262e2dd5be4.ghtml&tam=WIDGET']")
browser.switch_to.frame(iframe)
loginForm = browser.find_elements_by_id("login")
loginForm = loginForm[0]
loginForm.send_keys(login)
passwordForm = browser.find_elements_by_id("password")
passwordForm = passwordForm[0]
passwordForm.send_keys(password)
loginButton = browser.find_element_by_xpath("//button[@type='submit']")
loginButton.click()
browser.switch_to.default_content()
time.sleep(5)

# vote loop
while(True):
        try:
            image = browser.find_element_by_class_name("gc__3_EfD")
            image.click()
            time.sleep(2)
        except:
            break
print('FIM')
