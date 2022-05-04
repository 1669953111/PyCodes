from textwrap import dedent
import time
f = open(f"notes/{time.sfrtime('%Y-%m-%d',time.localtime())}.txt","a+")

def read_notes():
    print(f.read())

def write_notes():
    content = input("输入你想记录的内容> ")
    f.write(content)

def main():
    while True:
        print(dedent("""
        -----记笔记工具-----
        1 查看笔记
        2 记笔记
        3 退出"""))
        choose = input("输入数字> ")
        if choose == "1":
            write_notes()
            continue
        elif choose == "2":
            read_notes()
            continue
        else:
            break
    exit()
