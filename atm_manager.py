
def count_coins(cash_result: list):
    coin_amount = 0
    for cash_elem in cash_result:
        if cash_elem.get('type') == 'COIN':
            coin_amount += cash_elem.get('amount')
    # print(coin_amount)
    return coin_amount


class Atm:
    def __init__(self):
        self.cash = [
            {'type': 'BILL', 'value': 200, 'amount': 2},
            {'type': 'BILL', 'value': 100, 'amount': 10},
            {'type': 'COIN', 'value': 10, 'amount': 5},
            {'type': 'COIN', 'value': 5, 'amount': 1},
            {'type': 'COIN', 'value': 1, 'amount': 10},
            {'type': 'COIN', 'value': 0.1, 'amount': 10},
            {'type': 'COIN', 'value': 0.01, 'amount': 5}
        ]
        self.cash_map = {self.cash[v].get('value'): v for v in range(len(self.cash))}

    def update_cash(self, cash_map: dict):
        for ind in cash_map.keys():
            # print(self.cash[ind]['amount'])
            self.cash[ind]['amount'] -= cash_map.get(ind)
        # print('cash')
        # print(self.cash)

    def put_money(self, cash_list: list):
        for cash in cash_list:
            value = cash.get('value')
            amount = cash.get('amount')
            ind = self.cash_map.get(int(value))
            self.cash[ind]['amount'] += int(amount)

    def count(self, money):
        result = []
        cash_map = {}
        cur_money = money
        for ind in range(len(self.cash)):
            temp_cash = {}
            type = self.cash[ind].get('type')
            value = self.cash[ind].get('value')
            amount = self.cash[ind].get('amount')
            res = (cur_money * 100) // (value * 100)
            if res >= 1:
                if res <= amount:
                    temp_cash['type'] = type
                    temp_cash['value'] = value
                    temp_cash['amount'] = int(res)
                    cur_money -= value * res
                    cur_money = round(cur_money, 2)
                    result.append(temp_cash)
                    cash_map[ind] = int(res)
                else:
                    if amount != 0:
                        temp_cash['type'] = type
                        temp_cash['value'] = value
                        temp_cash['amount'] = amount
                        cur_money -= value * amount
                        cur_money = round(cur_money, 2)
                        result.append(temp_cash)
                        cash_map[ind] = amount
            else:
                continue
        if cur_money > 0:
            res = 0
            for cash in self.cash:
                res += cash.get('value') * cash.get('amount')
            return res
        else:
            self.update_cash(cash_map=cash_map)
            # print(result)
            # print(cash_map)
            # print(self.cash_map)
            return result


if __name__ == '__main__':
    # count(110)
    # count(500)
    # count(450)
    # count(100.03)
    # count(116)
    # count(201.25)
    # count(837.44)
    atm = Atm()
    # atm.count(400)
    # atm.count(400)
    # atm.put_money([{'value': 200, 'amount': 4},
    #                {'value': 100, 'amount': 444},
    #                {'value': 10, 'amount': 40}])
    # atm.put_money(200, 10)
    # print(atm.count(10020.23))
    res = atm.count(1020.22)
    # print(res)
    count_coins(res)