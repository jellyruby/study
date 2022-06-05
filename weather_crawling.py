from urllib.request import urlopen
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

from tkinter import *

def get_weather() :

    weather_list = []

    html = urlopen("https://www.weather.go.kr/w/weather/forecast/mid-term.do")

    bsObject = BeautifulSoup(html, "html.parser")

    for link in bsObject.find_all('a'):
        if link.text.strip() == '그래프':
            print(link.text.strip(), link.get('href'))
            weather_list.append(link.get('href'))
    
    return weather_list

#for link in bsObject.find_all('img'):
#    print(link.text.strip(), link.get('src'))

#plt.plot([1,2,3], [110,130,120])
#plt.show()

tk = Tk()

def event():
    text.delete(1.0,"end")
    text.insert(1.0, '\n'.join(get_weather()))

button = Button(tk,text='날씨 URL 가져오기.',command=event)
button2 = Button(tk,text=' 날씨 정보 가져오기.')
button.pack(side=LEFT,padx=10,pady=10) #side로 배치설정, padx로 좌우 여백설정, pady로 상하 여백설정 
button2.pack(side=LEFT, padx=10, pady= 10)

text=Text(tk)
text.insert(CURRENT, "")


text.pack()
tk.title("JongHwa Crwaling Project")
tk.geometry("1000x400+100+100")


tk.mainloop()
