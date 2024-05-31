def transform(legacy_data):
    new_scores = {}
    for score, letters in legacy_data.items():
        for letter in letters:
            new_scores[letter.lower()] = score
    return new_scores
