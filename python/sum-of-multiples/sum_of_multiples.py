def sum_of_multiples(limit, factors):
    # Generate list of multiples up to limit for each
    #   input and then sum the list
    multiples = []
    
    for f in factors:        
        multiplier = 1
        value = f

        while value < limit:        
            if value not in multiples:
                multiples.append(value)

            multiplier += 1
            value = f * multiplier
    
    return sum(multiples)
    
