def isPalindrome(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False
 
s = str(input("Enter a string: "))
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")