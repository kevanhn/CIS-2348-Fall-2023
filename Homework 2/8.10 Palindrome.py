def is_palindrome(input_str):
    input_str = input_str.replace(" ", "").lower()
    return input_str == input_str[::-1]

def main():
    input_str = input("")
    if is_palindrome(input_str):
        print(f"{input_str} is a palindrome")
    else:
        print(f"{input_str} is not a palindrome")

if __name__ == "__main__":
    main()