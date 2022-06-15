#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import re
from IPython.display import Image
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_columns', None)


# - **Ejercicio 1**
# 
# Realiza web scraping de una página de la bolsa de Madrid (https://www.bolsamadrid.es) utilizando BeautifulSoup y Selenium.

# Intentaremos extraer la **tabla de índices**  de la bolsa de Barcelona( que está contenida en la web)

# Nota: Aunque el ejercicio pueda parecer simple, era la primera vez que me encontraba con este tipo de programas, además de que 
# mis conocimientos de html y el DOM eran nulos. 
# Si bien es cierto que con BeatifulSoup el aprendizaje ha sido fácil, con Selenium no. La mayoria de tutoriales, incluido el de
# la página de ITAcademy están desctaualizados. Los comandos de búsqueda no son los mismos, instalar el drive de Chrome, entre las 
# diferentes opciones que me dejaba la web de Selenium, sólo me ha funcionado una. 
# 
# En definitiva, presento el nivel 1 solamente porque he tardado más tiempo en aprender a manejarme con Selenium que entender 
# los conceptos

# In[164]:




URL = "https://www.bolsamadrid.es/esp/aspx/Indices/Resumen.aspx?grupo=BBarna"
# abrimos la web de los índices de la bolsa de Barcelona con get() 
page = requests.get(URL)

print(page.text)# imprimimos el doc de HTML


# In[165]:


soup = BeautifulSoup(page.content, "html.parser")


# tras explorar el DOM, observamos que todos los elementos de la **tabla** se encuentran anidados en la clase **TblPort**, así que guardamos la clase entera

# In[166]:


results = soup.find(class_="TblPort") 


# Podemos distinguir dos tipos de diviones intersantes, las "th" y "td". 
# 
#  - las th contienen los nombres de las columnas de la tabla
#  
#  - las td contienen todos elementos de la tabla que no son columnas   

# In[141]:


td1 = results.find_all("td")
th1= results.find_all("th")


# In[167]:


columnas1=[]# extraemos los elementos de los nombres de las columnas 
for k in range(0, 9):
       columnas1.append(th1[k].text)
columnas1


# Los elementos de la tabla en td1 vienen ordenados por filas. Es decir, primeos vienen los k elelmentos de la fila 1, luego 
# luegos los de la fila 2,... y sucesivamente. Vamos a crear uan funciona que nos separe las columnas en listas, y vamos a 
# anidar las listas-columnas en la tabla lista1

# In[168]:


lista1 =[] # contenedor de columnas 


def listaux1(i):  #función de extracción de columnas 
    list=[]
    for j in range(i, 144,9):
        list.append(td1[j].text)
        
    return list 

for i in range(0,9):
    lista1.append( listaux1(i))

lista1


# In[169]:


arr1=np.array(lista1)# la convertimos en array para poder hacer la traspuesta 


# In[170]:


df1= pd.DataFrame(arr1.T, columns=columnas1)# y creamos el DF para visualizarlo
df1


# In[171]:


#hacemos lo mismo con Selenium 


# In[19]:


from selenium import webdriver
import selenium


# Descargamos el driver

# In[173]:


driver= webdriver.Chrome(executable_path=r"C:\Users\walte\cursopy\sprint 11 y 12\chromedriver.exe")
driver.get("http:python.org")
driver.close()


# In[172]:


from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
options= Options()
#invocamos Options


# In[150]:


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[174]:


# abrimoa la web de la bolsa de Madrid 
browser= webdriver.Chrome(options =options)# 
browser.switch_to.new_window('window')
browser.get("https://www.bolsamadrid.es/esp/aspx/Indices/Resumen.aspx?grupo=BBarna")


# y a partir de aquí seguimos el mismo procedimiento que en BeautifulSoup

# In[176]:


search = browser.find_element(By.CLASS_NAME, "TblPort")


# In[177]:


type(search)


# In[178]:


print(search.text)


# In[179]:


td= search.find_elements(By.TAG_NAME, "td")
th=  search.find_elements(By.TAG_NAME, "th")
tr=search.find_elements(By.TAG_NAME, "tr")


# In[180]:


for j in td:
    print (j.text)


# In[181]:


print(len(th))


# In[182]:


columnas= []


# In[183]:



for k in range(0, 9):
       columnas.append(th[k].text)
columnas


# In[184]:


lista =[]


def listaux(i):  
    list=[]
    for j in range(i, 144,9):
        list.append(td[j].text)
        
    return list 

for i in range(0,9):
    lista.append( listaux(i))

lista
        


# In[185]:


arr=np.array(lista)
arr


# In[186]:


df= pd.DataFrame(arr.T, columns=columnas)
df


# In[188]:


browser.close()


# In[ ]:





# 
