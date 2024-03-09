"""
In this analysis I'll go through nifty daily data and analys the effect of topped up SIPs during down months

"""
import pandas as pd

DATA_DIR = 'nifty/data/'
NIFTY_50_10 = pd.read_csv(DATA_DIR + 'NIFTY_50_Historical_PR_01012000to31122010.csv')
NIFTY_50_24 = pd.read_csv(DATA_DIR + 'NIFTY_50_Historical_PR_01012011to29022024.csv')

SIP = 1000

nifty_df = pd.concat([NIFTY_50_10, NIFTY_50_24], ignore_index=True)

# Data type conversion
#TODO: convert using flour/ceiling for accuracy
convert_dict = {
                'Open': int,
                'High': int,
                'Low': int,
                'Close': int
                }

nifty_df = nifty_df.astype(convert_dict)
nifty_df['Date'] = pd.to_datetime(nifty_df['Date'])

nifty_df.sort_values(by="Date", inplace=True)
nifty_df = nifty_df.reset_index(drop=True)


running_high = 0
for i, row in nifty_df.iterrows():
    if row['High'] > running_high:
        running_high = row['High']
        print(row['Date'], running_high)
    # print(row)

# print(running_high)

# print(nifty_df)

# print("Hello from github codespace.")