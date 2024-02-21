import math

#定义加法运算
def jiafa():
    jiafa_a = int(input("输入第一个加数："))
    jiafa_b = int(input("输入第二个加数："))
    jiafa_c = jiafa_a + jiafa_b
    print(f"结果：{jiafa_c}")
    
#定义减法运算
def jianfa():
    jianfa_a = int(input("输入被减数："))
    jianfa_b = int(input("输入减数："))
    jianfa_c = jianfa_a -jianfa_b
    print(f"结果：{jianfa_c}")
    
#定义乘法运算
def chengfa():
    chengfa_a = int(input("输入第一个乘数："))
    chengfa_b = int(input("输入第二个乘数："))
    chengfa_c = chengfa_a * chengfa_b
    print(f"结果：{chengfa_c}")
    
#定义除法运算
def chufa():
    chufa_a = int(input("输入被除数："))
    chufa_b = int(input("输入除数："))
    chufa_c = chufa_a / chufa_b
    print(f"结果：{chufa_c}")
    
#定义乘方运算
def chengfang():
    chengfang_a = int(input("输入底数："))
    chengfang_b = int(input("输入指数："))
    chengfang_c = chengfang_a ** chengfang_b
    print(f"结果：{chengfang_c}")
    
#定义取余运算
def quyu():
    quyu_a = int(input("输入被除数："))
    quyu_b = int(input("输入除数："))
    quyu_c = quyu_a % quyu_b
    print(f"结果：{quyu_c}")
    
#定义平方根运算
def pingfanggen():
    pingfanggen_a = int(input("输入被开方数："))
    pingfanggen_b = math.sqrt(pingfanggen_a)
    print(f"结果：{pingfanggen_b}")
    
#定义余弦函数运算
def cosine():
    cosine_a = int(input("输入角度："))
    cosine_b = math.cos(cosine_a)
    print(f"结果：{cosine_b}")
    
#定义正弦函数运算
def sine():
    sine_a = int(input("输入角度："))
    sine_b = math.sin(sine_a)
    print(f"结果：{sine_b}")
    
#定义正切函数运算
def tangent():
    tangent_a = int(input("输入角度："))
    tangent_b = math.tan(tangent_a)
    print(f"结果：{tangent_b}")
    
#定义反余弦函数运算
def arccos():
    arccos_a = int(input("输入角度："))
    arccos_b = math.acos(arccos_a)
    print(f"结果：{arccos_b}")
    
#定义反正弦函数运算
def arcsin():
    arcsin_a = int(input("输入角度："))
    arcsin_b = math.asin(arcsin_a)
    print(f"结果：{arcsin_b}") 
    
#定义反正切函数运算
def arctan():
    arctan_a = int(input("输入角度："))
    arctan_b = math.atan(arctan_a)
    print(f"结果：{arctan_b}")
    
#定义双曲余弦函数
def cosh():
    cosh_a = int(input("输入角度："))
    cosh_b = math.cosh(cosh_a)
    print(f"结果：{cosh_b}")
    
#定义双曲正弦函数
def sinh():
    sinh_a = int(input("输入角度："))
    sinh_b = math.sinh(sinh_a)
    print(f"结果：{sinh_b}")
    
#定义双曲正切函数
def tanh():
    tanh_a = int(input("输入角度："))
    tanh_b = math.tanh(tanh_a)
    print(f"结果：{tanh_b}")
    
#定义反双曲余弦函数
def acosh():
    acosh_a = int(input("输入角度："))
    acosh_b = math.acosh(acosh_a)
    print(f"结果：{acosh_b}")
    
#定义反双曲正弦函数
def asinh():
    asinh_a = int(input("输入角度："))
    asinh_b = math.asinh(asinh_a)
    print(f"结果：{asinh_b}")
    
#定义反双曲余弦函数
def atanh():
    atanh_a = int(input("输入角度："))
    atanh_b = math.atanh(atanh_a)
    print(f"结果：{atanh_b}")

   