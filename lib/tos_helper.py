def create_pricelist(hist_price: float | str) -> list[float | str]:
    output_ls = []
    for candle in hist_price['candles']:
        output_ls.append(candle['close'])
    return output_ls