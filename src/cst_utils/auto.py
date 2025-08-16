"""自动化计算机操作"""

import time

import pyautogui as pg

# 全局设置：全局暂停，单位为秒
pg.PAUSE = 0.1


class Mouse:
    @staticmethod
    def mouse_down():
        pass

    @staticmethod
    def mouse_up():
        pass

    @staticmethod
    def click():
        # button:默认左键，左键 left，右键 right,中键 middle
        # clicks:点击次数，默认是1次
        # interval:每次点击间隔时间，默认是0
        # duration:持续时间，默认是0
        pg.click(x=90, y=100, clicks=2, interval=0, duration=0, button="left")

    @staticmethod
    def doublee_click():
        pg.doubleClick(x=90, y=100, duration=0, button="left")

    @staticmethod
    def move_to():
        pg.moveTo()

    @staticmethod
    def drag():
        # 相对拖拽
        # #默认左键，左键 left，右键 right,中键 middle
        pass

    @staticmethod
    def drag_to():
        # 绝对位置拖拽
        pass


class KeyBoard:
    KEYBOARD_KEYS = pg.KEYBOARD_KEYS

    @staticmethod
    def write():
        # 键盘操作
        # 输入字符
        # messge:想要输入的字符
        # interval:每次输入间隔时间，默认是0
        # 不能直接输入中文，需要使用unicode编码
        # 输入时应先使输入框获取焦点，否则无法输入（可以先单击一下）
        pg.write("Hello, World!", interval=0.2)

    @staticmethod
    def hotkey():
        # 热键操作
        # interval:每次按键间隔时间，默认是0
        pg.hotkey("ctrl", "a", interval=0.2)


class Auto:
    @staticmethod
    def hotkey():
        pg.hotkey("win", "d")  # 自动按键，显示桌面

    @staticmethod
    def show_msg(msg: str):
        time.sleep(0.5)
        pg.alert(msg)


class Msg:
    @staticmethod
    def alert():
        # 消息框
        # title:标题
        # text:文本
        # button:按钮，默认是OK
        # 返回值：默认是OK
        arr1 = pg.alert(title="Hello, World!", text="没钱只能当牛马", button="ok")
        print(arr1)

    @staticmethod
    def confirm():
        # 可以设置多个button
        # 返回值：返回用户点击的按钮
        arr2 = pg.confirm(
            title="Hello, World!", text="没钱只能当牛马", buttons=["ok", "cancel"]
        )
        print(arr2)

    @staticmethod
    def prompt():
        # 自带文本输入框的消息框
        # 返回值：返回用户输入的内容
        # 文本输入框没字返回：None
        arr3 = pg.prompt(
            title="Hello, World!", text="没钱只能当牛马", default="请您输入："
        )
        print("您输入的内容是：" + arr3)

    @staticmethod
    def passwword():
        # 自带密码的文本输入框的消息框
        # 返回值：返回用户输入的密码
        # 密码没字返回：None
        arr4 = pg.password(
            title="Hello, World!", text="没钱只能当牛马", default="请您输入：", mask="*"
        )
        print("您输入的密码是：" + arr4)


class Screen:
    @staticmethod
    def shot():
        # 屏幕截图
        # imageformat:截图保存的格式，默认是png
        # region:截图的范围，默认是整个屏幕
        # 截取全屏 在1920 x 1080屏幕上，screenshot（）函数大约需要100毫秒-不快但不慢。
        # 截取全屏，并以图片保存
        pg.screenshot("screenshot.png")

    @staticmethod
    def shot_region():
        # 指定区域内截屏
        # region:截图的范围，默认是整个屏幕 : [开始位置x,开始位置y,x扩展的分辨率,y扩展的分辨率]
        pg.screenshot("screenshot.png", region=[100, 100, 500, 500])

    @staticmethod
    def locate_center_on_screen():
        # 图片定位
        # 定位到的图片的坐标（从左到右，从上到下）
        # image:图片路径
        # confidence:定位精度，默认是0.8
        # count:定位到的图片数量，默认是1
        # 返回图片中心点

        pg.locateCenterOnScreen("screenshot.png", confidence=0.1)


if __name__ == "__main__":
    pg.moveTo()
    print(pg.size())
