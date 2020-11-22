#!/usr/bin/python3

from setting import session
from zaiko import *
from uriage import *
from datetime import datetime
date = datetime.today()

zaiko = session.query(Zaiko).all()
def prin():
    print('------')

sum = 0
kago = []
count = []
k = {}
while True:

    prin()
    for tmp in zaiko:
        print(str(tmp.product_id) + ':', str(tmp.product_name), str(tmp.tanka) + 'yen')
    prin()

    num = input('input product_number:')
    nums = input('input product_quantity:')
    num = int(num)
    nums = int(nums)
    kago.append(num)
    count.append(nums)
    bought_pros = session.query(Zaiko).filter(Zaiko.product_id == num).one()
    bought_pro = bought_pros.tanka
    sum += int(bought_pro) * nums
    prin()
    print('sum: ' + str(sum) + 'yen')

    if num in k:
        k[num] += nums
    else:
        k[num] = nums
    a = list(k.keys())

    for i in a:
        b = session.query(Zaiko).filter(Zaiko.product_id == i).one()
        b = b.product_name
        print(b + ' : ' +str(k[i]))
    prin()

    g_zaiko = session.query(Zaiko).filter(Zaiko.product_id == num).one()
    g_zaiko.count -= int(nums)

    if g_zaiko.count <=  0:
        prin()
        print('sorry out of stock')
        prin()
        continue

    else:
        pass

    yn = input('continue shopping? [y/n] :')
    if yn == 'y':
        continue

    else:
        prin()
        print('byebye')
        prin()
        break

for i in range(len(kago)):
    g_uriage = session.query(Uriage).filter(Uriage.product_id == kago[i]).one()
    g_uriage.count += int(count[i])
g_uriage.product_id = num
g_uriage.date = date

session.add(g_zaiko)
session.add(g_uriage)

session.commit()