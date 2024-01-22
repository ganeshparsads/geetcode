class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_set = set(order)
        
        order_strings = []
        rest_order = []
        
        
        for i in s:
            if i in order_set:
                order_strings.append(i)
            else:
                rest_order.append(i)
        
        ord_cnt = dict(Counter(order_strings))
        
        result = []
        
        for i in order:
            if i in ord_cnt:
                result.append(i*ord_cnt[i])
            
        result += rest_order
        
        return ''.join(result)
                