import sys

n = int(input())
mobile_prices_per_years = list(map(int, input().split()))

min_price = (2 ** 31) - 1
when_purchased_index = len(mobile_prices_per_years) - 1

for i in range(len(mobile_prices_per_years)):
    if min_price > mobile_prices_per_years[i]:
        min_price = mobile_prices_per_years[i]
        when_purchased_index = i

if when_purchased_index == len(mobile_prices_per_years) - 1:
    print("0")
    sys.exit()

after_purchasing_max_price = 0

for price in mobile_prices_per_years[when_purchased_index + 1:]:
    if after_purchasing_max_price <= price:
        after_purchasing_max_price = price

if after_purchasing_max_price - min_price <= 0:
    print("0")
else:
    print(after_purchasing_max_price - min_price)