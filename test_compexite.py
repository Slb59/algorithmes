def f(n):
    compteur = 0
    i = 1
    while i<n:
        j = i+1
        while j<=n:
            compteur += 1
            j +=1
        i *=2
    return compteur

def main():
    print(f(4))

if __name__ == "__main__":
    main()