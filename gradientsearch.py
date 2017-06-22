def f(a):
    '''
    A is our mixed strategy
    a = [D,E,F]
    output -> max(F-E, D - F,E-D)
    For RPS, we said that F(a) = max()
    '''
    D = a[0]
    E = a[1]
    F = a[2]
    return max(F-E,D-F,E-D)
def gradientsearch():
    state = [1,0,0]
    step = 0.001
    score = f(a)
    prevscore = float("inf")
    while abs(prevscore - score) > 0:
        directions = []
        prevscore = score
        for increase_index in range(0,3):
            for decrease_index in range(0,3):
                if increase_index != decrease_index and (state[increase_index] + step) <= 1 and (state[decrease_index] - step) >= 0:
                    directions.apend([float("inf"),list(state)])
                    directions[-1][1][increase_index] += step
                    directions[-1][1][decrease_index] -= step
                    
