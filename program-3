def generate_odd_series(a: int) -> str:

    if a < 1:
        return "Input must be a positive integer."
 
    n = (a + 1) // 2
 
    odd_numbers = [str(2 * i + 1) for i in range(n)]

    return ', '.join(odd_numbers)
 
if __name__ == "__main__":
    a = int(input("Enter a positive integer: "))
    result = generate_odd_series(a)
    print(result)
