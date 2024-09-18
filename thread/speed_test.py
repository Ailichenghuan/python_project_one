import time
import tkinter
import tkinter.messagebox

def download():
    """模拟下载任务需要花费10s时间"""

    time.sleep(10)
    tkinter.messagebox.showinfo('提示', '下载完成!')

def show_about():
    tkinter.messagebox.showinfo('作者', '刘子翊(v1.0)')

def main():
    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()