def is_palindrome(string: str) -> bool:
    left = 0
    right = len(string) - 1

    palindrome = True

    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            palindrome = False
            break

    return palindrome
