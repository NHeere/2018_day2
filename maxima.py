def find_maxima(x):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 2, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    Input arguments:
        x -- 1D list numbers

    Output:
        idx -- list of indices of the local maxima in x
    """

    idx = []
    possible_idx = []
    upstep = False
    for i in range(len(x)):
        if i == len(x) - 1:
            if x[i-1] < x[i]:
                idx.append(i)
        elif i == 0:
            if x[i+1] < x[i]:
                idx.append(i)
        # `i` is a local maximum if the signal decreases before and after it
        elif x[i-1] < x[i] and x[i+1] < x[i]:
            idx.append(i)
        elif x[i-1] < x[i] and x[i+1] == x[i]:
            upstep = True
            possible_idx.append(i)
        elif upstep and x[i-1] == x[i] and x[i+1] == x[i]:
            possible_idx.append(i)
        elif upstep and x[i-1] == x[i] and x[i+1] < x[i]:
            possible_idx.append(i)
            idx.extend(possible_idx)
            upstep = False
            possible_idx = []
        elif upstep and x[i-1] == x[i] and x[i+1] > x[i]:
            possible_idx = []
            upstep = False


    return idx
