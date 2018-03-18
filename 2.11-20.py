def feladat_11():
  try:
      fajl=open("be11.txt","r")

      legrovidebb=-1
      for line in fajl:
          utolso=line[-2:-1]
          if utolso=="!" or utolso=="?" or utolso==".":
              if legrovidebb==-1 or len(line)<legrovidebb: legrovidebb=len(line)




      fajl.close()
      print(legrovidebb+1)
  except Exception as e:
      print(e)
def feladat_12():
    try:
        fajl = open("be12.txt", "r")
        sorokszama=sum(1 for line in fajl)
        if sorokszama<1 or sorokszama>15:
            return

        szamok={}
        utolso=0
        fajl.seek(0)
        for line in fajl:
            line.rstrip()
            szamok[line.rstrip()]=0
        fajl.seek(0)
        for line in fajl:
            line.rstrip()
            szamok[line.rstrip()]=szamok[line.rstrip()]+1
            utolso=int(line.rstrip())
        kimenet=open("ki12.txt","w")

        for szam,db in szamok.items():
            if db==utolso and db>0:

                kimenet.write("Tartalmaz.")


        fajl.close()
        kimenet.close()



    except Exception as e:
        print(e)
def feladat_13():
    try:
    fajl=open("be13.txt","r")
    szamok=[]
    utolso=0
    for line in fajl:
        szam=int(line.rstrip())
        szamok.append(szam)
        utolso=szam
    db=0
    for i in range(1,szamok.__len__()):
        szam=szamok[i]
        for j in range(i,szamok.__len__()):

            if szam-szamok[j]<=utolso:
                db=db+1
    print (db)
    except Exception as e:
        print (e)


def feladat_15():
    try:
    fajl=open("be15.txt","r")
    sorok=[]
    for line in fajl:
        sor=line.rstrip()
        sor=sor[::-1].rstrip()
        sor=sor[::-1]

        sorok.append(sor)

    kimenet=open("ki15.txt","w")
    for sor in sorok:
        kimenet.write(sor + "\n")


    fajl.close()
    kimenet.close()
    except Exception as e:
        print (e)
def feladat_16():
    try:
    fajl=open("be16.txt","r")
    kimenet=open("ki16.txt","w")
    for line in fajl:
        sor=line.rstrip()
        szavak=sor.split(" ")
        kiirni=True
        for szo in szavak:
            if szo[0]==szo[0].lower():
                kiirni=False
        if kiirni:
            kimenet.write(sor+"\n")
    fajl.close()
    kimenet.close()
    except Exception as e:
        print (e)
def feladat_17():
    try:
    fajl = open("be17.txt", "r")
    kimenet = open("ki17.txt", "w")
    for line in fajl:
        sor = line.rstrip()
        szavak = sor.split(" ")
        kiirni = False
        for szo in szavak:
            if szo == szo.lower():
                kiirni = True
        if kiirni:
            kimenet.write(sor + "\n")
    fajl.close()
    kimenet.close()
    except Exception as e:
        print (e)

def feladat_18():
    try:
    fajl=open("be18.txt","r")
    nyeresegek={}
    for line in fajl:
        szavak=line.rstrip().split(" ")
        nyeresegek[szavak[0]]=0
        nyeresegek[szavak[2]] = 0
    fajl.seek(0)
    for line in fajl:
        szavak=line.rstrip().split(" ")
        nyeresegek[szavak[0]]=nyeresegek[szavak[0]]+1
        nyeresegek[szavak[2]] =nyeresegek[szavak[2]]+1

    print(max(nyeresegek,key=nyeresegek.get))
    except Exception as e:
        print (e)
def feladat_19():
    try:
    fajl = open("be19.txt", "r")
    latogatottsag = {}
    for line in fajl:
        szavak = line.rstrip().split(" ")
        latogatottsag[szavak[0]] = int(szavak[1])
    print(max(latogatottsag,key=latogatottsag.get))
    except Exception as e:
        print (e)
def feladat_20():
    try:
    fajl = open("be20.txt", "r")
    lakossag = {}
    for line in fajl:
        szavak = line.rstrip().split(";")
        lakossag[szavak[0]] = int(szavak[2])
    print(max(lakossag, key=lakossag.get))
    except Exception as e:
        print (e)
def main():
     feladat_11()
     feladat_12()
     feladat_13()
     feladat_15()
     feladat_16()
     feladat_17()
     feladat_18()
     feladat_19()
     feladat_20()

if __name__ == '__main__':
        main()