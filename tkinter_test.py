# 参考URL: https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/

# Tkinterのテスト
import tkinter as tk

# Windowを取得する関数
def getWindow():

    # Windowの作成
    root = tk.Tk()
    root.title("Tkinter Test")
    # WIndowをループさせて、継続的にWindowを表示させる
    root.mainloop()

if __name__ == "__main__":
    getWindow()