def findMin(V):

    change = [1, 4, 7, 9]
    n = len(change)

    # Initialize Result 
    ans = []

    # Traverse through all denomination 
    i = n - 1

    while (i >= 0):

        # Find denominations 
        while (V >= change[i]):
            V -= change[i]
            ans.append(change[i])

        i -= 1

    # Print result 
    for i in range(len(ans)):
        print(ans[i], end=" ")

    print("\n", "Jumlah pecahan ada: ", len(ans))

if __name__ == '__main__':
    n = 29
    print("koin yang digunakan untuk memecah", n, "adalah: ", end = "")
    findMin(n)