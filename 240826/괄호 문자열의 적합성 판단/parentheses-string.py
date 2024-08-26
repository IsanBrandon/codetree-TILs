# function solution(str)
#   set s = empty stack
#   for i = 0 ... i < str.size  // 주어진 문자열을 순회합니다.
#     if str[i] == '('          // 열린 괄호에 대해서는
#       s.push('(')             // stack에 열린 괄호를 넣어줍니다.
#     else
#       if s.empty() == true    // 닫힌괄호가 나온 상황에서, stack이 비어있다면,
#         return false          // 올바른 괄호 문자열이 아닙니다.
#       s.pop()                 // 가장 위에 있는 값을 비워줍니다.

#   if s.empty() == false       // 전부 순회했는데도 불구하고 stack이 비어있지 않다면
#     return false              // 올바른 괄호 문자열이 아닙니다.
#   return true                 // 전부 통과했다면 올바른 괄호 문자열 입니다.

import sys

class Stack:
    def __init__(self):         # 빈 스택 하나를 생성합니다.
        self.items = []

    def push(self, item):       # 스택에 데이터를 추가합니다.
        self.items.append(item)

    def empty(self):            # 스택이 비어있으면 True를 반환합니다.
        return not self.items

    def size(self):             # 스택에 있는 데이터 수를 반환합니다.
        return len(self.items)

    def pop(self):              # 스택의 가장 위에 있는 데이터를 반환하고 제거합니다. 
        if self.empty():
            raise Exception("Stack is empty")

        return self.items.pop()

    def top(self):              # 스택의 가장 위에 있는 데이터를 제거하지 않고 반환합니다.
        if self.empty():
            raise Exception("Stack is empty")

        return self.items[-1]


# 변수 선언 및 입력:
string = input()
s = Stack()

for char in string:
    if char == '(':
        s.push('(')
    else:
        if s.empty():
            print("No")
            sys.exit(0)

        s.pop()

if s.empty():
    print("Yes")
else:
    print("No")