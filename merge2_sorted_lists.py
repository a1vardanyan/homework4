def merge_2sorted_lists(vec1, vec2): 
    i = 0 
    j = 0 
    N = len(vec1)  
    M = len(vec2) 
    c = [] 
    while i < N and j < M: 
        if vec1[i] < vec2[j]: 
            c.append(vec1[i]) 
            i += 1 
        else: 
            c.append(vec2[j]) 
            j += 1 
    if i == N and j != M: 
        c.extend(vec2[j:]) 
    else: 
        c.extend(vec1[i:]) 
    return c
