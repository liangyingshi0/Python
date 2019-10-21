# 利用if判断一个年份是否为闰年
# 1.非整百年能被4整除的为闰年。（如2004年就是闰年,2100年不是闰年）
# 2.能被400整除的是闰年。(如2000年是闰年，1900年不是闰年)

year = int(input('请输入一个年份：'))
if year % 100 != 0 and year % 4 == 0:
    print(year, '是闰年')
elif year % 400 == 0:
    print(year, '是闰年')
else:
    print(year, '不是闰年')
