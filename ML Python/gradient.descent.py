#########梯度下降法
#############-号的是梯度下降法，求最小值；+号的是梯度上升法，求最大值

def fun(vecx):
    x=vecx[0];y=vecx[1]
    return (1-x)**2 + 100*(y-x**2)**2

def deviantfun(vecx):
    x=vecx[0];y=vecx[1]
    return array([400 * x**3 - 400*x*y +2*x-2 , 200*(y-x**2)])

x0 = array([-1,-1])
alpha = 0.001
for i in range(50000):
    x = x0 - alpha * deviantfun(x0)
    if abs(fun(x)-fun(x0))<1e-6:
        print(x)
        print(i)
        break
    else:x0 = x







###################一元
def fun(x):return x**2 +4 - 4*x

def deviantfun(x):return 2*x - 4

alpha = 0.001
x0 = -3
for i in range(1000):
    x = x0 - alpha * deviantfun(x0)
    if abs(fun(x)-fun(x0))<1e-6:
        print(x)
        break
    else:x0 = x
