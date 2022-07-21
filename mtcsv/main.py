# MODULES
import re



# FUNCTIONS
def write(account,time,money):
    ac = account
    for i in range(2):  # 去除['']
        ti = ','.join(str(i) for i in time)
        mo = ','.join(str(i) for i in money)
    csv.write(f"{ac},{ti},{mo}\n")



# INITIALIZATION
csv = open("ccb.csv", "a+")  # 添加模式
msg = open("msg.txt", "r")  # 只读模式
lines = msg.readlines()



# MAIN CODE
for line in lines:
    # acc - account
	# tim - time
	# mon - money

    if "您尾号7092" in line:
        
        # account
        acc = "7092"
        # time
        if "时" and "分" in line:
            tim = re.findall(r"\d+月\d+日\d+时\d+分", line)
        elif ":" in line:
            tim = re.findall(r"\d+月\d+日\d{2}:\d{2}", line)
        else:  # x时x分
            tim = re.findall(r"\d+月\d+日", line)
        # money
        if "退货/退税入账" in line:            
            if "." in line:  # 退货/退税
                mon = re.findall(r"退货/退税入账\d+\.\d{2}元", line)                
            else:
                mon = re.findall(r"退货/退税入账\d+元", line)        
        elif "消费" in line:
            mon = re.findall(r"消费\d+\.\d{2}元", line)
        elif "存入" in line:
            mon = re.findall(r"存入\d+\.\d{2}元", line)
        elif "还款" in line:
            if "." in line:
                mon = re.findall(r"还款\d+\.\d+元", line)
            else:
                mon = re.findall(r"还款\d+元", line)
        else:
            pass
        write(acc, tim, mon)

    elif "您尾号6298" in line:
        # account
        acc = "6298"
        # time
        if "时" and "分" in line:
            tim = re.findall(r"\d+月\d+日\d+时\d+分", line)
        else:
            tim = re.findall(r"\d+月\d+日\d{2}:\d{2}", line)
        # money
        if "支出" in line:
            if "人民币" in line:
                mon = re.findall(r"支出人民币\d+\.\d{2}元", line)
            else:
                mon = re.findall(r"支出\d+\.\d{2}元", line)
        else:  # 收入
            if "人民币" in line:
                mon = re.findall(r"收入人民币\d+\.\d{2}元", line)
            else:
                mon = re.findall(r"收入\d+\.\d{2}元", line)
		
        write(acc, tim, mon)

    else:  # 尾号0392, 只有一条
        acc = "0392"
        tim = ['22年05月23日']  # findall返回的是列表，所以这里用列表
        mon = ['收入5552.00元']
        write(acc, tim, mon)



# END
msg.close()
csv.close()
