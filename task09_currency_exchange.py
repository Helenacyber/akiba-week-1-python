#Currency Exchange Desk
class exchange:
    exchange_rate= 150
    def __init__(self,usd_amount: int):
            self.usd_amount = usd_amount

    def currency_exchange(self):
        eth_amount= self.usd_amount/exchange_rate
        return eth_amount