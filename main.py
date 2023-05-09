import pandas as pd
from cal_indicators import *
from get_price import save_price_data_to_csv
from plots import *

# read the price data from price_data.csv
price_data = pd.read_csv('price_data.csv')

# add sma indicators
# price_data = squeeze_momentum_indicator(price_data)
# price_data = calculate_moving_averages(price_data,'close',5, 20)
price_data = calculate_ema(price_data,'close',25)
price_data = calculate_ema(price_data,'close',50)

price_data = generate_signals(price_data, 'EMA25','EMA50')

# save_price_data_to_csv(price_data, filename='price_data_with_indicator.csv')

# plot the price data
# plot_squeeze_momentum(price_data)
plot_combined(price_data,'EMA25','EMA50')

# Backtesting the strategy
start_day = '2022-11-16 05:00:00'
end_day = '2023-05-09 17:00:00'

price_data_filtered = price_data[(price_data['time'] >= start_day) & (price_data['time'] <= end_day)]

profit_loss = backtest(price_data_filtered)
print(f"Total profit/loss: {profit_loss}")