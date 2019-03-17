from sympy import *


x = Symbol('x')

mine=10918*cos(x**8121)*x**10917-8121*x**19038*sin(x**8121)+4879*cos(cos(cos(cos(cos(153))**9142)**9376)**9667)**347*x**4878-2831928*x**7571+3033284*sin(cos(810)**9347)*sin(x**9599)**315*cos(x**9599)*x**9598
ori=x   **  7526 *   cos(x   **  8121) *   x   **  3392 +  x   **  3388 *   cos(cos(cos(cos(cos(+153))**  9142)**  9376)**  9667)**  347 *   x   **  1491    - 374 *   x   **  7572 +  sin(x   **  9599)**  316 *   sin(cos(810)**  9347)
ori = diff(ori)
print(abs(ori.evalf(subs={x : 10}) - mine.evalf(subs={x:10})) < 0.00001)

