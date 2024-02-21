import yunsuan

#程序头
print("华夏计算器\n版本1.0\n需要获取帮助请输入help或h\n")

#程序主循环
while True:
    user_aw = input("输入一个代号：")
    #判断用户输入的代号
    #执行模块帮助
    if user_aw == "help" or "h":
        with open('module_help.txt') as module_help1:
            module_help = module_help1.read()
        print(module_help)    
         
    #执行加法运算
    elif user_aw == "jiafa":
        yunsuan.jiafa()
    
    #执行减法运算
    elif user_aw == "jianfa":
        yunsuan.jianfa()

    #执行乘法运算    
    elif user_aw == "chengfa":
        yunsuan.chengfa()

    #执行除法运算    
    elif user_aw == "chufa":
        yunsuan.chufa()
    
    #执行乘方运算
    elif user_aw == "chengfang":
        yunsuan.chengfang()
    
    #执行取余运算
    elif user_aw == "quyu":
        yunsuan.quyu()
    
    #执行平方根运算
    elif user_aw == "pingfanggen":
        yunsuan.pingfanggen()

    #执行余弦函数运算
    elif user_aw == "cosine":
        yunsuan.cosine()

    #执行正弦函数运算
    elif user_aw == "sine":
        yunsuan.sine()

    #执行正切函数运算
    elif user_aw == "tangent":
        yunsuan.tangent()

    #执行反余弦函数运算
    elif user_aw == "arccos":
        yunsuan.arccos()

    #执行反正弦函数运算
    elif user_aw == "arcsin":
        yunsuan.arcsin()

    #执行反正切函数运算
    elif user_aw == "arctan":
        yunsuan.arctan()

    #执行双曲余弦函数
    elif user_aw == "cosh":
        yunsuan.cosh()

    #执行双曲正弦函数
    elif user_aw == "sinh":
        yunsuan.sinh()

    #执行双曲正切函数
    elif user_aw == "tanh":
        yunsuan.tanh()

    #执行反双曲余弦函数
    elif user_aw == "acosh":
        yunsuan.acosh()

    #执行反双曲正弦函数
    elif user_aw == "asinh":
        yunsuan.asinh()

    #执行反双曲正切函数
    elif user_aw == "atanh":
        yunsuan.atanh()
    

    