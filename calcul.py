def premierSup(m):

    ListePremiers = [2]
    n= 3

    while ListePremiers[-1] < m:

        nEstPremier = True
        for x in ListePremiers:
            if n%x == 0:
                nEstPremier = False
                break
        if nEstPremier:
            ListePremiers.append(n)
        n+=1
    return ListePremiers[-1]
        
