# importing whole module
from tkinter import *
from tkinter.ttk import *
import calculator

# importing strftime function to
# retrieve system's time
from time import strftime
import time
# creating tkinter window
win = Tk()
win.title('CryptoCurrency')
win.geometry('800x480')
import requests

# This function is used to
# display time on the label

name, inr, crypto = calculator.values()


def vraiables(i, data):
    cur_inr = float(data[i]["last"]) * crypto[i]
    spend_inr = inr[i]
    crypto_value = crypto[i]
    real_name = name[i]
    live = float(data[i]["last"])
    return real_name, crypto_value, cur_inr, spend_inr, live

def percentage(x, y):
    value = (x/y * 100) - 100
    return "{:.2f}".format(value)


def LIVE():
    string = strftime('%H:%M:%S %p')
    # title.config(text = string)
    response = requests.get('https://api.wazirx.com/api/v2/tickers')
    data = response.json()


    colunm1 = Label(win, text="Coin Name", font=('calibri', 10, 'bold'))
    colunm1.place(x=15, y=75)

    colunm2 = Label(win, text="Crypto Value", font=('calibri', 10, 'bold'))
    colunm2.place(x=200, y=75)

    colunm3 = Label(win, text="Current Value", font=('calibri', 10, 'bold'))
    colunm3.place(x=300, y=75)

    colunm4 = Label(win, text="Spend Value", font=('calibri', 10, 'bold'))
    colunm4.place(x=400, y=75)

    colunm5 = Label(win, text="Live Value", font=('calibri', 10, 'bold'))
    colunm5.place(x=500, y=75)

    colunm6 = Label(win, text="Profit(+) | Loss(-)", font=('calibri', 10, 'bold'))
    colunm6.place(x=600, y=75)

    title = Label(win, text="CryptoFroce.Ai", font=('calibri', 17, 'bold'))
    title.place(x=300, y=10)

    time = Label(win, text=f"{string}", font=('calibri', 12, 'bold'))
    time.place(x=700, y=30)

    text = Label(win, text="TOTAL", font=('calibri', 12, 'bold'))
    text.place(x=500, y=400)

    # btc = Label(win, text=f"{btcinr}")
    # btc.place(x=500, y=100)
    # btc.after(1000, LIVE)

    # Bitcoin
    real_name_btc, crypto_value_btc, cur_inr_btc, spend_inr_btc, live_btc = vraiables("btcinr", data)
    cryptoname_btc = Label(win, text=f"{real_name_btc}", background='purple', foreground='white')
    cryptoname_btc.place(x=15, y=100 + 25)

    C_V_btc = "{:.5f}".format(crypto_value_btc)
    cryptovalue_btc = Label(win, text=f"{C_V_btc}", background='purple', foreground='white')
    cryptovalue_btc.place(x=200, y=100 + 25)

    C_I_btc = "{:.2f}".format(cur_inr_btc)
    curinr_btc = Label(win, text=f"{C_I_btc}", background='purple', foreground='white')
    curinr_btc.place(x=300, y=100 + 25)

    S_I_btc = "{:.2f}".format(spend_inr_btc)
    spendinr_btc = Label(win, text=f"{S_I_btc}", background='purple', foreground='white')
    spendinr_btc.place(x=400, y=100 + 25)

    LIVE_btc = "{:.4f}".format(live_btc)
    live1_btc = Label(win, text=f"{LIVE_btc}", background='purple', foreground='white')
    live1_btc.place(x=500, y=100 + 25)

    P_L_btc = "{:.5f}".format(cur_inr_btc - spend_inr_btc)
    profit_loss_btc = Label(win, text=f"{P_L_btc}    {percentage(cur_inr_btc, spend_inr_btc)}%", background='purple', foreground='white')
    profit_loss_btc.place(x=600, y=100 + 25)

    # Ethereum
    real_name_eth, crypto_value_eth, cur_inr_eth, spend_inr_eth, live_eth = vraiables("ethinr", data)
    cryptoname_eth = Label(win, text=f"{real_name_eth}", background='purple', foreground='white')
    cryptoname_eth.place(x=15, y=100 + 50)

    C_V_eth = "{:.5f}".format(crypto_value_eth)
    cryptovalue_eth = Label(win, text=f"{C_V_eth}", background='purple', foreground='white')
    cryptovalue_eth.place(x=200, y=100 + 50)

    C_I_eth = "{:.2f}".format(cur_inr_eth)
    curinr_eth = Label(win, text=f"{C_I_eth}", background='purple', foreground='white')
    curinr_eth.place(x=300, y=100 + 50)

    S_I_eth = "{:.2f}".format(spend_inr_eth)
    spendinr_eth = Label(win, text=f"{S_I_eth}", background='purple', foreground='white')
    spendinr_eth.place(x=400, y=100 + 50)

    LIVE_eth = "{:.4f}".format(live_eth)
    live1_eth = Label(win, text=f"{LIVE_eth}", background='purple', foreground='white')
    live1_eth.place(x=500, y=100 + 50)

    P_L_eth = "{:.5f}".format(cur_inr_eth - spend_inr_eth)
    profit_loss_eth = Label(win, text=f"{P_L_eth}    {percentage(cur_inr_eth, spend_inr_eth)}%", background='purple', foreground='white')
    profit_loss_eth.place(x=600, y=100 + 50)

    # Dogecoin
    real_name_doge, crypto_value_doge, cur_inr_doge, spend_inr_doge, live_doge = vraiables("dogeinr", data)
    cryptoname_doge = Label(win, text=f"{real_name_doge}")
    cryptoname_doge.place(x=15, y=100 + 75)

    C_V_doge = "{:.5f}".format(crypto_value_doge)
    cryptovalue_doge = Label(win, text=f"{C_V_doge}")
    cryptovalue_doge.place(x=200, y=100 + 75)

    C_I_doge = "{:.2f}".format(cur_inr_doge)
    curinr_doge = Label(win, text=f"{C_I_doge}")
    curinr_doge.place(x=300, y=100 + 75)

    S_I_doge = "{:.2f}".format(spend_inr_doge)
    spendinr_doge = Label(win, text=f"{S_I_doge}")
    spendinr_doge.place(x=400, y=100 + 75)

    LIVE_doge = "{:.4f}".format(live_doge)
    live1_doge = Label(win, text=f"{LIVE_doge}")
    live1_doge.place(x=500, y=100 + 75)

    P_L_doge = "{:.5f}".format(cur_inr_doge - spend_inr_doge)
    profit_loss_doge = Label(win, text=f"{P_L_doge}     {percentage(cur_inr_doge, spend_inr_doge)}%")
    profit_loss_doge.place(x=600, y=100 + 75)

    # WazirX Token
    real_name_wrx, crypto_value_wrx, cur_inr_wrx, spend_inr_wrx, live_wrx = vraiables("wrxinr", data)
    cryptoname_wrx = Label(win, text=f"{real_name_wrx}")
    cryptoname_wrx.place(x=15, y=100 + 100)

    C_V_wrx = "{:.5f}".format(crypto_value_wrx)
    cryptovalue_wrx = Label(win, text=f"{C_V_wrx}")
    cryptovalue_wrx.place(x=200, y=100 + 100)

    C_I_wrx = "{:.2f}".format(cur_inr_wrx)
    curinr_wrx = Label(win, text=f"{C_I_wrx}")
    curinr_wrx.place(x=300, y=100 + 100)

    S_I_wrx = "{:.2f}".format(spend_inr_wrx)
    spendinr_wrx = Label(win, text=f"{S_I_wrx}")
    spendinr_wrx.place(x=400, y=100 + 100)

    LIVE_wrx = "{:.4f}".format(live_wrx)
    live1_wrx = Label(win, text=f"{LIVE_wrx}")
    live1_wrx.place(x=500, y=100 + 100)

    P_L_wrx = "{:.5f}".format(cur_inr_wrx - spend_inr_wrx)
    profit_loss_wrx = Label(win, text=f"{P_L_wrx}    {percentage(cur_inr_wrx, spend_inr_wrx)}%")
    profit_loss_wrx.place(x=600, y=100 + 100)

    # Basic Attention Token
    real_name_bat, crypto_value_bat, cur_inr_bat, spend_inr_bat, live_bat = vraiables("batinr", data)
    cryptoname_bat = Label(win, text=f"{real_name_bat}")
    cryptoname_bat.place(x=15, y=100 + 125)

    C_V_bat = "{:.5f}".format(crypto_value_bat)
    cryptovalue_bat = Label(win, text=f"{C_V_bat}")
    cryptovalue_bat.place(x=200, y=100 + 125)

    C_I_bat = "{:.2f}".format(cur_inr_bat)
    curinr_bat = Label(win, text=f"{C_I_bat}")
    curinr_bat.place(x=300, y=100 + 125)

    S_I_bat = "{:.2f}".format(spend_inr_bat)
    spendinr_bat = Label(win, text=f"{S_I_bat}")
    spendinr_bat.place(x=400, y=100 + 125)

    LIVE_bat = "{:.4f}".format(live_bat)
    live1_bat = Label(win, text=f"{LIVE_bat}")
    live1_bat.place(x=500, y=100 + 125)

    P_L_bat = "{:.5f}".format(cur_inr_bat - spend_inr_bat)
    profit_loss_bat = Label(win, text=f"{P_L_bat}    {percentage(cur_inr_bat, spend_inr_bat)}%")
    profit_loss_bat.place(x=600, y=100 + 125)

    # Dock
    real_name_dock, crypto_value_dock, cur_inr_dock, spend_inr_dock, live_dock = vraiables("dockinr", data)
    cryptoname_dock = Label(win, text=f"{real_name_dock}")
    cryptoname_dock.place(x=15, y=100 + 150)

    C_V_dock = "{:.5f}".format(crypto_value_dock)
    cryptovalue_dock = Label(win, text=f"{C_V_dock}")
    cryptovalue_dock.place(x=200, y=100 + 150)

    C_I_dock = "{:.2f}".format(cur_inr_dock)
    curinr_dock = Label(win, text=f"{C_I_dock}")
    curinr_dock.place(x=300, y=100 + 150)

    S_I_dock = "{:.2f}".format(spend_inr_dock)
    spendinr_dock = Label(win, text=f"{S_I_dock}")
    spendinr_dock.place(x=400, y=100 + 150)

    LIVE_dock = "{:.4f}".format(live_dock)
    live1_dock = Label(win, text=f"{LIVE_dock}")
    live1_dock.place(x=500, y=100 + 150)

    P_L_dock = "{:.5f}".format(cur_inr_dock - spend_inr_dock)
    profit_loss_dock = Label(win, text=f"{P_L_dock}     {percentage(cur_inr_dock, spend_inr_dock)}%")
    profit_loss_dock.place(x=600, y=100 + 150)

    # Nem (XEM)
    real_name_xem, crypto_value_xem, cur_inr_xem, spend_inr_xem, live_xem = vraiables("xeminr", data)
    cryptoname_xem = Label(win, text=f"{real_name_xem}")
    cryptoname_xem.place(x=15, y=100 + 175)

    C_V_xem = "{:.5f}".format(crypto_value_xem)
    cryptovalue_xem = Label(win, text=f"{C_V_xem}")
    cryptovalue_xem.place(x=200, y=100 + 175)

    C_I_xem = "{:.2f}".format(cur_inr_xem)
    curinr_xem = Label(win, text=f"{C_I_xem}")
    curinr_xem.place(x=300, y=100 + 175)

    S_I_xem = "{:.2f}".format(spend_inr_xem)
    spendinr_xem = Label(win, text=f"{S_I_xem}")
    spendinr_xem.place(x=400, y=100 + 175)

    LIVE_xem = "{:.4f}".format(live_xem)
    live1_xem = Label(win, text=f"{LIVE_xem}")
    live1_xem.place(x=500, y=100 + 175)

    P_L_xem = "{:.5f}".format(cur_inr_xem - spend_inr_xem)
    profit_loss_xem = Label(win, text=f"{P_L_xem}    {percentage(cur_inr_xem, spend_inr_xem)}%")
    profit_loss_xem.place(x=600, y=100 + 175)

    # Tron
    real_name_trx, crypto_value_trx, cur_inr_trx, spend_inr_trx, live_trx = vraiables("trxinr", data)
    cryptoname_trx = Label(win, text=f"{real_name_trx}")
    cryptoname_trx.place(x=15, y=100 + 200)

    C_V_trx = "{:.5f}".format(crypto_value_trx)
    cryptovalue_trx = Label(win, text=f"{C_V_trx}")
    cryptovalue_trx.place(x=200, y=100 + 200)

    C_I_trx = "{:.2f}".format(cur_inr_trx)
    curinr_trx = Label(win, text=f"{C_I_trx}")
    curinr_trx.place(x=300, y=100 + 200)

    S_I_trx = "{:.2f}".format(spend_inr_trx)
    spendinr_trx = Label(win, text=f"{S_I_trx}")
    spendinr_trx.place(x=400, y=100 + 200)

    LIVE_trx = "{:.4f}".format(live_trx)
    live1_trx = Label(win, text=f"{LIVE_trx}")
    live1_trx.place(x=500, y=100 + 200)

    P_L_trx = "{:.5f}".format(cur_inr_trx - spend_inr_trx)
    profit_loss_trx = Label(win, text=f"{P_L_trx}    {percentage(cur_inr_trx, spend_inr_trx)}%")
    profit_loss_trx.place(x=600, y=100 + 200)

    # SHIBA INU
    real_name_shib, crypto_value_shib, cur_inr_shib, spend_inr_shib, live_shib = vraiables("shibinr", data)
    cryptoname_shib = Label(win, text=f"{real_name_shib}")
    cryptoname_shib.place(x=15, y=100 + 225)

    C_V_shib = "{:.5f}".format(crypto_value_shib)
    cryptovalue_shib = Label(win, text=f"{C_V_shib}")
    cryptovalue_shib.place(x=200, y=100 + 225)

    C_I_shib = "{:.2f}".format(cur_inr_shib)
    curinr_shib = Label(win, text=f"{C_I_shib}")
    curinr_shib.place(x=300, y=100 + 225)

    S_I_shib = "{:.2f}".format(spend_inr_shib)
    spendinr_shib = Label(win, text=f"{S_I_shib}")
    spendinr_shib.place(x=400, y=100 + 225)

    LIVE_shib = "{:.4f}".format(live_shib)
    live1_shib = Label(win, text=f"{LIVE_shib}")
    live1_shib.place(x=500, y=100 + 225)

    P_L_shib = "{:.5f}".format(cur_inr_shib - spend_inr_shib)
    profit_loss_shib = Label(win, text=f"{P_L_shib}    {percentage(cur_inr_shib, spend_inr_shib)}%")
    profit_loss_shib.place(x=600, y=100 + 225)

    # Siacoin
    real_name_sc, crypto_value_sc, cur_inr_sc, spend_inr_sc, live_sc = vraiables("scinr", data)
    cryptoname_sc = Label(win, text=f"{real_name_sc}")
    cryptoname_sc.place(x=15, y=100 + 250)

    C_V_sc = "{:.5f}".format(crypto_value_sc)
    cryptovalue_sc = Label(win, text=f"{C_V_sc}")
    cryptovalue_sc.place(x=200, y=100 + 250)

    C_I_sc = "{:.2f}".format(cur_inr_sc)
    curinr_sc = Label(win, text=f"{C_I_sc}")
    curinr_sc.place(x=300, y=100 + 250)

    S_I_sc = "{:.2f}".format(spend_inr_sc)
    spendinr_sc = Label(win, text=f"{S_I_sc}")
    spendinr_sc.place(x=400, y=100 + 250)

    LIVE_sc = "{:.4f}".format(live_sc)
    live1_sc = Label(win, text=f"{LIVE_sc}")
    live1_sc.place(x=500, y=100 + 250)

    P_L_sc = "{:.5f}".format(cur_inr_sc - spend_inr_sc)
    profit_loss_sc = Label(win, text=f"{P_L_sc}    {percentage(cur_inr_sc, spend_inr_sc)}%")
    profit_loss_sc.place(x=600, y=100 + 250)

    # BitTorrent
    real_name_btt, crypto_value_btt, cur_inr_btt, spend_inr_btt, live_btt = vraiables("bttinr", data)
    cryptoname = Label(win, text=f"{real_name_btt}")
    cryptoname.place(x=15, y=100 + 275)

    C_V_btt = "{:.5f}".format(crypto_value_btt)
    cryptovalue_btt = Label(win, text=f"{C_V_btt}")
    cryptovalue_btt.place(x=200, y=100 + 275)

    C_I_btt = "{:.2f}".format(cur_inr_btt)
    curinr_btt = Label(win, text=f"{C_I_btt}")
    curinr_btt.place(x=300, y=100 + 275)

    S_I_btt = "{:.2f}".format(spend_inr_btt)
    spendinr_btt = Label(win, text=f"{S_I_btt}")
    spendinr_btt.place(x=400, y=100 + 275)

    LIVE_btt = "{:.4f}".format(live_btt)
    live1_btt = Label(win, text=f"{LIVE_btt}")
    live1_btt.place(x=500, y=100 + 275)

    P_L_btt = "{:.5f}".format(cur_inr_btt - spend_inr_btt)
    profit_loss_btt = Label(win, text=f"{P_L_btt}    {percentage(cur_inr_btt, spend_inr_btt)}%")
    profit_loss_btt.place(x=600, y=100 + 275)

    sum  = float(P_L_btc) + float(P_L_sc) + float(P_L_bat) + float(P_L_dock) + float(P_L_btt) + float(P_L_doge) + float(P_L_eth) + float(P_L_shib) + float(P_L_trx) + float(P_L_wrx) + float(P_L_xem)
    total = "{:.5f}".format(sum)
    total_val = Label(win, text=f"{total} ₹", font=('calibri', 12, 'bold'))
    total_val.place(x=600, y=100+300)

    time.after(3000, LIVE)

    # time.sleep(1)
# Styling the label widget so that clock
# will look more attractive
# lbl = Label(win, font=('calibri', 10, 'bold'), background='purple', foreground='white')

# Placing clock at the centre
# of the tkinter window

LIVE()

mainloop()
