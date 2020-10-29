#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


def function_for_root(x):
    a = 1.01
    b = -3.04
    c = 2.07
    return a*x**2 + b*x + c


# In[ ]:


def derivitive_for_root(x):
    a = 1.01
    b = -3.04
    return 2*a*x + b


# In[ ]:


def newton_raphson_root_finding(f, dfdx, x_start, tol):
    
    
    flag = 1
    imax = 10000
    i = 0
    
    x_old = x_start
    x_new = 0.0
    y_new = 0.0
    
    while(flag):
        
        x_new = x_old - f(x_old)/dfdx(x_old)
        
        print(x_new, x_old, f(x_old), dfdx(x_old))
        
        y_new = f(x_new)
        
        if(np.fabs(y_new)<tol):
            flag = 0
            
        else:
            
            x_old = x_new
            
            i+=1
            
        if(i>=imax):
            print("max iteration reached")
            raise StopIteration('stopping iteration after',i)
        
    return x_new
            


# In[ ]:


x_start = 0.5
tolerance = 1.0e-6

print(x_start, function_for_root(x_start))

x_root = newton_raphson_root_finding(function_for_root,derivitive_for_root, x_start, tolerance)
y_root = function_for_root(x_root)

s = "root found with y(%f) = %f" % (x_root,y_root)
print(s)


# In[ ]:


x = np.linspace(0, 3, 1000)

y = 1.01*x**2 - 3.04*x + 2.07
z = -0.498*x + 1.025 
w = 0*x


# In[ ]:


fig = plt.figure(figsize=(6,6))

plt.plot(x, y, label=r'$y = (y)$')
plt.plot(x, z, label=r'$y = (z)$')
plt.plot(x, w, label=r'$y = (w)$')

plt.plot(1.96903135229,0,'d')
plt.plot(1.040870,0,'d')

plt.xlabel('f(x)')
plt.ylabel('x')
plt.xlim([0,3])
plt.ylim([-0.5,2.1])
plt.legend(loc=1,framealpha=0.95)


# In[ ]:




