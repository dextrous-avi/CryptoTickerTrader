from bittrex.bittrex import Bittrex, API_V2_0, API_V1_1


API_KEY = 'API KEY'
API_SECRET = 'SECRET KEY'
PERCENT_BUY = 0.5

bittrex_obj_api1 = Bittrex(API_KEY, API_SECRET, api_version=API_V1_1)
bittrex_obj_api2 = Bittrex(API_KEY, API_SECRET, api_version=API_V2_0)
set_coin_call = 'BTC-NEO'

set_coin_call_val = 2
coin_ticker_value_obj = bittrex_obj_api1.get_ticker(set_coin_call)
coin_ticker_last_val = coin_ticker_value_obj['result']['Last']
#print(json.dumps(my_balance, sort_keys=True, indent=4))
btc_bal = bittrex_obj_api2.get_balance('BTC')
my_holding_btc = '{:10.8f}'.format(btc_bal['result']['Balance'])
last_updated_my_holding = btc_bal['result']['Updated']
print('You have %s BTC, last updated at %s' % (my_holding_btc, last_updated_my_holding))
if btc_bal['result']['Balance'] > 0:
    print('You have some funds to trade')
    if set_coin_call_val >= coin_ticker_last_val:
        print('Finally, its right time to purchase as per your set value')
        invest_btc = PERCENT_BUY * btc_bal['result']['Balance']
        print(set_coin_call, invest_btc, coin_ticker_last_val)
        trade_buy_obj = bittrex_obj_api2.trade_buy(set_coin_call, order_type='LIMIT', quantity=invest_btc, rate=coin_ticker_last_val, time_in_effect='GOOD_TIL_CANCELLED')
        print(trade_buy_obj)
        open_order_obj = bittrex_obj_api2.get_open_orders(set_coin_call)
        print(open_order_obj)
        if len(open_order_obj['result']) > 0:
            open_order_uuid = open_order_obj['result'][0]['OrderUuid']
            cancel_order = bittrex_obj_api2.cancel(open_order_uuid)
            print(cancel_order)
        else:
            print('No Open orders')






else:
    print('Sorry, deposit some BTC')
#print(json.dumps(btc_price, sort_keys=True, indent=4))
