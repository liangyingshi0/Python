# 实现一周的记账功能
# 首先记录输入的7天的收入，然后记录输入的7天的支出。
# 然后打印出以下内容：
# 7天的收入(list)
# 7天的支出(list)
# 每天的结余(dict)
# 最终的结余

# 定义两个列表
income = list()
out = list()

# 记录7天收入
print('请输入7天的收入：')
i = 1
while i <= 7:
    print('第', i, '天收入：')
    money_in = input()
    income.append(money_in)
    i += 1

# 记录7天支出
print('\n请输入7天的支出：')
j = 1
while j <= 7:
    print('第', j, '天支出：')
    money_out = input()
    out.append(money_out)
    j += 1

# 输出收入与支出情况
print('7天的收入：', income)
print('7天的支出：', out)

# 计算每天结余
print('每天结余情况：')
money = dict()
i = 1
while i <= 7:
    s = int(out[i-1]) - int(income[i-1])
    money[i] = s
    print('第', i, '天:', s)
    i += 1

# 计算最终结余
all_money = 0
for i in [1, 2, 3, 4, 5, 6, 7]:
    all_money += int(money[i])
print('最终结余：', all_money)

