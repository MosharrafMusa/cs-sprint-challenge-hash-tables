def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for i, weight in enumerate(weights):
        total = limit - weight
        if total in cache:
            x = cache[total]
            return (i, x)
        else:
            cache[weight] = i

    return None


print(get_indices_of_item_weights([3, 6, 9, 12, 17], 6, 18))
