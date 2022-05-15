class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if price == 95:
            import pdb
            pdb.set_trace()

        cur_price, cur_span = price, 1

        while self.stack and self.stack[-1][0] <= cur_price:
            prev_price, prev_span = self.stack.pop()
            cur_span += prev_span

        self.stack.append( (cur_price, cur_span) )
        
        return cur_span