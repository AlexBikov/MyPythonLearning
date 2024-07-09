#a =  3 ** 2021 + 5 * 3 ** 2000 + 3 ** 501 + 5 * 3 ** 500 + 1


"""def step(k):
    m = ""
    while k > 0:
       m += str(k % 9)
       k = k // 9
    return m[::-1]


print(step(a))"""

"""b = 3 ** 2021 + 5 * 3 ** 2000 + 3 ** 501 + 5 * 3 ** 500 + 1
def nine(f):
    Переводит из одной системы счисления в другую
    o = ''
    while f > 0:
        o += str(f % 9)
        f = f // 9
    return o[::-1]
for n in (nine(b)):
    o = nine(b)
    n = o.count('0')
    print(n)
    break"""

"""a = 5 ** 2019 - 5 ** 1019 + 25 ** 600 - 125
print(a)

def chis(s):
    O = ""
    while s > 0:
        O += str(s % 5)
        s = s // 5
    return O[::-1]
for cisla in (chis(a)):
    m = chis(a)
    cht = m.count('4')
    print(cht)
    break"""






"""def DEL(n, m):
    "Возвращает правду или ложь в выражении"
    return n % m == 0

for A in range(1, 100000):
    "Перебирает А в диапазоне"
    for x in range(0, 100000):
        "Перебирает х в диапазоне"
        if ((not(DEL(x, A))) <= ((DEL(x, 18)) <= (not(DEL(x, 81))))) == False:
            break
    else:
        print(A)"""





"""def DEL(n, m):
    return n % m == 0

for A in range(1, 1000):
    for x in range(0, 1000):
        if ((not(DEL(x, A)))<=(((DEL(x, 26))<=(not(DEL(x, 169)))))) == False:
            break
    else:
        print(A)

def DEL(x, A):
    "Возвращает Истинность или Лоожность значения выражения"
    return ((x % A) != 0)<=((x % 26 == 0)<=(x % 169 != 0))


for A in range(1, 10000):
    for x in range(0, 1000):
        if not(DEL(x, A)):
            break
    else:
        print(A)"""


"""def DEL(x, A):
    "Возвращает Истинность или Лоожность значения выражения"
    return ((x % A) != 0)<=((x % 26 == 0)<=(x % 169 != 0))
    "Здесь переписали выражение из задания заменив делы на логические выражение с равенством либо не навенством 0"
for A in range(1, 10000):
    fl = True
    "Это флаг переменная, которая показыввает ложна или правдива ли функция "
    for x in range(0, 1000):
        "в условии прописано, что если функция будет посчитана с результатом 0 и значение переменной будет равно Ложь, тоесть Х нам не подойдет,то программа перестанет считать"
        if not(DEL(x, A)):
            fl == False
            break
    if fl==True:
        print(A)"""






"""def trg(x, A, m):
    return x + A > m and x + m > A and A + m > x


for A in range(1, 1000):
    for x in range(1, 1000):
       if (not(((trg(x, 12, 20)) == (max(x, 5) <= 28)) and (trg(x, A, 3)))) == False:
           break
    else:
        print(A)"""


"""print("x,y,z,w,F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not((x <= y) <= w) and z) == 1:
                    print(x, y, z, w)"""


"""for n in range(100, 1000):
    K = str(n)
    F = K[0]
    S = K[1]
    T = K[2]
    D = int(F)**2 + int(S) ** 2
    V = int(S)**2 + int(T) ** 2


    if D < V:
        G = str(V)+str(D)
        print(G)
    elif D == V:
        G = str(D) + str(V)
        print(G)
    else:
        G = str(D)+str(V)
        print(G)

    R = int(G)
    if R == 9752:
        print(F,S,T)"""








"""for n in range(1,100):
    N = bin(n)[2:]
    S = len(N)
    if S % 2 == 0:
        S = N[:len(N)//2] + '1' + N[len(N)//2:]
        R = int(S, 2)
        if R >= 26:
            print(n)"""






"""for n in range (1,100):
    k = n % 4
    N = bin(n - k)[2:]
    K = N.count('1')
    N = str(N) + str(K % 2)
    K = N.count('1')
    N = str(N) + str(K % 2)

    R = int(N, 2)
    if R < 64:
        print(n)"""







"""Z = 4 ** 700 + 4 ** 100 - 16 ** 100 - 64

def step(x):
    m = ""
    while x > 0:
        m += str(x % 4)
        x = x // 4
    return m[::-1]

S = step(Z).count("3")


print(Z)
print(step(Z))
print(S)"""





"""def DEL(x, A):
    return x % A 


for A in range(1, 1000):
    for x in range(1, 1000):
        if ((not(DEL(x, A))) <= (DEL(x, 54) <= (not(DEL(162, x))))) == 0:
            break

    else:
        print(A)"""


"""def M(x):
    return (x % A != 0) <= ((x % 54 == 0) <= (162 % x != 0))

A = 1000
while True:
    if all(M(x) for x in range(1, 1000)):
        print(A)
        break
    A -= 1"""




"""def vst_sort(A):
    #Сортировка вставками
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            A[k], A[k-1] = A[k - 1], A[k]
            k -= 1
    return A


M = [2,4,6,7,3,1,5,8]
print(vst_sort(M))"""


"""def sort_v(L):
    ''' Сортировка вставками'''
    M = len(L)
    for high in range(0, 21):
        h = high
        while h > 0 and L[h - 1] > L[h]:
            L[h - 1], L[h] = L[h], L[h - 1]
            h -= 1
    return(L)"""

#s = [2,5,6,8,9,13,4,15,17,20,1,0,19,14,12,10,11,18,7,3,16]
#print(sort_v(s))


"""def test_sort(sort_algorithm) :
    print("Тестируем :", sort_algorithm.__doc__)
    print("testcase #1: ", end="")
    A = [2,5,6,8,9,13,4,15,17,20,1,0,19,14,12,10,11,18,7,3,16]
    A_sorted = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14,15,16,17,18,19,20]
    sort_algorithm(A)
    print("ok" if A == A_sorted else "Fail")

def test_sort(srt_alg):
    print("тест для:", srt_alg.__doc__)
    print("тест - кейс 1: ", end="")
    A = [2,5,6,8,9,13,4,15,17,20,1,0,19,14,12,10,11,18,7,3,16]
    A_sr = [0,1, 2, 3, 4, 5, 6, 20, 8, 9, 10, 11, 12, 13,14,15,16,17,18,19,7]
    srt_alg(A)
    print("OKEY" if A == A_sr else "FATAL")
    


if __name__ == "__main__":
    test_sort(sort_v)"""


"""def sort_vbr(A):
    N = len(A)
    for pos in range(N - 1):
        for k in range(pos + 1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]
    return(A)




K = [10,9,8,7,60,100,6,5,4,3,2,1,22,45,50]
print(sort_vbr(K))"""



"""def test_sort(sort_algorithm) :
    print("testcase #2 :", end="")
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print("ok" if A == A_sorted else "Fail")


if __name__ == "__main__":
    test_sort(sort_vbr)"""



def sort_bubble(A):
    N = len(A)
    for bypass in range(1,N - 1):
        for k in range(0, N - bypass):
            if A[k] > A[k + 1]:
                A[k], A[k+1] = A[k+1], A[k]

    return(A)

from math import *

K = [10,9,8,7,60,100,6,5,4,3,2,1,22,45,50]
print(K)
print(sort_bubble(K))
print(min(sort_bubble(K)))
print(max(sort_bubble(K)))
print(int(sqrt(max(sort_bubble(K)))))
