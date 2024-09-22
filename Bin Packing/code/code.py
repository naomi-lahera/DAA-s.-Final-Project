def first_fit_decreasing(items, bin_capacity=1):
    items.sort(reverse=True)
    bins = []
    
    for item in items:
        placed = False
        for b in bins:
            if b + item <= bin_capacity:
                b += item  
                placed = True
                break
        
        if not placed:
            bins.append(item)
    
    return len(bins)