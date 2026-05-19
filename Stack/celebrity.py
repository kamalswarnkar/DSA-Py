"""
A celebrity is a person who is known to all 
but does not know anyone at a party. A party 
is being organized by some people. A square 
matrix mat[][] of size n*n is used to represent 
people at the party such that if an element of 
row i and column j is set to 1 it means ith 
person knows jth person. You need to return the 
index of the celebrity in the party, if the 
celebrity does not exist, return -1.
"""

def naive_method(mat): # O(n^2)
    if len(mat) == 1:
            return 0
        
    r = len(mat)
    c = r #square matrix
        
    celeb = [0] * r
        
    for i in range(r):
        for j in range(c):
            if i != j:
                if mat[i][j] == 1:
                    celeb[i] += 1
                    break
                elif mat[j][i] == 0:
                    celeb[i] += 1
                    break
        
    for i in range(r):
        if celeb[i] == 0:
            return i
        
    return -1

def efficient_method(mat): # O(n)
    if len(mat) == 1:
        return 0
        
    r = len(mat)
    c = r
        
    stack = []
    for i in range(r):
        stack.append(i)
        
    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()
            
        if mat[a][b] == 1:
            stack.append(b)
        else:
            stack.append(a)
            
    cand = stack.pop()

    # to verify candi    
    for i in range(r):
        if i != cand:
            if mat[cand][i] == 1:
                return -1
            if mat[i][cand] == 0:
                return -1
        
    return cand