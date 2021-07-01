import base64

    #base64转普通文件
def Base64FileToFile():
    #读取文件
    ofile = open(input("需要将base64转换为普通格式的文件路径名："))
    nfile = (input("转成普通格式输出的文件名："))
    #逐行写入
    for line in ofile.readlines():
        with open(nfile, "a") as mon:
            mon.writelines(base64ToStr(line))


    #普通文件转base64
def FileToBase64File():
    ofile = open(input("需要转换成base64编码的文件路径名："))
    nfile = (input("转成base64格式输出的文件名："))

    # 逐行写入
    for line in ofile.readlines():
        with open(nfile, "a") as mon:
            mon.writelines(strToBase64(line)+"\n")



def strToBase64(s):
    '''
    将字符串转换为base64字符串
    :param s:
    :return:
    '''
    strEncode = base64.b64encode(s.encode('utf8'))
    return str(strEncode, encoding='utf8')


def base64ToStr(s):
    '''
    将base64字符串转换为字符串
    :param s:
    :return:
    '''
    strDecode = base64.b64decode(bytes(s, encoding="utf8"))
    return str(strDecode, encoding='utf8')

# 没用的东西比如ache
def Achebanner():
    print("              .__  \n"
          "_____    ____ |  |__   ____ \n"
          "\__  \ _/ ___\|  |  \_/ __ \ \n"
          " / __ \\  \___|   Y  \  ___/          Base64 ---change---             \n"
          "(____  /\___  >___|  /\___  >\n"
          "    \/     \/     \/     \/                                                  ------ache\n")

if __name__ == '__main__':
    base64Tstr = "1"
    strTbase64 = "2"

    Achebanner()
    print(""
        "如果您需要将普通文件转为base64编码请输入1： \n"
          "如果您需要将base64转为普通文件请输入2  \n")
    flag1 =  input()
    if flag1 == base64Tstr:
        FileToBase64File()
    else:
        Base64FileToFile()