import random
while True:
    start = eval(input('游戏即将开始，请输入你的选择1为开始游戏，2为退出游戏'))
    if start == 1:
        print('游戏开始，数字以生成，你有十次机会')
        num = random.randint(0, 9)
        jishu = 0
        while True:
            user = eval(input("请输入你猜的数字："))
            if user == num:
                print('猜对了数字是%d' % num)
                break
            elif user < num:
                print('数字比你猜的大')
                jishu += 1
            elif user > num:
                print("数字比你猜的小")
                jishu += 1
            if jishu == 9:
                print('你输了，真笨')
                break
    elif start == 2:
        print('再见')
        break
    elif start != 1 and start != 2:
        print('请输入正确的选项')