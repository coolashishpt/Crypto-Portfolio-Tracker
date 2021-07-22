def values():
    name = {"btcinr": "Bitcoin (BTC)", "ethinr": "Ethereum (ETH)",
            "dogeinr": "Dogecoin (DOGE)", "wrxinr": "WazirX Token (WRX)",
            "batinr": "Basic Attention Token (BAT)",
            "dockinr": "Dock (DOCK)", "xeminr": "Nem (XEM)", "trxinr": "Tron (TRX)", "shibinr": "SHIBA INU (SHIB)",
            "scinr": "Siacoin (SC)", "bttinr": "BitTorrent (BTT)"}

    inrvalues = {"btcinr": 998, "ethinr": 394.8, "dogeinr": 80.3634, "trxinr": 395, "batinr": 933.413,
              "dockinr": 93.730, "wrxinr": 1485.3, "xeminr": 483.892,
             "shibinr": 166.999, "scinr": 494.08, "bttinr": 1070.89995}

    cryptovalue = {"btcinr": 0.00027, "ethinr": 0.0014, "dogeinr": 2, "trxinr": 40, "batinr": 10,
                "dockinr": 13, "wrxinr": 9, "xeminr": 19,
                "shibinr": 117771, "scinr": 193, "bttinr": 2055}
    return name, inrvalues, cryptovalue

name, inr, crypto = values()


# while True:
#     data = scrape.api()
#     for i in name:
#         cur_inr = float(data[i]["last"]) * crypto[i]
#         spend_inr = inr[i]
#         crypto_value = crypto[i]
#         real_name = name[i]
#         print(f"{real_name} : {crypto_value} | {cur_inr} | {spend_inr} P/L Value = {cur_inr - spend_inr}")



