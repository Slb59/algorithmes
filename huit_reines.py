def reine(n):
    def _reine(s,n,solutions): 
        if len(s)==n: solutions.append(s)
        else:
            for i1 in set(range(1,n+1))-set(s): 
                liste=[len(s)-j!=abs(i1-i) for j,i in enumerate(s)]
                if not(False in liste): _reine(s+[i1],n,solutions)
    solutions=[]
    _reine([],n,solutions)
    return solutions,('Nombre de solutions : %d' % len(solutions))

if __name__ == '__main__':
    print(reine(8))

