positives = filter(lambda x: x > 0, [1, -5, 0, 6, -2, 8])
print(repr(positives))  # filter object returns values lazily
print(list(positives))

# passing none as the first arg removes all elements that evaluate to false
trues = filter(None, [0, 1, False, True, [], [1,2,3], '', 'hello'])
print(list(trues))