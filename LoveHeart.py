import tkinter as tk
import math
import random
import time


class HeartWindow:
    def __init__(self, master, text, x, y, color):
        self.master = master
        self.text = text
        self.x = x
        self.y = y
        self.color = color

        # 创建窗口
        self.window = tk.Toplevel(master)
        self.window.title("大学祝福")
        self.window.geometry(f"240x120+{int(x)}+{int(y)}")
        self.window.configure(bg=color)
        self.window.attributes("-topmost", True)  # 确保窗口在最前面

        # 添加祝福文本
        label = tk.Label(self.window, text=text, font=("微软雅黑", 10, "bold"),
                         bg=color, fg="white", wraplength=220, justify="center")
        label.pack(expand=True, fill="both", padx=12, pady=12)

        # 添加关闭按钮
        close_btn = tk.Button(self.window, text="关闭", command=self.close_window,
                              bg="white", fg=color, font=("微软雅黑", 8),
                              relief="raised", bd=2)
        close_btn.pack(pady=5)

    def close_window(self):
        self.window.destroy()


class HeartEffect:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("大学生爱心祝福")
        self.root.geometry("400x220")
        self.root.configure(bg="#2C2C2C")

        # 原创大学生祝福语列表
        self.blessings = [
            "愿你的大学时光如诗如画，精彩纷呈",
            "学海无涯，愿你在知识的海洋中乘风破浪",
            "青春正好，不负韶华，书写属于你的传奇",
            "愿你的梦想在大学里生根发芽，茁壮成长",
            "四年光阴，愿你收获知识、友谊与成长",
            "勇敢追梦，不畏挑战，未来因你而精彩",
            "愿你在大学找到人生的方向与无限可能",
            "珍惜青春岁月，创造属于你的辉煌篇章",
            "学有所成，心有所向，未来可期",
            "愿你以梦为马，不负青春，不负自己",
            "大学是新的起点，愿你展翅高飞向未来",
            "愿你的努力终将绽放最美丽的人生花朵",
            "在知识的殿堂里，遇见更好的自己",
            "把握青春，珍惜当下，创造无限可能",
            "愿你心怀理想，脚踏实地，勇往直前",
            "大学时光，愿你收获成长、快乐与智慧",
            "用奋斗书写青春，用汗水浇灌梦想之花",
            "愿你在这里找到志同道合的伙伴与知己",
            "四年耕耘，终将收获丰硕的人生果实",
            "勇敢做自己，不畏将来，不念过往",
            "愿你的大学生活丰富多彩，充满意义",
            "在追梦的路上，愿你永远保持初心与热情",
            "大学是人生的加油站，愿你加满能量再出发",
            "愿你在这里学会独立思考，成为更好的自己",
            "青春不留白，大学不留憾，勇敢向前行",
            "知识改变命运，大学成就未来，加油",
            "愿你的每一天都充满阳光与希望",
            "把握机会，展现自我，创造精彩人生",
            "大学是梦想的摇篮，愿你在这里茁壮成长",
            "愿你的大学生活成为一生中最美的回忆",
            "勤奋是成功的阶梯，坚持是胜利的钥匙",
            "愿你在这里收获知识，更收获人生的智慧",
            "大学时光短暂而珍贵，请好好珍惜",
            "愿你以热情拥抱生活，以智慧面对挑战",
            "在大学里找到真正的自己，实现人生价值",
            "愿你的努力不被辜负，梦想终将实现",
            "青春无悔，奋斗无价，大学加油",
            "愿你在这里结交良师益友，共同进步",
            "大学是人生的转折点，愿你把握方向",
            "愿你在这里发现自己的潜力，超越自我"
        ]

        # 青春活力的颜色列表
        self.colors = [
            "#FF6B6B", "#4ECDC4", "#FFD166", "#06D6A0",
            "#118AB2", "#EF476F", "#7209B7", "#3A86FF",
            "#FB5607", "#FF006E", "#8338EC", "#FFBE0B",
            "#1A936F", "#88D498", "#C6D4FF", "#9C89B8",
            "#F3722C", "#F8961E", "#43AA8B", "#577590",
            "#F94144", "#F3722C", "#F8961E", "#90BE6D",
            "#277DA1", "#577590", "#4D908E", "#43AA8B",
            "#F9844A", "#F8961E", "#F9C74F", "#90BE6D",
            "#F94144", "#F3722C", "#F8961E", "#F9844A"
        ]

        # 创建标题
        title_label = tk.Label(self.root, text="🎓 大学生爱心祝福 🎓",
                               font=("微软雅黑", 16, "bold"),
                               bg="#2C2C2C", fg="#4ECDC4")
        title_label.pack(pady=12)

        # 创建控制按钮框架
        button_frame = tk.Frame(self.root, bg="#2C2C2C")
        button_frame.pack(pady=15)

        # 创建重新生成按钮
        regenerate_btn = tk.Button(button_frame, text="🔄 重新生成", command=self.start_animation,
                                   bg="#FF6B6B", fg="white", font=("微软雅黑", 11, "bold"),
                                   padx=18, pady=6, relief="raised", bd=3)
        regenerate_btn.pack(side=tk.LEFT, padx=8)

        # 创建关闭所有窗口按钮
        close_all_btn = tk.Button(button_frame, text="❌ 关闭所有", command=self.close_all_windows,
                                  bg="#118AB2", fg="white", font=("微软雅黑", 11, "bold"),
                                  padx=18, pady=6, relief="raised", bd=3)
        close_all_btn.pack(side=tk.LEFT, padx=8)

        # 创建退出程序按钮
        exit_btn = tk.Button(button_frame, text="🚪 退出程序", command=self.root.quit,
                             bg="#7209B7", fg="white", font=("微软雅黑", 11, "bold"),
                             padx=18, pady=6, relief="raised", bd=3)
        exit_btn.pack(side=tk.LEFT, padx=8)

        # 创建说明文字
        info_label = tk.Label(self.root,
                              text="程序启动后自动展现爱心祝福，窗口会依次出现形成动画效果",
                              font=("微软雅黑", 9), bg="#2C2C2C", fg="#BDC3C7")
        info_label.pack(pady=8)

        self.windows = []
        self.window_positions = []
        self.current_window_index = 0

        # 程序启动后立即创建爱心窗口动画
        self.root.after(500, self.start_animation)

        self.root.mainloop()

    def heart_function(self, t):
        """爱心参数方程"""
        x = 16 * (math.sin(t) ** 3)
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        return x, y

    def calculate_heart_positions(self):
        """计算爱心形状的位置"""
        # 获取屏幕尺寸
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # 爱心中心点
        center_x = screen_width // 2 - 120
        center_y = screen_height // 2 - 60

        # 计算所有窗口位置
        num_windows = 40
        positions = []

        for i in range(num_windows):
            t = 2 * math.pi * i / num_windows
            x, y = self.heart_function(t)

            # 缩放并调整位置（增大爱心尺寸）
            scaled_x = x * 25 + center_x
            scaled_y = -y * 25 + center_y  # 负号是为了翻转Y轴
            positions.append((scaled_x, scaled_y))

        return positions

    def start_animation(self):
        """开始动画效果"""
        # 先关闭之前的所有窗口
        self.close_all_windows()

        # 计算爱心位置
        self.window_positions = self.calculate_heart_positions()

        # 重置索引
        self.current_window_index = 0

        # 开始动画
        self.animate_heart()

    def animate_heart(self):
        """动画效果：依次创建窗口"""
        if self.current_window_index < len(self.window_positions):
            # 获取当前位置
            x, y = self.window_positions[self.current_window_index]

            # 随机选择祝福语和颜色
            blessing = random.choice(self.blessings)
            color = random.choice(self.colors)

            # 创建窗口
            try:
                window = HeartWindow(self.root, blessing, x, y, color)
                self.windows.append(window)
            except Exception as e:
                print(f"创建窗口时出错: {e}")

            # 增加索引，准备创建下一个窗口
            self.current_window_index += 1

            # 安排下一个窗口的创建（间隔150毫秒）
            self.root.after(150, self.animate_heart)

    def close_all_windows(self):
        """关闭所有祝福窗口"""
        for window in self.windows:
            try:
                if hasattr(window, 'window') and window.window.winfo_exists():
                    window.window.destroy()
            except Exception as e:
                print(f"关闭窗口时出错: {e}")

        self.windows = []


if __name__ == "__main__":
    app = HeartEffect()