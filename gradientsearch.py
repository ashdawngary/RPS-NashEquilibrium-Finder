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
    score = f(state)
    prevscore = float("inf")
    while abs(prevscore - score) > 0.0001:
        print "State: %s, score: %s diff(%s)"%(state,score,abs(prevscore - score))
        directions = []
        prevscore = score
        for increase_index in range(0,3):
            for decrease_index in range(0,3):
                if increase_index != decrease_index and (state[increase_index] + step) <= 1 and (state[decrease_index] - step) >= 0:
                    directions.append([float("inf"),list(state)])
                    directions[-1][1][increase_index] += step
                    directions[-1][1][decrease_index] -= step
                    directions[-1][0] = f(directions[-1][1])
        directions.sort(key = lambda a:a[0])
        optimal = directions[0]
        state = optimal[1]
        score = optimal[0]
    print abs(prevscore-score)
    return state
