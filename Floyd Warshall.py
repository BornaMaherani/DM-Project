# By Borna Maherani
# 401243079

def inf(m):
    n = len(m)
    infinite = 0
    for i in range(0, n):
        for j in range(0, n):
            infinite += m[i][j]
    infinite = infinite * infinite
    return infinite


def initFW(m):    
    n = len(m)
    infinite = inf(m)
    for i in range(0, n):
        for j in range(0, n):
            if(i != j and m[i][j] == 0):
                m[i][j] = infinite
            elif(i == j):
                m[i][j] = 0
    return m

def unInfinite(m, inf):
    n = len(m)
    for i in range(n):
        for j in range(n):
            if(m[i][j] >= inf):
                m[i][j] = 0
    return m


def initSh(m): 
    n = len(m)
    infinite = inf(m)
    for i in range(0, n):
        for j in range(0, n):
            if(m[i][j] == 0):
                m[i][j] = infinite
    return m

#1
def floWar(w):
    n = len(w)
    infinite = inf(w)
    initFW(w)
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                w[i][j] = min(w[i][j], (w[i][k] + w[k][j]))
    infinite = inf(w)
    for i in range(0, n):
        for j in range(0, n):
            if(w[i][j] >= infinite):
                w[i][j] = 0
    return unInfinite(w, infinite)


def clone(l):
    n = len(l)
    c = []
    for i in range(0, n):
        t = []
        for j in range(0, n):
            t.append(l[i][j])
        c.append(t)
    return c

#2
def shPathP(w, p):
    infinite = inf(w)
    initSh(w)
    n = len(w)
    infM = []
    M = []
    for i in range(0, n):
        t = []
        for j in range(0, n):
            t.append(infinite)
        infM.append(t)
    p1 = clone(w)
    M.append(p1)
    for k in range(0, p-1):
        p1 = clone(infM)
        for l in range(0,k+1):
            for i in range(0, n):
                for j in range(0, n):
                    for q in range(0, n):
                        if (p1[i][j] > (M[l][i][q] + M[k-l][q][j])):
                            p1[i][j] = M[l][i][q] + M[k-l][q][j]
        M.append(p1)
    return unInfinite(M[p-1] , infinite)

#3
def mulP_ShPath(w , p):
    w = shPathP(w , p)
    w = floWar(w)
    return w


#4
def rec_shPathP(w1,w2,p):
    n = len(w2)
    infinite = inf(w1)
    initSh(w1)
    initSh(w2)
    if (p==1): 
        return (unInfinite(w2,infinite))
    else:
        temp = []
        for i in range(0, n):
            q = []
            for j in range(0, n):
                q.append(-1)
            temp.append(q)
        
        for i in range(0, n):
            for j in range(0, n):
                shPath = infinite
                for k in range(0, n):
                    if ((w1[i][k] + w2[k][j]) < shPath):
                        shPath = w1[i][k] + w2[k][j]
                    if ((w2[i][k] + w1[k][j]) < shPath):
                        shPath = w2[i][k] + w1[k][j]
                temp[i][j] = shPath
        return rec_shPathP(unInfinite(w1, infinite), unInfinite(temp, infinite) , p-1)



graph = [[1, 2, 0, 3], [2, 0, 2, 5], [1, 1, 0, 0], [0, 0, 4, 0]]
graph2=clone(graph)