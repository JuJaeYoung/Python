# 정해진 금액
maxi = int(input())

# 메뉴판
menu = {'로스카츠' : 7000, '카레카츠' : 9000, '카츠동' : 7000, '사케동' : 10000, '텐동' : 10000}
menu_name = ['']
menu_price = [0]

# 메뉴와 가격 분리
for k, v in menu.items() :                              
    menu_name.append(k)
    menu_price.append(v)

# 부분집합
menu_lst = []
for a in menu_name[0:2:1] :                             
    for b in menu_name[0:3:2] :
        for c in menu_name[0:4:3] :
            for d in menu_name[0:5:4] :
                for e in menu_name[0:6:5] :
                    menu_lst.append("".join(a + ' ' + b + ' '+ c + ' ' + d + ' ' + e))

# 조합 별 가격
price_lst = []
for x in menu_lst :
    price = 0
    if '로스카츠' in x :
        price += menu_price[1]
    if '카레카츠' in x :
        price += menu_price[2]
    if '카츠동' in x :
        price += menu_price[3]
    if '사케동' in x :
        price += menu_price[4]
    if '텐동' in x :
        price += menu_price[5]
    price_lst.append(price)

# 공백 제거
for i in range(len(menu_lst)) :
    menu_lst[i] = menu_lst[i].strip()      
    menu_lst[i] = menu_lst[i].split()

# 주문 가능한 메뉴 선정
possible_menu = {}
for i in range(1,len(menu_lst)) :
    if price_lst[i] <= maxi :
        p_menu = ''
        for j in range(len(menu_lst[i])) :
            if j != len(menu_lst[i]) - 1 :
                p_menu += menu_lst[i][j] + ', '
            else :
                p_menu += menu_lst[i][j]
        possible_menu[p_menu] = price_lst[i]


# 출력
# 1 메뉴판
print('┌─☆★☆★☆★☆★☆★☆─┐')
print(f'    메뉴   >    가격    ')
print('├─────────────┤')
for i in range(1,6) :
    print(f"{'%6s'%menu_name[i]}"," " * (5 -len(menu_name[i])), f"{'%7d'%menu_price[i]}  ")
print('└─────────────┘')

#2 결과
print(f'\n주문 가능 금액 : {maxi}원\n')
print('↓ 가능한 주문 리스트 ↓')
for k, v in possible_menu.items() :
    print(f'<{k}> 주문하시면 {v}원 입니다.')
print('\n'+'어떤 메뉴를 주문하시겠습니까?')












