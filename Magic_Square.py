mat=[]
def main():
    print("Enter the odd order of a square matrix: ")
    n=int(input())
    for i in range(0,n):
        mat.append([])
    for i in range(0,n):
        for j in range(0,n):
            mat[i].append(j)
            mat[i][j]=0  #initialising all elements in a matrix to zero

    magic_const=(n*(n**2+1)//2)
    print("Magic Square constant is: ")
    print(magic_const)
    odd_magic_square_generator(n) # a constant(sum) by any row,column or diagonal

#Odd Magic Squares
def odd_magic_square_generator(n):
    i=n//2
    j=n-1
    mat[i][j]=1

    for a in range(2, n ** 2 + 1):
        i = i - 1
        j = j + 1
        if (i == -1 and j != n):
            i = n - 1
        elif (j == n and i != -1):
            j = 0
        elif (i == -1 and j == n):
            i = 0
            j = n - 2

        if mat[i][j] != 0:
            i = i + 1
            j = j - 2

        mat[i][j] = a

    print("The magic Square generated is: ")
    for i in range(n):
        for j in range(n):
            print(mat[i][j],end=" ")  #so that elements in inner loop are prited in same line
        print("\n")
        

main()

        




