# modules
import sqlite3, datetime
from sys import exit
from random import randint
from textwrap import dedent
from numpy import double


# variables
con = sqlite3.connect("main.db")
cur = con.cursor()


# functions
def add_record():
    # get infomation
    now = datetime.datetime.now()
    ID = now.strftime(f"%Y%M%D%H%M%S{randint(1,1000)}")
    date_time = now.strftime("%Y-%M-%D %H:%M:%S")
    money = double(input("输入金额："))
    src = input("钱从哪里来：")
    dst = input("钱到哪里去：")
    note = input("备注：")
    cur.execute(f"INSERT INTO tally_book VALUES({ID}, '{date_time}', {money}, '{src}', '{dst}', '{note}')")

def show_book():
    x = cur.execute("SELECT * FROM tally_book")
    print(dedent("""
        | ID | 时间 | 来龙 | 去脉 | 备注 |
        --------------------------------
    """))
    for r in x:
        print(r)


# main code
while True:
    print(dedent("""
        ----------记账本----------
        \t1 我要记账
        \t2 查看账本
        \tq 退出程序
    """))
    choose = input("输入你的选择：")

    if choose == "1":
        add_record()
        continue
    elif choose == "2":
        show_book()
        continue
    else:
        con.commit()
        con.close()
        exit()