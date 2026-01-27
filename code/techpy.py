import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
excel_file='tech.xlsm'

sheet_name='10 Year Historical data '

df_raw=pd.read_excel(excel_file, sheet_name=sheet_name, header=None)
num_stocks=len(df_raw.columns)//4

stocks_data={}

for i in range(num_stocks):
    col_start = i * 4
    stock_name = str(df_raw.iloc[0, col_start]).strip()
   
    raw_dates  = df_raw.iloc[2:, col_start]                 
    raw_prices = df_raw.iloc[2:, col_start+2]               
    dates  = pd.to_datetime(raw_dates,  errors='coerce')
    prices = pd.to_numeric(raw_prices, errors='coerce')

    df = pd.DataFrame({'Date': dates, 'Close': prices})
    df = df.dropna().sort_values('Date').reset_index(drop=True)

    df = df.set_index('Date')                                   
    df = df['Close'].asfreq('B', method='ffill')                
    df = df.to_frame('Close')                                  
    df = df.reset_index()     
                                
    stocks_data[stock_name] = df
    print(f"Loaded → {stock_name}  |  {len(df)} business days (gaps filled)")

def calculate_rsi(close, period=14 ):
    delta = close.diff()
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
    rs = gain / loss
    rsi= 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(close):
    exp1 = close.ewm(span=12, adjust=False).mean()
    exp2 = close.ewm(span=26, adjust=False).mean()
    macd = exp1 - exp2
    signal = macd.ewm(span=9, adjust=False).mean()
    return macd, signal 

def calculate_bollinger(close, period=20):
    sma = close.rolling(window=period).mean()
    std = close.rolling(window=period).std()
    upper = sma + (std * 2)
    lower = sma - (std * 2)
    return upper, sma, lower


for stock_name, df in stocks_data.items():
    df['RSI'] = calculate_rsi(df['Close'])
    df['MACD'], df['Signal'] = calculate_macd(df['Close'])
    df['BB_Upper'], df['BB_Middle'], df['BB_Lower'] = calculate_bollinger(df['Close'])

   
    fig = plt.figure(figsize=(28, 20))                   
    gs = fig.add_gridspec(4, 1, height_ratios=[3.5, 1, 1, 0.6], hspace=0.3)

    # 1. Price + Bollinger Bands
    ax1 = fig.add_subplot(gs[0])
    ax1.plot(df['Date'], df['Close'], color='black', linewidth=1.8, label='Adj Close')
    ax1.plot(df['Date'], df['BB_Upper'], color='#d62728', linestyle='--', alpha=0.8, label='Upper Band')
    ax1.plot(df['Date'], df['BB_Middle'], color='gray', alpha=0.9, label='Middle Band (20 SMA)')
    ax1.plot(df['Date'], df['BB_Lower'], color='#2ca02c', linestyle='--', alpha=0.8, label='Lower Band')
    ax1.fill_between(df['Date'], df['BB_Lower'], df['BB_Upper'], color='gray', alpha=0.07)
    ax1.set_ylabel('Bollinger Bands', fontsize=12)
    ax1.set_title(f'{stock_name} — 10-Year Technical Analysis', fontsize=18, fontweight='bold', pad=20)
    ax1.legend(frameon=True, fancybox=True, shadow=True, loc='upper left')
    ax1.grid(alpha=0.3)

    # 2. RSI
    ax2 = fig.add_subplot(gs[1], sharex=ax1)
    ax2.plot(df['Date'], df['RSI'], color='#9467bd', linewidth=1.5)
    ax2.axhline(70, color='red', linestyle='--', alpha=0.7)
    ax2.axhline(30, color='green', linestyle='--', alpha=0.7)
    ax2.axhline(50, color='gray', linestyle='-', alpha=0.4)
    ax2.fill_between(df['Date'], 70, 100, color='red', alpha=0.1)
    ax2.fill_between(df['Date'], 0, 30, color='green', alpha=0.1)
    ax2.set_ylabel('RSI', fontsize=12)
    ax2.set_ylim(0, 100)
    ax2.grid(alpha=0.3)

    # 3. MACD
    ax3 = fig.add_subplot(gs[2], sharex=ax1)
    hist = df['MACD'] - df['Signal']
    ax3.plot(df['Date'], df['MACD'], label='MACD', color='#1f77b4', linewidth=1.4)
    ax3.plot(df['Date'], df['Signal'], label='Signal', color='#ff7f0e', linewidth=1.4)
    colors = ['green' if x >= 0 else 'red' for x in hist]
    ax3.bar(df['Date'], hist, color=colors, alpha=0.6, width=3, label='Histogram')
    ax3.axhline(0, color='black', linewidth=0.8)
    ax3.set_ylabel('MACD', fontsize=12)
    ax3.legend(frameon=True, fancybox=True)
    ax3.grid(alpha=0.3)

    # 4. Info box
    ax4 = fig.add_subplot(gs[3])
    ax4.axis('off')
    info = (f"RSI        : {df['RSI'].iloc[-1]:.1f}\n"
            f"Data points: {len(df):,} business days")
    ax4.text(0, 0.5, info, fontsize=13, verticalalignment='center',
             bbox=dict(facecolor='beige', edgecolor='brown', boxstyle='round,pad=1'))

    # Final layout magic (removes the tiny-graph-on-the-left problem forever)
    plt.subplots_adjust(left=0.08, right=0.98, top=0.93, bottom=0.08)
    plt.xticks(rotation=45)

    safe_name = stock_name.replace("/", "_").replace(" ", "_")
    plt.savefig(f"{safe_name}_10Y.png", dpi=300, facecolor='white')
    plt.close(fig)