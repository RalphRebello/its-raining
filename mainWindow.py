from tkinter import *
import getInstaWeather as getWt
import getCityWindow


#vendo estruturas basicas tkinter |
#as alteraçoes podem ser feitas de qualquer progama, so importar o mainWindow
window = Tk()#cria janela
window.title("It's Raining") #texto superior


welcome_text = Label(window, text="Hello, have a nice day!")  # cria texto dentro da janela
welcome_text.grid(column=0, row=0, padx=10, pady=10)  # posiciona texto dentro da janela

sync_button = Button(window, text="Get Weather Forecast", background="tan", command=getWt.get_insta_weather)
sync_button.grid(column=0, row=1, padx=10, pady=10)

city_show = Label(window, text="City")
city_show.grid(column=0, row=2)

info_show = Label(window, text="No data")  # var atualizada na funcao getInstaWeather quando clica no botao
info_show.grid(column=0, row=3, padx=10, pady=10)

get_city_button = Button(window, text="Change city", command=getCityWindow.get)
get_city_button.grid(column=0, row=4, padx=10, pady=10)

txt = Label(window, text="Weather Forecast")
txt.grid(column=0, row=5, padx=10, pady=10)
window.mainloop()  # mantem a janela aberta 'em loop'

