def balanced_parentheses(str):
    counter = 0

    for char in range(len(str)):
        if str[char] == '(' or str[char] == '{' or str[char] == '[':
            counter += 1
        elif str[char] == ')' or str[char] == '}' or str[char] == ']':
            counter -= 1
        # exit function and return False if counter < 0, meaning unbalanced chars    
        # need to re-check on each iteration, so can't be an elif
        if counter < 0:
            return False

    # need to explicitly specify since 0 is a falsy value
    return True if counter == 0 else False


print(balanced_parentheses("()")) # True
print(balanced_parentheses("())")) # False
print(balanced_parentheses("(){}")) # True
print(balanced_parentheses("({})")) # True
print(balanced_parentheses("(){}[])")) # False
print(balanced_parentheses("][")) # False
print(balanced_parentheses("(({}")) # False
print(balanced_parentheses("}([]){")) # False
print(balanced_parentheses("{[()]({})}()")) # True