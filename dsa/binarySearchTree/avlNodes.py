# Function to find minimum number of nodes

def AVLnodes(height):
     
    # Base Conditions
    if (height == 0):
        return 1
    elif (height == 1):
        return 2
 
    # Recursive function call
    # for the recurrence relation
    return (1 + AVLnodes(height - 1) +
                AVLnodes(height - 2))
 
# Driver Code
if __name__ == '__main__':
    H = 2
    print(AVLnodes(H))