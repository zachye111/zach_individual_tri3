def tree(x):
    print("\n".join([f"{'*'*(2* n + 1):^{2*x+1}}" for n in range(x)]))
def trunk(n):
    for i in range(n):
        for j in range(n-1):
            print('      ', end=' ')
        print('***')
tree(15)
trunk(3)
print("        Here is the Tree.")