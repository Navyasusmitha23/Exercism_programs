def distance(strand_a, strand_b):
    if len(strand_a)!=len(strand_b):
        raise ValueError("Strands must be of equal length.")
    hamming_code = 0
    for letter1,letter2 in zip(strand_a,strand_b):
        if letter1 != letter2:
           hamming_code += 1
    return hamming_code
