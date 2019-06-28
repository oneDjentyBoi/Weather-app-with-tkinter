import tkinter as tk
#from tkinter import font
import requests
root=tk.Tk()
root.title("Aritro's Weather app")
c=tk.Canvas(height=600,width=1000,bg='#f5427e')
c.pack()
def test(entry):
    print (entry)
bimg=tk.PhotoImage(file="C:\\Users\\USER\\Desktop\\pypy\\kolkata.png")
bimg_label=tk.Label(root,image=bimg) 
bimg_label.place(relwidth=1,relheight=1) 

def format_response(weather):
    try: 
        name = weather['city']['name']
        d = weather['list'][0]['weather'][0]['description']
        t = weather['list'][0]['main']['temp']
        finalstr = "In %s, its %s °C\n with %s"%(name,t,d)
    except:
        finalstr ="Invalid city!! Try again!!"
    return finalstr


def get_wheather(city):
    key='9adc576861292b9775d15211761badf6'
    url='https://api.openweathermap.org/data/2.5/forecast'
    params={'APPID': key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params = params,verify=False)
    weather = response.json()
    label['text'] = format_response(weather)
    #label['image']= weather['list'][0]['weather'][0]['icon']
    
    
frame=tk.Frame(root,bg='cyan',bd=5)
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.08)


entry=tk.Entry(frame,font=("Calibri",20))
entry.place(relx=0,rely=0,relheight=1,relwidth=0.6)

button=tk.Button(frame,text="GO!!",bd=5,command=lambda: get_wheather((entry.get())))
button.place(relx=0.608,rely=0,relheight=1,relwidth=0.4,anchor='nw')

l_frame=tk.Frame(root,bg='cyan',bd=5)
l_frame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

label=tk.Label(l_frame,font=("Comic Sans MS",20))
label.place(relx=0,rely=0,relheight=1,relwidth=1)
#print(tk.font.families())
root.mainloop()

