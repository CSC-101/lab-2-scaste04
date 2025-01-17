def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b                  # This statement will be evaluated when both a > b and a > c are true
    elif b > c:
        return b + c                # This statement will be evaluated when the previous if condition was false and when b > c is true
    else:
        return 2 * c            # This statement will be evaluated when both the if condition and elif were false

answer1 = function2(3, 2, 1)
answer2 = function2(2, 3, 1)
answer3 = function2(2, 1, 3)
print()