total = 3
pw = "a123456"
input_pw = ""
while total > 0 :
    total -= 1
    input_pw = input("請輸入密碼：")
    if(input_pw == pw):
        print("登入成功")
        break
    else:
        print("密碼錯誤!還有%d次機會" % total)
