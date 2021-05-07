import time, os
import auto_player as player


class YysRound():

    def __init__(
        self,
        list_start=[],
        list_running=['running'],
        list_end_1=['end_1', 'end_2'],
        list_end_2=['end_3'],
        list_end_3=['end_4', 'end_5'],
        list_end_fail=['fail_1', 'fail_2']
        ):
        self.list_start = list_start
        self.list_running = list_running
        self.list_end_1 = list_end_1
        self.list_end_2 = list_end_2
        self.list_end_3 = list_end_3
        self.list_end_fail = list_end_fail
    
    def round_start(self):
        while True:
            re_start = player.find_touch_any(self.list_start, True)
            re_running = player.find_touch_any(self.list_running, False)
            if re_start == None and re_running == 'running':
                break

    def round_end(self):
        while True:
            re_end_1 = player.find_touch_any(self.list_end_1, True)
            re_end_2 = player.find_touch_any(self.list_end_2, True)
            if re_end_2:
                time.sleep(0.7)
            re_end_3 = player.find_touch_any(self.list_end_3, True)
            if re_end_3:
                time.sleep(0.2)
                break
            re_fail = player.find_touch_any(self.list_end_fail, True)
            if re_fail:
                time.sleep(0.2)
                break


class TuPoRound(YysRound):

    def __init__(
        self,
        list_tupo = ['tupo_1', 'tupo_2', 'tupo_3', 'tupo_4', 'tupo_5', 'tupo_6'],
        list_jingong = ['jingong']
        ):
        super().__init__()
        self.list_tupo = list_tupo
        self.list_jingong = list_jingong

    def round_start(self):
        while True:
            re_tupo = player.find_touch_any(self.list_tupo, True, False)
            time.sleep(0.5)
            re_jingong = player.find_touch_any(self.list_jingong, True)
            time.sleep(5)
            re_running = player.find_touch_any(self.list_running, False)
            if re_running == 'running':
                break


class YuHun(YysRound):

    def __init__(
        self, 
        single_flag=False,
        list_start_single = ['start_1', 'huntu_1', 'huntu_2', 'yeyuanhuo'],
        list_start_team = ['huntuzudui'],
        list_invite = ['autoinvite'],
        list_yes = ['yes'],
        list_tick_1 = ['tick_1'],
        list_tick_2 = ['tick_2']
        ):
        super().__init__()
        self.single_flag = single_flag
        if single_flag:
            self.list_start = list_start_single
        else:
            self.list_start = list_start_team
        self.list_invite = list_invite
        self.list_yes = list_yes
        self.list_tick_1 = list_tick_1
        self.list_tick_2 = list_tick_2

    def if_fail(self):
        if self.single_flag:
            re_invite = player.find_touch_any(self.list_invite, True, False)
            if re_invite:
                time.sleep(0.2)
            re_yes = player.find_touch_any(self.list_yes, True)
            if re_yes:
                time.sleep(0.2)
        else:
            re_tick_1 = player.find_touch_any(self.list_tick_1, True, False)
            if re_tick_1:
                time.sleep(0.3)
            re_tick_2 = player.find_touch_any(self.list_tick_2, True)
            if re_tick_2:
                time.sleep(0.3)


class TanSuoRound(YysRound):

    def __init__(
        self,
        list_start = ['shouling', 'xiaoguai'],
        list_ground = ['ground'],
        list_round_end_1 = ['tansuoend_1'],
        list_round_end_2 = ['tansuoend_2'],
        list_baoxiang = ['baoxiang'],
        list_tansuo = ['tansuo'],
        list_28 = ['k28'],
        ):
        super().__init__()
        self.list_start = list_start
        self.list_ground = list_ground
        self.list_round_end_1 = list_round_end_1
        self.list_round_end_2 = list_round_end_2
        self.list_baoxiang = list_baoxiang
        self.list_tansuo = list_tansuo
        self.list_28 = list_28

    def round_start(self):
        last_flag = 0
        while True:
            re_start = player.find_touch_any(self.list_start, True)
            if re_start == 'shouling':
                last_flag = 1
            re_running = player.find_touch_any(self.list_running, False)
            if re_running == 'running':
                break
            re_start = player.find_touch_any(self.list_start, False)
            if re_start == None and re_running == None:
                re_ground = player.find_touch_any(self.list_ground, True)
                time.sleep(1)
        return last_flag

    def round_end(self):
        while True:
            re_end_1 = player.find_touch_any(self.list_end_1, True)
            re_end_2 = player.find_touch_any(self.list_end_2, True)
            if re_end_2:
                time.sleep(0.8)
            re_end_3 = player.find_touch_any(self.list_end_3, True)
            if re_end_3:
                time.sleep(0.2)
                break

    def round_check(self):
        time.sleep(5.5)
        for i in range(3):
            re_end_1 = player.find_touch_any(self.list_round_end_1, True)
            if re_end_1:
                time.sleep(0.3)
                re_end_2 = player.find_touch_any(self.list_round_end_2, True)
                time.sleep(0.2)
        while True:
            re_baoxiang = player.find_touch_any(self.list_baoxiang, True)
            if re_baoxiang:
                time.sleep(0.5)
                re_end_2 = player.find_touch_any(self.list_end_2, True)
                if re_end_2:
                    time.sleep(0.7)
                re_end_3 = player.find_touch_any(self.list_end_3, True)
            re_tansuo = player.find_touch_any(self.list_tansuo, True)
            if re_tansuo:
                break
            if re_tansuo == None:
                re_28 = player.find_touch_any(self.list_28, True)
                time.sleep(0.8)


class YuLingRound(YysRound):

    def __init__(
        self,
        list_start=['yuling']
        ):
        super().__init__()
        self.list_start = list_start


class HuoDongRound(YysRound):

    def __init__(
        self,
        list_start = ['start_1', 'huodong_1']
        ):
        super().__init__()
        self.list_start = list_start


def huntu_single(round=99):
    huntu_round = YuHun(single_flag=True)
    for i in range(round):
        print('Round {}'.format(i+1))
        huntu_round.round_start()
        time.sleep(10)
        huntu_round.round_end()
        huntu_round.if_fail()


def huntu_team(round=99):
    huntu_round = YuHun(single_flag=False)
    for i in range(round):
        print('Round {}'.format(i+1))
        huntu_round.round_start()
        time.sleep(10)
        huntu_round.round_end()
        huntu_round.if_fail()


def yeyuanhuo(round=30):
    yeyuanhuo_round = YuHun(single_flag=True)
    for i in range(round):
        print('Round {}'.format(i+1))
        yeyuanhuo_round.round_start()
        time.sleep(18)
        yeyuanhuo_round.round_end()


def tupo(round=9):
    tupo_round = TuPoRound()
    for i in range(round):
        print('Round {}'.format(i+1))
        tupo_round.round_start()
        time.sleep(2)
        tupo_round.round_end()


def tansuo_single():
    tansuo_round = TanSuoRound()
    i = 0
    while True:
        print('Round {}'.format(i+1)) 
        last_flag = tansuo_round.round_start()
        tansuo_round.round_end()
        if last_flag == 1:
            print('The last one is dead!')
            tansuo_round.round_check()
        i += 1


def yuling(round=100):
    yuling_round = YuLingRound()
    for i in range(round):
        print('Round {}'.format(i+1))
        yuling_round.round_start()
        time.sleep(2)
        yuling_round.round_end()


def huodong_single(round=9):
    huodong_round = HuoDongRound()
    for i in range(round):
        print('Round {}'.format(i+1))
        huodong_round.round_start()
        time.sleep(5)
        huodong_round.round_end()


def get_screen():   
    player.screen_shot()


def menu(debug=False):

    menu_list = [
        [get_screen,        '获取当前屏幕截图'],
        [huntu_single,      '自动挖土[司机or单人]'],
        [huntu_team,        '自动挖土[打手]'],
        [yeyuanhuo,         '自动业原火'],
        [tupo,              '自动结界突破'],
        [tansuo_single,     '自动困28[单人]'],
        [yuling,            '自动御灵'],
        [huodong_single,    '自动挂机活动'],
    ]

    start_time = time.time()
    print('Start, now: {}\n'.format(time.ctime()))
    while True:
        i = 0
        for func, des in menu_list:
            print('{} : {}\n'.format(i, des))
            i += 1
        player.alarm(1)
        raw = input("Choose function: ") if not debug else 1
        index = int(raw) if raw else 1
        func, des = menu_list[index]
        print('{} is chosen !'.format(des))
        func()

if __name__ == '__main__':
    menu()