// https://leetcode.com/problems/integer-to-english-words

from collections import deque
class Solution:  
    def __init__(self):
        self.one_digit = {
            '0': '', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', 
            '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
                }
        self.special_two_digit = {
            '10': 'Ten', '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen', 
            '15': 'Fifteen', '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen'
        }
        self.two_digit = {
            '0': '', '2': 'Twenty', '3': 'Thirty', '4': 'Forty', '5': 'Fifty',
            '6': 'Sixty', '7': 'Seventy', '8': 'Eighty', '9': 'Ninety'
        }

    def numberToWords(self, num):
        if num == 0:
            return 'Zero'
        str_num = str(num)
        no, thousand, million, billion = [], [], [], []
        for i in range(len(str_num)):
            idx = (len(str_num) - 1) - i
            if i // 3 == 0:
                no = [str_num[idx]] + no
            if i // 3 == 1:
                thousand = [str_num[idx]] + thousand
            if i // 3 == 2:
                million = [str_num[idx]] + million
            if i // 3 == 3:
                billion = [str_num[idx]] + billion

        ans = deque([])
        name_and_num = {'': no, 'Thousand': thousand, 'Million': million, 'Billion': billion}
        for name, item in name_and_num.items():
            tmp = []
            if len(item) == 0:
                continue

            elif len(item) == 3:
                if item[0] != '0':
                    tmp.append(self.one_digit[item[0]])
                    tmp.append('Hundred')
                if item[1] == '1':
                    tmp.append(self.special_two_digit[item[1] + item[2]])
                else:
                    tmp.append(self.two_digit[item[1]])
                    tmp.append(self.one_digit[item[2]])

            elif len(item) == 2:
                if item[0] == '1':
                    tmp.append(self.special_two_digit[item[0] + item[1]])
                else:
                    tmp.append(self.two_digit[item[0]])
                    tmp.append(self.one_digit[item[1]])

            elif len(item) == 1:
                tmp.append(self.one_digit[item[0]])
            
            if item != ['0', '0', '0']:
                tmp.append(name)
            for i in reversed(range(len(tmp))):
                if tmp[i] != '':
                    ans.appendleft(tmp[i])
        return ' '.join(ans).strip(' ')
