def feladat_1(n):
    lst=[]
    for i in range(2,n):
        if n%i==0:
            lst.append(i)
    if len(lst)==2:
        return True
    else:
        return False
def feladat_2(n):
    a=1
    lst=[]
    prmlst=[]
    for i in range(n):
        lst=[]
        while len(lst) !=1:
            lst=[]
            a=a+1
            for j in range(1,a):
                if a%j==0:
                    lst.append(j)
        prmlst.append(a)
    return prmlst[len(prmlst)-1]
def feladat_3(n):
    a=1
    while n>a:
        a=a*2
    return a



def main():
    print (feladat_1(8))
    print(feladat_2(8))
    print(feladat_3(513))
    if __name__ == '__main__':
        main()
