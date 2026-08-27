import tkinter as tk
import random
import math
import time

root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="#fff0f5")

# Nhấn ESC để thoát
root.bind("<Escape>", lambda e: root.destroy())

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

canvas = tk.Canvas(
    root,
    width=screen_w,
    height=screen_h,
    bg="#fff0f5",
    highlightthickness=0
)
canvas.pack()

# Tiêu đề
title = canvas.create_text(
    screen_w // 2,
    130,
    text="💗 Gửi người tui thương 💗",
    font=("Arial", 40, "bold"),
    fill="#d6336c"
)

message = canvas.create_text(
    screen_w // 2,
    screen_h // 2 - 30,
    text="",
    font=("Arial", 22),
    fill="#5c374c",
    justify="center",
    width=1000
)

text = """Có một điều tui đã muốn nói với ông...

Giữa rất nhiều người trên thế giới,
tui lại may mắn gặp được ông.

Tui thích nụ cười của ông,
thích những điều nhỏ bé ở ông,
và thích cả những ngày bình thường
chỉ vì trong đó có ông.

Tui không cần một tình yêu hoàn hảo.
Tui chỉ muốn được ở bên ông,
cùng ông tạo ra thật nhiều kỷ niệm.

Và nếu ông cho phép...

Tui muốn được ở bên ông thật lâu. ❤️"""

final = canvas.create_text(
    screen_w // 2,
    screen_h - 180,
    text="",
    font=("Arial", 30, "bold"),
    fill="#e0316f"
)

# Nút bắt đầu
button = tk.Button(
    root,
    text="💌 Bấm vào đây...",
    command=lambda: start(),
    font=("Arial", 20, "bold"),
    bg="#ff6b9a",
    fg="white",
    relief="flat",
    padx=40,
    pady=18,
    cursor="hand2"
)

canvas.create_window(
    screen_w // 2,
    screen_h // 2 + 260,
    window=button
)

hearts = []
running = False


def shoot_hearts():
    """Bắn trái tim từ giữa màn hình ra mọi hướng."""

    for i in range(100):
        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(8, 18)

        x = screen_w // 2
        y = screen_h // 2

        heart = canvas.create_text(
            x,
            y,
            text=random.choice(["❤️", "💗", "💕", "💖", "💘"]),
            font=("Arial", random.randint(18, 35))
        )

        hearts.append([
            heart,
            math.cos(angle) * speed,
            math.sin(angle) * speed,
            random.randint(40, 100)
        ])


def animate_hearts():
    if not running:
        return

    alive = []

    for heart in hearts:
        item, dx, dy, life = heart

        canvas.move(item, dx, dy)

        life -= 1
        heart[3] = life

        if life > 0:
            alive.append(heart)
        else:
            canvas.delete(item)

    hearts[:] = alive

    # Bắn thêm tim liên tục
    if random.random() < 0.25:
        shoot_small_hearts()

    root.after(30, animate_hearts)


def shoot_small_hearts():
    x = screen_w // 2 + random.randint(-250, 250)
    y = screen_h // 2 + random.randint(-150, 150)

    heart = canvas.create_text(
        x,
        y,
        text=random.choice(["❤️", "💗", "💕", "💖"]),
        font=("Arial", random.randint(15, 30))
    )

    dx = random.uniform(-4, 4)
    dy = random.uniform(-8, -3)

    hearts.append([heart, dx, dy, random.randint(40, 80)])


def show_message():
    current = ""

    for line in text.split("\n"):
        current += line + "\n"

        canvas.itemconfig(
            message,
            text=current
        )

        root.update()
        time.sleep(0.35)

    canvas.itemconfig(
        final,
        text="💗 ÔNG CÓ ĐỒNG Ý Ở BÊN TUI KHÔNG? CÓ THÌ NHỚ TRẢ LỜI TUI NHA💗"
    )


def start():
    global running

    button.destroy()

    running = True

    # Bắn đợt tim đầu tiên
    shoot_hearts()

    # Bắt đầu hiệu ứng
    animate_hearts()

    # Hiện lời tỏ tình
    root.after(
        500,
        show_message
    )


root.mainloop()