#Currency Exchange Desk
class exchange:
    exchange_rate= 150
    def __init__(self,usd_amount: int):
            self.usd_amount = usd_amount

    def currency_exchange(self):
        eth_amount= self.usd_amount/self.exchange_rate
        return eth_amount

    def __str__(self):
        print('=' *40)
        print('      CURRENCY EXCHANGE')
        print('=' *40)
        print(f'USD Amount: {self.usd_amount}')
        print(f'Exchange Rate: 1 USD ={self.exchange_rate}* ETB')
        print(f'ETH Amount: {self.currency_exchange()} ETB')   
        print('=' *40)

exchange_rate = float(input('Enter the exchange rate: '))
currency = exchange(100)
print(currency.__str__())