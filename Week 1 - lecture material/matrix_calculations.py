def multiply_manually(A,B):
    result_py = []
    for i in range(d):
        result_py.append([])
        for j in range(d):
            temp = 0
            for t in range(d):
                temp+= A[i,t]*B[t,j]
            result_py[-1].append(temp)
            
    return np.array(result_py)