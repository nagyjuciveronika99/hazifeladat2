def feladat_6(n,m):
    n_szamjegyek=[]
    m_szamjegyek=[]
    while n!=0:
        n_szamjegyek.append(n%10)
        n=n/10
    while m!=0:
        m_szamjegyek.append(m%10)
        m=m/10
    kozosdb=0
    for s in n_szamjegyek:
        for t in m_szamjegyek:
            if s==t:
                kozosdb=kozosdb+1
                if kozosdb==2:
                    print("A ket szam rokon.")
                    return
    print ("A ket szam nem rokon.")



def feladat_7(n,m):
    n_szamjegyek = []
    m_szamjegyek = []
    while n != 0:
        n_szamjegyek.append(n % 10)
        n = n / 10
    while m != 0:
        m_szamjegyek.append(m % 10)
        m = m / 10
    kozosdb = 0
    for s in n_szamjegyek:
        for t in m_szamjegyek:
            if s == t:
                kozosdb = kozosdb + 1
                if kozosdb == 1:
                    print("A ket szam barat.")
                    return
    print("A ket szam nem barat.")
def feladat_8(n):
    for szam in range(0,n):
        szamok=range(0,szam+1)
        osszeg=sum (szamok)
        if osszeg>=n :
            print (szam)
            return

def feladat_9(kivant_magassag):
    aktualis_magassag=1
    novekmeny=2
    while aktualis_magassag<=kivant_magassag:
        aktualis_magassag=aktualis_magassag+1/novekmeny
        novekmeny=novekmeny+1
    print(novekmeny-2)



def main():
    feladat_6(14,15)
    feladat_7(150,15)
    feladat_8(5)
    feladat_9(2)#300-ig nagyon sok idő.
if __name__ == '__main__':
   main()