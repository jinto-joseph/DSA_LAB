def Is_Palindrome(name):
    stack = []
    for char in name.lower():
        stack.append(char)

    reversed_name = ""
    while stack :
        reversed_name+=stack.pop()
    
    return reversed_name==name.lower()

print("Enter the number of names :")
n = int(input())
palindrome_stack = []
for i in range(n):
    name = input("Enter the name :")
    if Is_Palindrome(name):
        palindrome_stack.append(name.lower())
    
print("Palindrome in LIFO :")
if not palindrome_stack:
    print("No Palindrome")
else :
    while palindrome_stack:
        print(palindrome_stack.pop())