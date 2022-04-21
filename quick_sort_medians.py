def quick_sort_median(vec, med): 
    def qs(vec, start, end): 
        same = [] 
        lower = [] 
        greater = [] 
        if len(vec) > med: 
            value = vec[np.median(random.sample(range(len(vec)-1), med)).astype(int)] 
            for element in vec: 
                if element < value: 
                    lower.append(element) 
                elif element > value: 
                    greater.append(element) 
                else: 
                    same.append(element) 
            return qs(lower, 0, len(lower) - 1) +  same + qs(greater, 0, len(greater) - 1)
        #if required med is higher than vec
        if 1 < len(vec) <= med: 
            value = vec[0] 
            for element in vec: 
                if element < value: 
                    lower.append(element) 
                elif element > value: 
                    greater.append(element) 
                else: 
                    same.append(element) 
            return qs(lower, 0, len(lower) - 1) +  same + qs(greater, 0, len(greater) - 1) 
        else: 
            return vec 
    return qs(vec, 0, len(vec) - 1)
