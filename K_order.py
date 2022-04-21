def K_order(vec, K): 
    def recurs(vec, start, end, K): 
        same = [] 
        lower = [] 
        greater = []
        counter = 0
        if len(vec) > 1: 
            value = vec[(start+end)//2] 
            for element in vec: 
                if element < value: 
                    lower.append(element) 
                elif element > value: 
                    greater.append(element) 
                elif element == value:
                    same.append(element)
            if K < len(lower):
                return recurs(lower, 0, len(lower) - 1, K)
            elif K < len(lower + same):
                return same[0]
            else:
                count = len(lower + same)
                K -= count
                return recurs(greater, count, len(greater) - 1, K)
        else: 
            return vec[K]
    return recurs(vec, 0, len(vec) - 1, K)
