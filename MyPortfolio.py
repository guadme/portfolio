# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import configparser

config = configparser.RawConfigParser()
config.read('ConfigFile.properties')


#os.chdir(r'C:\Users\guill\Desktop\streamlit')

st.markdown('''# **Portfolio tracker**
Hi *Guillermo*, welcome back  to your crypto portfolio information and analytics.
''')

# Load market data from Binance and Conigecko API
df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')
df_adax = pd.read_json('https://api.coingecko.com/api/v3/simple/price?ids=adax&vs_currencies=eur&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true')
df_vet_eur = df.loc[df["symbol"] == "VETEUR"]

#Set holding variables

vet_amount = float(#insert num of vet coins)
adax_amount = float(#insert num of adax coin)

vet_investment = float(#inser vet investment)
adax_investment = float(#insert adax investment)
total_investment = vet_investment + adax_investment

auxx1, header1, auxx2 = st.columns(3)

header1.header('**Tokens price**')

price_col1 , price_col2 = st.columns(2)

col1_name = 'VETEUR'
col2_name = 'ADAXEUR'

col1_price = round(float(df_vet_eur['lastPrice']),4)
col2_price = round(float(df_adax.loc['eur']),4)

col1_percent = f'{round(float(df_vet_eur["priceChangePercent"]),2)}%'
col2_percent = f'{round(float(df_adax.loc["eur_24h_change"]),2)}%'

price_col1.metric(col1_name,col1_price,col1_percent)
price_col2.metric(col2_name,col2_price,col2_percent)


vet_money_aux = vet_amount * col1_price
adax_money_aux = adax_amount * col2_price
total_money_aux = vet_money_aux + adax_money_aux

vet_money = f'{round(vet_amount * col1_price,2)}€'
adax_money = f'{round(adax_amount * col2_price,2)}€'
total_money = f'{round(vet_money_aux + adax_money_aux,2)}€'


col1_holdings_name = "Vechain investment performance"
col2_holdings_name = "Adax investment performance"

vet_money_percent = f'{round(((vet_money_aux - vet_investment)/vet_money_aux)*100,3)}%'
adax_money_percent =f'{round(((adax_money_aux - adax_investment)/adax_money_aux)*100,3)}%'
total_money_percent = f'{round(((total_money_aux - total_investment)/total_money_aux)*100,3)}%'


aux1, title2col, aux2 = st.columns(3)
title2col.header('**Your holdings**')

holdings_col1 , holdings_col2, holdings_col3 = st. columns(3)

holdings_col11 , holdings_col21, holdings_col31 = st. columns(3)
holdings_col111 , holdings_col211, holdings_col311 = st. columns(3)
 
holdings_col1.subheader('VeChain Investment: ')
holdings_col2.subheader("ADAX investment: ")
holdings_col3.subheader("Total investment: ")

holdings_col11.subheader(f'{vet_investment}€')
holdings_col21.subheader(f'{adax_investment}€')
holdings_col31.subheader(f'{total_investment}€')

holdings_col111.metric('Current VET balance', vet_money, vet_money_percent)
holdings_col211.metric('Current ADAX balance', adax_money, adax_money_percent)
holdings_col311.metric('Current total balance', total_money, total_money_percent)
