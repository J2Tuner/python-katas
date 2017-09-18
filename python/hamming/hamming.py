def distance(strand1, strand2):
    if len(strand1) != len(strand2):
        raise ValueError
    
    mismatches = 0
    for i in range(len(strand1)):
        if strand1[i] != strand2[i]:
            mismatches += 1

    return mismatches
            
    
