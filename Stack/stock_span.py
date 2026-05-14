"""
The stock span problem is a financial problem where 
we have a series of n daily price quotes for a stock 
and we need to calculate the span of the stock’s price 
for all n days. The span Si of the stock’s price on a 
given day i is defined as the maximum number of consecutive 
days just before the given day, for which the price of the 
stock on the current day is less than its price on the given day. 
"""

def stock_span(arr):
    stack = []
    stack.append(0)
    print(1, end=" ")
    n = len(arr)

    for i in range(1, n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        span = i + 1 if len(stack) == 0 else i - stack[-1]
        print(span, end=" ")
        stack.append(i)
    