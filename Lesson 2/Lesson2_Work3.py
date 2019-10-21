# 实现ATM机功能
# 查询余额
# 存款
# 取款
# 退出

switch = -1  # 能进入循环
money = 0  # 初始为0元
while switch != 4:
    print('\n1.查询余额\n2.存款\n3.取款\n4.退出')
    switch = int(input('请输入功能编号：'))
    if switch == 1:
        print('余额：', money)
    elif switch == 2:
        income = int(input('请输入存款金额：'))
        money += income
        print('存款成功！！！\n余额：', money)
    elif switch == 3:
        outcome = int(input('请输入取款金额：'))
        if money >= outcome:
            money -= outcome
            print('取款成功！！！\n余额：', money)
        else:
            print('取款失败，余额不足！！！')
    elif switch == 4:
        break
    else:
        print('输入有误，请重新输入！！！')

