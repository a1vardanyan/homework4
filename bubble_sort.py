def bubble_sort(vec): 
    i = 0 
    N = len(vec) 
    while i < N: 
        for j in range(N-1): 
            if vec[j+1] < vec[j]: 
                vec[j], vec[j+1] = vec[j+1], vec[j] 
        i += 1 
    return vec
