import timeit
setup1="zaczynamy kopcowe sortowanie"
kod1 = '''
def kopiec(ciag,n,i):
    najwieksza=i
    l=2*i+1
    r=2*i+2

    if l < n and ciag[i]<ciag[l]:
        najwieksza=l
    if r<n and ciag[najwieksza]<ciag[r]:
        najwieksza=r
    if najwieksza!=i:
        ciag[i],ciag[najwieksza]=ciag[najwieksza],ciag[i] #zamiana
        kopiec(ciag,n,najwieksza)
def sortowanieKopca(ciag):
    n=len(ciag)
    for i in range(n//2-1,-1,-1):
        kopiec(ciag,n,i)
    for i in range(n-1,0,-1):
        ciag[i], ciag[0]=ciag[0],ciag[i] #zamiana
        kopiec(ciag,i,0)

ciag=[4,10,11,5,73,5,1]
sortowanieKopca(ciag)
n=len(ciag)
print("posortowany ciag to")
for i in range(n):
    print("%d" %ciag[i])
'''
czas1=timeit.timeit(setup=setup1, stmt=kod1, number=1)

setup2="rozpoczynamy sortowanie szybkie"
kod2='''
def podzial(ciag,mala,duza):
    i=(mala-1)
    cel=ciag[duza]
    for j in range(mala, duza):
        if ciag[j]<cel:
            i=i+1
            ciag[i],ciag[j]=ciag[j],ciag[i]
    ciag[i+1],ciag[duza]=ciag[duza],ciag[i+1]
    return (i+1)

def sortowanieSzybkie(ciag,mala,duza):
    if mala<duza:
        indexPodzialu=podzial(ciag,mala,duza)
        sortowanieSzybkie(ciag,mala,indexPodzialu-1)
        sortowanieSzybkie(ciag,indexPodzialu+1,duza)

ciag=[4,10,11,5,73,5,1]
sortowanieSzybkie(ciag,0,n-1)
n=len(ciag)
print("posortowany ciag to")
for i in range(n):
    print("%d" %ciag[i])
'''
czas2=timeit.timeit(setup=setup2, stmt=kod2, number=1)
print(czas1)
print(czas2)
#nie umiem ogarnac tego timeit :((((