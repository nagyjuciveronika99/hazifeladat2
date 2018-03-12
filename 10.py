def feladat_10(fajl_nev):
    fajl=open(fajl_nev,mode="r")
    max=0
    for sor in fajl:
        if(sor.[0].isupper()and len(sor)>max):
    print(max)
    fajl.close()
def main():
    feladat_10()
if __name__ == '__main__':
    main()
