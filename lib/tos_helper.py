def create_pricelist(hist_price):
    return [candle['close'] for candle in hist_price['candles']]