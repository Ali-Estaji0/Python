from datetime import *
import requests
from tkinter import *

root = Tk()
root.title('Live Weather')
root.geometry('350x370')
root.resizable(False, False)
root.config(bg='#66FFB2')

Url = "https://api.open-meteo.com/v1/forecast?latitude=36.2126&longitude=57.6819&hourly=temperature_2m"
location = "delhi technologicalunivercity"
Params = {'address': location}
info = requests.get(url=Url, params=Params)
data = info.json()
temps = data['hourly']['temperature_2m']

nowtimes = datetime.now()
now_hour = nowtimes.hour

# --------------------------frame------------------------------#

frm1 = Frame(root, height=40, width=320, bg='#66FFB2')
frm1.pack(side=TOP)
frm2 = Frame(root, height=40, width=320, bg='#66FFB2')
frm2.pack(side=TOP)
frm3 = Frame(root, height=40, width=320, bg='#66FFB2')
frm3.pack(side=TOP)
frm4 = Frame(root, height=40, width=320, bg='#66FFB2')
frm4.pack(side=TOP)
frm5 = Frame(root, height=40, width=320, bg='#66FFB2')
frm5.pack(side=TOP)
frm6 = Frame(root, height=40, width=320, bg='#66FFB2')
frm6.pack(side=TOP)
frm7 = Frame(root, height=40, width=320, bg='#66FFB2')
frm7.pack(side=TOP)
frm8 = Frame(root, height=40, width=320, bg='#66FFB2')
frm8.pack(side=TOP)

# --------------------------label------------------------------#

lbl1 = Label(frm6, text='Temp Is ?? C', bg='#66FFb2', fg='#202020')
lbl1.pack(padx=5, pady=5)

lbl2 = Label(frm7, text='For Get Temp Of Any Hour , Click On Hour')
lbl2.pack(padx=5, pady=5)

lbl3 = Label(frm7, text='Click To See Live Weather ',
             bg='#66FFB2', fg='#202020')
lbl3.pack(padx=5, pady=5)

# --------------------------variable-----------------------------#
temp = None
# --------------------------Defination---------------------------#


def glw():
    tempp = temps[now_hour]
    lbl3.config(text=f'Live Weather of {now_hour} , is  {tempp} C')


def h00():
    tempp = temps[0]
    lbl1.config(text=f'Temp is {tempp} C')


def h01():
    tempp = temps[1]
    lbl1.config(text=f'Temp is {tempp} C')


def h02():
    tempp = temps[2]
    lbl1.config(text=f'Temp is {tempp} C')


def h03():
    tempp = temps[3]
    lbl1.config(text=f'Temp is {tempp} C')


def h04():
    tempp = temps[4]
    lbl1.config(text=f'Temp is {tempp} C')


def h05():
    tempp = temps[5]
    lbl1.config(text=f'Temp is {tempp} C')


def h06():
    tempp = temps[6]
    lbl1.config(text=f'Temp is {tempp} C')


def h07():
    tempp = temps[7]
    lbl1.config(text=f'Temp is {tempp} C')


def h08():
    tempp = temps[8]
    lbl1.config(text=f'Temp is {tempp} C')


def h09():
    tempp = temps[9]
    lbl1.config(text=f'Temp is {tempp} C')


def h010():
    tempp = temps[10]
    lbl1.config(text=f'Temp is {tempp} C')


def h011():
    tempp = temps[11]
    lbl1.config(text=f'Temp is {tempp} C')


def h012():
    tempp = temps[12]
    lbl1.config(text=f'Temp is {tempp} C')


def h013():
    tempp = temps[13]
    lbl1.config(text=f'Temp is {tempp} C')


def h014():
    tempp = temps[14]
    lbl1.config(text=f'Temp is {tempp} C')


def h015():
    tempp = temps[15]
    lbl1.config(text=f'Temp is {tempp} C')


def h016():
    tempp = temps[16]
    lbl1.config(text=f'Temp is {tempp} C')


def h017():
    tempp = temps[17]
    lbl1.config(text=f'Temp is {tempp} C')


def h018():
    tempp = temps[18]
    lbl1.config(text=f'Temp is {tempp} C')


def h019():
    tempp = temps[19]
    lbl1.config(text=f'Temp is {tempp} C')


def h020():
    tempp = temps[20]
    lbl1.config(text=f'Temp is {tempp} C')


def h021():
    tempp = temps[21]
    lbl1.config(text=f'Temp is {tempp} C')


def h022():
    tempp = temps[22]
    lbl1.config(text=f'Temp is {tempp} C')


def h023():
    tempp = temps[23]
    lbl1.config(text=f'Temp is {tempp} C')


# --------------------------Button---------------------------#
btn0 = Button(frm8, text='Live Weather', command=glw)
btn0.pack(padx=10)

btn1 = Button(frm1, text='00', command=h00)
btn1.pack(padx=10, side=LEFT, pady=10)
btn2 = Button(frm1, text='01', command=h01)
btn2.pack(padx=10, side=LEFT)
btn3 = Button(frm1, text='02', command=h02)
btn3.pack(padx=10, side=LEFT)
btn4 = Button(frm1, text='03', command=h03)
btn4.pack(padx=10, side=LEFT)
btn5 = Button(frm1, text='04', command=h04)
btn5.pack(padx=10, side=LEFT)
btn6 = Button(frm1, text='05', command=h05)
btn6.pack(padx=10, side=LEFT)

# -------------------------------------#


btn7 = Button(frm2, text='06', command=h06)
btn7.pack(padx=10, side=LEFT, pady=10)
btn8 = Button(frm2, text='07', command=h07)
btn8.pack(padx=10, side=LEFT)
btn9 = Button(frm2, text='08', command=h08)
btn9.pack(padx=10, side=LEFT)
btn10 = Button(frm2, text='09', command=h09)
btn10.pack(padx=10, side=LEFT)
btn11 = Button(frm2, text='10', command=h010)
btn11.pack(padx=10, side=LEFT)
btn12 = Button(frm2, text='11', command=h011)
btn12.pack(padx=10, side=LEFT)

# --------------------------------------#

btn13 = Button(frm3, text='12', command=h012)
btn13.pack(padx=10, side=LEFT, pady=10)
btn14 = Button(frm3, text='13', command=h013)
btn14.pack(padx=10, side=LEFT)
btn15 = Button(frm3, text='14', command=h014)
btn15.pack(padx=10, side=LEFT)
btn16 = Button(frm3, text='15', command=h015)
btn16.pack(padx=10, side=LEFT)
btn17 = Button(frm3, text='16', command=h016)
btn17.pack(padx=10, side=LEFT)
btn18 = Button(frm3, text='17', command=h017)
btn18.pack(padx=10, side=LEFT)


# -------------------------------------#


btn19 = Button(frm4, text='18', command=h018)
btn19.pack(padx=10, side=LEFT, pady=10)
btn20 = Button(frm4, text='19', command=h019)
btn20.pack(padx=10, side=LEFT)
btn21 = Button(frm4, text='20', command=h020)
btn21.pack(padx=10, side=LEFT)
btn22 = Button(frm4, text='21', command=h021)
btn22.pack(padx=10, side=LEFT)
btn23 = Button(frm4, text='22', command=h022)
btn23.pack(padx=10, side=LEFT)
btn24 = Button(frm4, text='23', command=h023)
btn24.pack(padx=10, side=LEFT)

root.mainloop()
