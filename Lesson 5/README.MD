# 完成以下问答和编程练习

**理论部分**
1. 验证多重继承的属性规则，请选择
- 就近原则
- 随机原则
- 类定义的先后原则


```python
class A0:
    name = 'A0'
    
class A2(A0):
    num = 2
    
class A1:
    num = 1
    
class A3:
    name = 'A3'
    
class A4(A1,A2,A3):
    pass
 
ins = A4()
print(ins.name) # 就近原则：A4先继承A2，A2又继承A0，所以name=A0
print(ins.num) # 就近原则：A4先继承A1的num
```

    A0
    1
    

**编程实践部分**

1. 完成ATM的类实现  
将第二次课程的ATM机器改写成类实现


```python
class ATM:
    money = 0

    def menu(self):
        while True:
            print("""
===========
功能选项：
1. 查询余额
2. 存款
3. 取款
4. 退出
===========
            """)
            # noinspection PyBroadException
            try:
                choice = int(input('请选择操作对应的数字：'))
                if choice == 1:
                    self.show_money()
                elif choice == 2:
                    self.add_money()
                elif choice == 3:
                    self.out_money()
                elif choice == 4:
                    print('感谢使用本系统！')
                    break
                else:
                    print('输入有误，请重新输入！')
            except Exception:
                print('输入有误，请重新输入！')

    def show_money(self):
        print('你的余额为：', self.money)

    def add_money(self):
        a_money = int(input('你输入存款数额：'))
        self.money = self.money + a_money

    def out_money(self):
        o_money = int(input('请输入取款数额:'))
        if o_money > self.money:
            print('余额不足，提取失败')
        else:
            self.money = self.money - o_money
            print('取款成功！')


bm = ATM()
bm.menu()

```
   

2. 练习会先提供一个李靖类，用以记录人物角色的战斗力。需要你创建一个子类哪吒类，提供属性和参数的修改。  
要求： 在哪吒的初始化方法中，默认添加`['混天绫', '乾坤圈']` 两个装备,以及初始化战斗力为50.


```python
# 代码不用修改，读懂后运行即可。
class Lijing: # 李靖
    # 初始化函数，为每个实例创建4个参数（其中后3个参数有默认值）
    def __init__(self, name, weapons=[], power=10): 
        self.name = name
        self.weapons = weapons
        self.power = power

    def count_fight(self, weapon, weapon_power):
        self.weapons.append(weapon)
        self.power += weapon_power  # 总战力=武器战力之和

lijing = Lijing('李靖')
print(lijing.weapons)
lijing.count_fight('七宝玲珑塔', 50)  # 七宝玲珑塔 战力 50
print(lijing.power)
```

    []
    60
    


```python
class Lijing: # 李靖
    # 初始化函数，为每个实例创建4个参数（其中后3个参数有默认值）
    def __init__(self, name, weapons=[], power=10): 
        self.name = name
        self.weapons = weapons
        self.power = power

    def count_fight(self, weapon, weapon_power):
        self.weapons.append(weapon)
        self.power += weapon_power  # 总战力=武器战力之和
        
# your code here        
# 请你完成子类的定制（包括初始化方法和count_fight函数）
class Nezha(Lijing): # 哪吒
    def __init__(self, name, weapons=['混天绫', '乾坤圈'], power=50):
        self.weapons = weapons
        self.power = power
#     def count_fight(self):    直接用父类方法，不用改写。

    
# 通过两个实例，完成子类和父类的对比（可自行验证）
lijing = Lijing('李靖')
nezha = Nezha('哪吒')
print(lijing.weapons)
print(nezha.weapons)
lijing.count_fight('七宝玲珑塔', 50)  # 七宝玲珑塔 战力 50
print(lijing.weapons)
print(lijing.power)
nezha.count_fight('火尖枪', 40)  #
print(nezha.weapons)
print(nezha.power)
```

    []
    ['混天绫', '乾坤圈']
    ['七宝玲珑塔']
    60
    ['混天绫', '乾坤圈', '火尖枪']
    90
    


```python

```
