# 利用if判断一个年份是否为闰年
# 1.非整百年能被4整除的为闰年。（如2004年就是闰年,2100年不是闰年）
# 2.能被400整除的是闰年。(如2000年是闰年，1900年不是闰年)
# year = int(input('请输入一个年份：'))
# if year % 100 != 0 and year % 4 == 0:
#     print(year, '是闰年')
# elif year % 400 == 0:
#     print(year, '是闰年')
# else:
#     print(year, '不是闰年')

# 实现一周的记账功能
# 首先记录输入的7天的收入，然后记录输入的7天的支出。
# 然后打印出以下内容：
# 7天的收入(list)
# 7天的支出(list)
# 每天的结余(dict)
# 最终的结余
#
# # 定义两个列表
# income = list()
# out = list()
#
# # 记录7天收入
# print('请输入7天的收入：')
# i = 1
# while i <= 7:
#     print('第', i, '天收入：')
#     money_in = input()
#     income.append(money_in)
#     i += 1
#
# # 记录7天支出
# print('请输入7天的支出：')
# j = 1
# while j <= 7:
#     print('第', j, '天支出：')
#     money_out = input()
#     out.append(money_out)
#     j += 1
#
# # 输出收入与支出情况
# print('7天的收入：', income)
# print('7天的支出：', out)
#
# # 计算每天结余
# print('每天结余情况：')
# money = dict()
# i = 1
# while i <= 7:
#     s = int(out[i-1]) - int(income[i-1])
#     money[i] = s
#     print('第', i, '天:', s)
#     i += 1
#
# # 计算最终结余
# all_money = 0
# for i in [1, 2, 3, 4, 5, 6, 7]:
#     all_money += int(money[i])
# print('最终结余：', all_money)


# 实现ATM机功能
# 查询余额
# 存款
# 取款
# 退出

# switch = -1  # 能进入循环
# money = 0  # 初始为0元
# while switch != 4:
#     print('\n1.查询余额\n2.存款\n3.取款\n4.退出')
#     switch = int(input('请输入功能编号：'))
#     if switch == 1:
#         print('余额：', money)
#     elif switch == 2:
#         income = int(input('请输入存款金额：'))
#         money += income
#         print('存款成功！！！\n余额：', money)
#     elif switch == 3:
#         outcome = int(input('请输入取款金额：'))
#         if money >= outcome:
#             money -= outcome
#             print('取款成功！！！\n余额：', money)
#         else:
#             print('取款失败，余额不足！！！')
#     elif switch == 4:
#         break
#     else:
#         print('输入有误，请重新输入！！！')


#  词汇表生成及统计
# 将文本生成词汇表(单词list)，单词对应ID的dict，以及ID对应单词的dict。
# 将你的程序变成一个盒子，输入就是上面一段文本，盒子内部：首先将文本转换成单词列表，再得到统计的单词表(去重)，然后得到单词ID相互对应的字典。
# 效果如下：
# vocab = ['大家', '中国', '捍卫', ...}
# word2id = {'大家': 0, '中国': 1, '捍卫': 2, ...}
# id2word = {0: '大家', 1: '中国', 2: '捍卫', ...}

text = '2019 年 十月 一日 上午 ， 庆祝 中华人民共和国 成立 70 周年 阅兵式 在 首都北京 盛大举行 ， 59 个 阅兵 方阵 ， 580 台受 阅 装备 ， 1.5 万人 的 参阅 队伍 接受 了 全国 人民 ' \
       '的 检阅 。 阅兵 装备 方队 展示 的 武器装备 皆 为 国产 现役 主战 装备 ， 40% 为 首次 展示 。 其中 近些年来 广受 全球 关注 的 东风 41 洲际 弹道导弹 ， 巨浪 二潜射 弹道导弹 ， 东风 ' \
       '17 高超音速 武器 系统 终于 揭幕 亮剑 ， 以 " 不怒 自威 " 的 形象 向 世界 展示 中国 捍卫 和平 的 意志 与 力量 。 相较 于 其他 首度 公开 亮相 的 武器装备 ， 这 三款 武器 多年 来 ' \
       '传闻 不断 ， 备受 关注 ， 并 因 其 " 大国 基石 " 的 地位 而 被 公众 赋予 特殊 的 期待 ， 这 三款 武器装备 实力 究竟 如何 ， 又 各自 承担 着 怎样 的 历史 " 使命 " 呢 ？ 本报 ' \
       '特约 相关 领域 军事 专家 ， 为 大家 详细 解读 这 三款 彰显 国威 ， 震撼 世界 的 国 之 重器 。 '
# 每个单词后是空格，进行字符串切割
vocab = list()
for word in text.split(' '):
    vocab.append(word)
print(vocab)

# 列表转字典
# 创建一个有序数字列表
num = list()
for i in range(0, len(vocab)):
    num.append(i)
word2id = dict(zip(vocab, num))
id2word = dict(zip(num, vocab))
print(word2id)
print(id2word)