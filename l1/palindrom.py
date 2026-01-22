def solution(a_string: str) -> bool:
    a_string = ''.join(i for i in a_string.lower() if i.isalnum())
    return a_string == ''.join(reversed(a_string))
print(solution(input()))