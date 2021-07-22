from tkinter import *
import tkinter.font
import calculator
from time import time, sleep

#main Window using Tk
import threading
import requests
import json

win = Tk()

win.title("Crypto Portfolio")
win.geometry('800x480')
win.configure(background='#2d913a')
name, inr, crypto = calculator.values()



# data = scrape.reloadapi()

def portal(real_name, crypto_value, cur_inr, spend_inr, c, live):
    cryptoname = Label(win, text=f"{real_name}")
    cryptoname.place(x=15, y=100+c)

    C_V = "{:.5f}".format(crypto_value)
    cryptovalue = Label(win, text=f"{C_V}")
    cryptovalue.place(x=200, y=100+c)

    C_I = "{:.2f}".format(cur_inr)
    curinr = Label(win, text=f"{C_I}")
    curinr.place(x=300, y=100+c)

    S_I = "{:.2f}".format(spend_inr)
    spendinr = Label(win, text=f"{S_I}")
    spendinr.place(x=400, y=100+c)

    LIVE = "{:.4f}".format(live)
    live1 = Label(win, text=f"{LIVE}")
    live1.place(x=500, y=100+c)

    P_L = "{:.5f}".format(cur_inr - spend_inr)
    profit_loss = Label(win, text=f"{P_L}")
    profit_loss.place(x=600, y=100+c)

def vraiables(i, data):
    cur_inr = float(data[i]["last"]) * crypto[i]
    spend_inr = inr[i]
    crypto_value = crypto[i]
    real_name = name[i]
    live = float(data[i]["last"])
    return real_name, crypto_value, cur_inr, spend_inr, live


def reloadapi():
    threading.Timer(0.1, reloadapi).start()
    response  = requests.get('https://api.wazirx.com/api/v2/tickers')

    data = response.json()
    colunm1 = Label(win, text="Coin Name")
    colunm1.place(x=15, y=50)

    colunm2 = Label(win, text="Crypto Value")
    colunm2.place(x=200, y=50)

    colunm3 = Label(win, text="Current Value")
    colunm3.place(x=300, y=50)

    colunm4 = Label(win, text="Spend Value")
    colunm4.place(x=400, y=50)

    colunm5 = Label(win, text="Live Value")
    colunm5.place(x=500, y=50)

    colunm6 = Label(win, text="Profit(+) | Loss(-)")
    colunm6.place(x=600, y=50)

    #Bitcoin
    real_name, crypto_value, cur_inr, spend_inr, live = vraiables("btcinr", data)
    portal(real_name, crypto_value, cur_inr, spend_inr, 25, live)

    #Ethereum
    real_name, crypto_value, cur_inr, spend_inr, live = vraiables("ethinr", data)
    portal(real_name, crypto_value, cur_inr, spend_inr, 50, live)

    real_name, crypto_value, cur_inr, spend_inr, live = vraiables("dogeinr", data)
    portal(real_name, crypto_value, cur_inr, spend_inr, 75, live)

    real_name, crypto_value, cur_inr, spend_inr, live = vraiables("wrxinr", data)
    portal(real_name, crypto_value, cur_inr, spend_inr, 100, live)

    real_name, crypto_value, cur_inr, spend_inr, live = vraiables("batinr", data)
    portal(real_name, crypto_value, cur_inr, spend_inr, 125, live)

    real_name, crypto_value, cur_inr, spend_inr, live = vraiables("dockinr", data)
    portal(real_name, crypto_value, cur_inr, spend_inr, 150, live)

    real_name, crypto_value, cur_inr, spend_inr, live = vraiables("xeminr", data)
    portal(real_name, crypto_value, cur_inr, spend_inr, 175, live)

    real_name, crypto_value, cur_inr, spend_inr, live = vraiables("trxinr", data)
    portal(real_name, crypto_value, cur_inr, spend_inr, 200, live)

    real_name, crypto_value, cur_inr, spend_inr, live = vraiables("shibinr", data)
    portal(real_name, crypto_value, cur_inr, spend_inr, 225, live)

    real_name, crypto_value, cur_inr, spend_inr, live = vraiables("scinr", data)
    portal(real_name, crypto_value, cur_inr, spend_inr, 250, live)

    real_name, crypto_value, cur_inr, spend_inr, live = vraiables("bttinr", data)
    portal(real_name, crypto_value, cur_inr, spend_inr, 275, live)





reloadapi()
win.mainloop()


