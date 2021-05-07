import cv2, numpy, time, os, random, threading
import pyautogui
from winsound import Beep
from PIL import ImageGrab
from settings import *

# 桌面模式下的鼠标操作延迟, 程序已经设置随机延迟这里无需设置修改
pyautogui.PAUSE = 0.01

# 超时2秒未完成则重试, 传输图片时有极小概率卡死
def time_out(func):
    def wrap_func(*args, **kwargs):
        restart = lambda : func(*args, **kwargs)
        timer = threading.Timer(2, restart)
        timer.start()
        func(*args, **kwargs)
        timer.cancel()
    return wrap_func

# 匹配图片时小概率出错, 一般是图片传输时损坏, 重新截图匹配
def retry(func):
    def wrap_func(*args,**kwargs):
        try:
            re = func(*args, **kwargs)
        except:
            print("图片匹配错误, 稍后重试")
            time.sleep(2)
            re = func(*args, **kwargs)
        return re
    return wrap_func

# 截屏并发送到目录 './screen', 默认返回cv2读取后的图片
def screen_shot():
    screen = ImageGrab.grab()
    screen.save('./screen/screen.jpg')        
    screen = cv2.imread('./screen/screen.jpg')
    return screen

# 点击屏幕，参数pos为目标坐标(x, y)
def touch(pos):
    x, y = pos
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y)

# 蜂鸣报警器，参数n为鸣叫次数，可用于提醒出错或任务完成
def alarm(n=3):
    frequency = 1500
    last = 500
    for n in range(n):   
        Beep(frequency, last)
        time.sleep(0.05)

# 按 [cv2读取文件内容, 匹配精度, 图片名称] 格式批量读取要查找的目标图片, 名称为文件名
def load_imgs():
    imgs = {}
    treshold = accuracy
    path = wanted_path
    file_list = os.listdir(path)
    for filename in file_list:
        name = filename.split('.')[0]
        file_path = os.path.join(path, filename)
        a = [cv2.imread(file_path), treshold, name]
        imgs[name] = a
    return imgs
imgs = load_imgs()

# 在背景查找目标图片, 以列表形式返回查找目标的中心坐标
# screen是截屏图片, wanted是找的图片[按上面load_imgs的格式], show是否以图片形式显示匹配结果[调试用]
def locate(screen, wanted, show=0):
    loc_pos = []
    wanted, treshold, c_name = wanted
    result = cv2.matchTemplate(screen, wanted, cv2.TM_CCOEFF_NORMED)
    location = numpy.where(result >= treshold)
    h, w = wanted.shape[:-1] 
    n, ex, ey = 1, 0, 0
    for pt in zip(*location[::-1]):   
        x, y = pt[0] + int(w/2), pt[1] + int(h/2)
        # 去掉邻近重复的点
        if (x-ex) + (y-ey) < 15:  
            continue
        ex, ey = x, y
        cv2.circle(screen, (x, y), 10, (0, 0, 255), 3)
        x, y = int(x), int(y)
        loc_pos.append([x, y])
    # 在图上显示寻找的结果, 调试时开启
    if show:  
        cv2.imshow('we get', screen)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()
    return loc_pos

# 裁剪图片以缩小匹配范围，screen为原图内容，upleft、downright是目标区域的左上角、右下角坐标
def cut(screen, upleft, downright): 
    a, b = upleft
    c, d = downright
    screen = screen[b:d, a:c]
    return screen

# 随机偏移坐标, 防止游戏的外挂检测, p是原坐标(x, y), w, h是目标图像宽高, 返回目标范围内的一个随机坐标
def random_offset(p, w=30, h=30):
    a, b = p
    w, h = int(w/3), int(h/3)
    c, d = random.randint(-w, w), random.randint(-h, h)
    e, f = a + c, b + d
    y = [e, f]
    return y

# 随机延迟点击, 防止游戏外挂检测, 延迟时间范围为[x, y]秒之间
def random_delay(x=0.2, y=0.5):
    t = random.uniform(x, y)
    time.sleep(t)

# 寻找并点击, tap为FALSE则只寻找不点击, 返回结果是否找到TURE/FALSE
def find_touch(target, tap=True):
    screen = screen_shot()
    wanted = imgs[target]
    size = wanted[0].shape
    h, w, _ = size
    pts = locate(screen, wanted)
    if pts:
        print('Get ', target)
        xx = pts[0]
        xx = random_offset(xx, w, h)
        if tap:    
            touch(xx)
            random_delay()
        return True
    else:
        return False

# 寻找并点击, 找到返回目标名, 未找到返回NONE
def find_touch_any(target_list, tap=True, doubleclick=True):
    re = None
    screen = screen_shot()
    for target in target_list:
        wanted = imgs[target]
        size = wanted[0].shape
        h, w, _ = size
        pts = locate(screen, wanted)
        if pts:
            print('Get {}, \tposition: {}'.format(target, pts[0]))
            xx = pts[0]
            xx = random_offset(xx, w, h)
            if tap:      
                touch(xx)
                random_delay()
                if doubleclick:
                    touch(xx)
            re = target
            break
    return re