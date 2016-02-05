"""
Get the number of test cases
"""
T = int(input().strip())

"""
Go through all the test cases
"""
for case in range(T):
    """
    Number of Black and White elements required
    """
    B, W = [int(x) for x in input().strip().split(" ")]

    """
    Price per piece
    """
    X, Y, Z = [int(x) for x in input().strip().split(" ")]
    
    min_value = min(B * X, B * (Y + Z)) + min(W * Y, W * (X + Z))
    print(str(min_value))
