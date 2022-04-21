def quick_sort(vec): 
    def qs(vec, start, end): 
        same = [] 
        lower = [] 
        greater = [] 
        if len(vec) > 1: 
            value = vec[(start + end) // 2]
            #value = vec[np.random.randint(0, len(vec)-1, 1)] 
            for element in vec: 
                if element < value: 
                    lower.append(element) 
                elif element > value: 
                    greater.append(element) 
                elif element == value: 
                    same.append(element) 
            return qs(lower, 0, len(lower) - 1) +  same + qs(greater, 0, len(greater) - 1) 
        else: 
            return vec 
    return qs(vec, 0, len(vec) - 1)
