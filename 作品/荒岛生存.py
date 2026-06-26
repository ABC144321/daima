import time
import random
import sys


def survival_game():

    water = 100
    health = 100
    print('==================================')
    print('      欢迎来到海岛生存小游戏！')
    print('==================================')
    time.sleep(1)
    print('游戏开始...')
    time.sleep(1)
    print('你在一次航行中遇到了海啸，船只沉没，你被困在了一个无人海岛上。')
    print('整个船只有你一个人活了下来。')
    print('你带走了：燧石、鱼竿、钓饵、斧头、一小卷绳子、一把小刀。')
    print('你现在又累又渴，必须尽快想办法活下去。')
    time.sleep(2)
    while True:
        choice = input('你非常渴，你要：一、直接喝海水  二、制作简易淡化器（1小时产出25-50ml）：')
        if (choice == '一'):
            print('\n你忍不住喝了海水，咸苦的液体让你肠胃剧痛！')
            print('越喝越渴，体内电解质紊乱...')
            health -= 60
            print(f'【健康：{health}】你陷入昏迷，再也没有醒来...')
            print('游戏失败！')
            sys.exit()
        elif (choice == '二'):
            print('\n你用树枝、塑料布、容器制作了简易海水淡化器。')
            print('经过漫长的等待，你终于喝到了安全的淡水！')
            water = 100
            print(f'【水分：{water}】你恢复了一些体力。')
            break
        else:
            print('输入错误！请输入“一”或“二”！')
    time.sleep(2)
    print('\n淡水问题暂时解决，但你开始感到饥饿。')
    print('天色慢慢变暗，你必须尽快找到食物。')
    time.sleep(1)
    while True:
        choice = input('你选择：一、去海边钓鱼  二、进丛林找野果  三、用斧头砍树找虫子：')
        if (choice == '一'):
            print('你来到海边，架好鱼竿开始钓鱼...')
            time.sleep(2)
            luck = random.randint(1, 3)
            if (luck <= 2):
                print('你钓到了一条小鱼！用火烤熟后填饱了肚子。')
                health += 10
            else:
                print('运气不好，一条鱼都没上钩，你白白浪费了体力。')
                health -= 10
            break
        elif (choice == '二'):
            print('你进入丛林，阴暗潮湿，到处是藤蔓...')
            time.sleep(2)
            luck = random.randint(1, 4)
            if (luck == 1):
                print('你遇到了毒蛇！被咬了一口！')
                health -= 80
                print(f'【健康：{health}】你中毒身亡...')
                print('游戏失败！')
                sys.exit()
            else:
                print('你找到了一些无毒的野果，虽然酸涩，但可以充饥。')
                water -= 15
            break
        elif (choice == '三'):
            print('你用斧头劈开枯木，找到了高蛋白的虫子！')
            print('虽然恶心，但为了生存只能吃下去...')
            health += 5
            water -= 10
            break
        else:
            print('输入错误！请输入正确选项！')
    print(f'\n当前状态：健康={health}  水分={water}')
    time.sleep(2)
    print('\n夜幕降临，海岛变得寒冷、黑暗、危险。')
    print('你必须做出选择，否则可能被野兽袭击！')
    time.sleep(1)
    while True:
        choice = input('你选择：一、用燧石生火  二、躲进树洞  三、在沙滩过夜：')
        if (choice == '一'):
            print('你用燧石成功点燃了火堆！')
            print('火焰驱散了寒冷和野兽，你安全度过一夜。')
            health += 15
            break
        elif (choice == '二'):
            print('你找到一个大树洞躲了进去。')
            print('虽然安全，但又冷又闷，睡得很不好。')
            health -= 10
            break
        elif (choice == '三'):
            print('你在沙滩上睡去，深夜气温骤降，海风刺骨...')
            health -= 30
            print('你被冻醒，身体瑟瑟发抖。')
            break
        else:
            print('输入错误！')
    time.sleep(2)
    print('\n第二天清晨，你站在海边眺望远方。')
    print('你看到远处海平面上似乎有一个模糊的影子...')
    time.sleep(2)
    choice = input('\n你要：\n一、点燃大火堆发出浓烟求救  二、制作木筏尝试出海：')
    if (choice == '一'):
        print('\n你收集大量干柴，点燃巨大的火堆，滚滚浓烟直冲天空！')
        time.sleep(3)
        print('远处的船只看到了烟雾，朝你驶来！')
        time.sleep(2)
        print('你成功获救！游戏胜利！')
    elif (choice == '二'):
        print('\n你花费半天时间砍树、捆绑，制作了简易木筏。')
        time.sleep(2)
        luck = random.randint(1, 2)
        if (luck == 1):
            print('你在海上漂流了几小时，被渔船发现！')
            print('你成功获救！游戏胜利!')
        else:
            print('木筏不够坚固，被海浪打翻...')
            print('你体力不支，沉入海中...')
            print('游戏失败！')
    else:
        print('你错过了最佳求救时机，最终困死在海岛...')
        print('游戏失败！')

if (__name__ == '__main__'):
    survival_game()
