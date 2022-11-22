from tkinter import *
import getInstaWeather
import getWeather3Hours


def main():
    print('Hello')
    getInstaWeather.get_insta_weather()
    getWeather3Hours.get_3_hours_weather()


main()


window = Tk()
window.title("It's Raining")
welcome_text = Label(window, text="Hello, have a nice day!")
welcome_text.grid(column=0, row=0)
txt = Label(window, text="Weather Forecast")
txt.grid(column=0, row=2)

window.mainloop()
