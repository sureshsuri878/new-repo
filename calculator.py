def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    # Simple test cases for Jenkins to verify
    test_val1 = 10
    test_val2 = 5
    
    result_add = add(test_val1, test_val2)
    print(f"Testing Addition: {test_val1} + {test_val2} = {result_add}")
    
    if result_add == 15:
        print("Success: Addition is correct!")
    else:
        print("Failure: Addition is wrong!")
        exit(1) # Exit with error code 1 so Jenkins marks build as 'Failed'
