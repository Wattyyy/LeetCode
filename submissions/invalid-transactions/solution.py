// https://leetcode.com/problems/invalid-transactions

from collections import defaultdict

class Solution(object):
    def invalidTransactions(self, transactions):
        if not transactions:
            return []
        # name -> [[time, amount, city, is_invalid], [time, amount, city, is_invalid]...]
        record = defaultdict(list)
        for item in transactions:
            name, time, amount, city = item.split(",")
            tmp_list = [time, amount, city, False]
            if int(amount) >= 1000:
                tmp_list[-1] = True
            for item in record[name]:
                if (abs(int(item[0]) - int(time)) <= 60) and (city != item[2]):
                    item[-1] = True
                    tmp_list[-1] = True
            record[name].append(tmp_list)

        ans = []
        for name in record.keys():
            for item in record[name]:
                if item[-1]:
                    transaction = [name] + item[:-1]
                    string = ",".join(transaction)
                    ans.append(string)
        return ans       