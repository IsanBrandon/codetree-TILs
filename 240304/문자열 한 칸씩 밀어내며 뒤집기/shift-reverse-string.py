# 문자열과 q를 입력받습니다.
string, q_num = input().split()
# 문자열 내 값을 직접 변경하기 위해서는 리스트로 변환하여 해결합니다.
list_str = list(string)
q_num = int(q_num)

# 문자열의 길이를 구합니다.
str_size = len(list_str)

# q개의 질의를 수행합니다.
for i in range(q_num):
    # 요청을 입력받습니다.
    q_type = int(input())

    if q_type == 1:
        # step1: 가장 앞의 문자를 저장한 뒤,
        # step2: 문자열을 앞부터 순회하며 문자를 한 칸씩 앞으로 당기고
        # step3: 문자열의 제일 뒤에 가장 앞에 있던 문자를 넣어줍니다. 
        front = list_str[0]                   # step1
        for i in range(1, str_size):          # step2
            list_str[i - 1] = list_str[i]
        list_str[str_size - 1] = front        # step3

        # 리스트를 문자열로 변환하여 출력합니다. 
        print("".join(list_str))

    elif q_type == 2:
        # step1: 가장 뒤의 문자를 저장한 뒤,
        # step2: 문자열의 뒤부터 순회하며 문자를 한 칸씩 뒤로 밀어주고
        # step3: 문자열의 제일 앞에 가장 뒤에 있던 문자를 넣어줍니다. 
        back = list_str[str_size - 1];          # step1
        for i in range(str_size - 1, 0, -1):    # step2
            list_str[i] = list_str[i - 1]    
        list_str[0] = back					    # step3

        # 리스트를 문자열로 변환하여 출력합니다. 
        print("".join(list_str))

    else:
    # 문자열의 앞부터 순회하며 좌우 대칭 위치에 있는 문자와 swap해줍니다. 
        # 단, 문자열의 절반만 순회해줍니다.
        for i in range(str_size // 2):
            temp = list_str[i]
            list_str[i] = list_str[str_size - i - 1]
            list_str[str_size - i - 1] = temp
        
        # 리스트를 문자열로 변환하여 출력합니다. 
        print("".join(list_str))