def jaccard_similarity(set_a, set_b):

    set_a = set(set_a)
    set_b = set(set_b)

    union = set_a | set_b
    
    denominator = len(union)
    if denominator==0:
        return 0

    intersection = set_a & set_b
    numerator = len(intersection)

    return numerator/denominator
   