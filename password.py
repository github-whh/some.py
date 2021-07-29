file_open = open("Password", "r")
your_password = file_open.readline()


# 从文件中读取密码

class SolvePassword:

    def __init__(self, word, number=0):
        """初始化函数"""
        self.password = word
        self.number = number


    def encryption(self):
        """解码函数"""
        print("开始加密")
        password_list = list(self.password)
        count = 0
        for char in password_list:
            if char >= "a" and char <= "z":
                char_number = ord(char) + self.number
                if chr(char_number) > "z":
                    char_number -= 26
                password_list[count] = chr(char_number)  # 小写转换
            if char >= "A" and char <= "Z":
                char_number = ord(char) + self.number
                if chr(char_number) > "Z":
                    char_number -= 26
                password_list[count] = chr(char_number)  # 大写转换
            count += 1
        self.encry_password = "".join(password_list)
        return self.encry_password

    def decryption(self):
        """解码函数"""
        print("开始解密")
        encry_password_list = list(self.encry_password)
        count = 0
        for char in encry_password_list:

            if char >= "a" and char <= "z":
                char_number = ord(char) - self.number
                if chr(char_number) < "a":
                    char_number += 26
                encry_password_list[count] = chr(char_number)  # 小写转换
            if char >= "A" and char <= "Z":
                char_number = ord(char) - self.number
                if chr(char_number) < "A":
                    char_number += 26
                encry_password_list[count] = chr(char_number)  # 大写转换
            count += 1
        self.decry_password = "".join(encry_password_list)
        return self.decry_password

    def getencrynumber(self):
        return self.encry_password

    def getdecrynumber(self):
        return self.decry_password

    def __str__(self):
        return "加密后的密码为 %s , 解密之后为 %s" % (self.getencrynumber(), self.getdecrynumber())  # 字符串


while True:
    number = input("请输入一个整数K: ")
    if number.isdigit():
        break
    else:
        print("输入不是整数，请输入一个整数")  # 判断是否为整数

K = int(number) % 26

private_password = SolvePassword(your_password, K)
private_password.encryption()
private_password.decryption()
print(private_password)
file_open.close()
