def udelejmilistik(radky,sloupce,znak):
    listik=[]
    for i in range(0,radky,1):
        radek=[]
        for j in range(0,sloupce,1):
            radek.append(znak)
            print(" {} ".format(znak),end="")
        listik.append(radek)
        print()
    return listik
if __name__=="__main__":
    prom=udelejmilistik(5,5,"*")