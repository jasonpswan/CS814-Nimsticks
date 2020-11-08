import time

def remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list

def successors(state):
    result = []
    player = 0
    
    if state[-1] == 1:
        player = 2
    else:
        player = 1
    
    for i in range(len(state[0])):
        
        if state[0][i] >= 3:
            copied = state[0].copy()
            copied[i] = copied[i] - 3
            if copied[i] != 0:
                copied.sort()
                result.append((copied, player))
            else:
                copied.pop(i)
                copied.sort()
                result.append((copied, player))
                
        if state[0][i] >= 2:
            copied = state[0].copy()
            copied[i] = copied[i] - 2
            if copied[i] != 0:
                copied.sort()
                result.append((copied, player))
            else:
                copied.pop(i)
                copied.sort()
                result.append((copied, player))
        
        if state[0][i] >= 1:
            copied = state[0].copy()
            copied[i] = copied[i] - 1
            if copied[i] != 0:
                copied.sort()
                result.append((copied, player))
            else:
                copied.pop(i)
                copied.sort()
                result.append((copied, player))
                
    result = remove(result)
    return result

def terminal_test(state):
    if state == (([], 1)) or state == (([1], 2)) or state == state == (([], 2)) or state == (([1], 1)):
        return True
    else:
        return False
    
def utility(state):
    if state == (([], 1)) or state == (([1], 2)):
        return 1
    elif state == state == (([], 2)) or state == (([1], 1)):
        return -1
    else:
        return "This has failed"
    
def max_value_ab(state, alpha, beta):
    if terminal_test(state) is True:
        return utility(state)
    else:
        v = -1
        for s in successors(state):
            v = max(v, min_value_ab(s, alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v
    
def min_value_ab(state, alpha, beta):
    if terminal_test(state) is True:
        return utility(state)
    else:
        v = 1
        for s in successors(state):
            v = min(v, max_value_ab(s, alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v
    
def minimax_value_ab(state):
    if state[-1] == 1:
        return max_value_ab(state, -100, 100)
    elif state [-1] == 2:
        return min_value_ab(state, -100, 100)
    else:
        return "This has failed!"
    
def test_ab(state):
    start = time.time()
    search_result = minimax_value_ab(state)
    end = time.time()
    print('Time taken:', end - start)
    return search_result