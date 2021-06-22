This problem has been solved using the gap strategy in DP 

We create a matrix with i -> rows and j-> columns

The difference between i and j is the gap .
Considering the central diagonal , i and j values are same
Hence gap here is zero

Note that , as we traverse through the gap ,i always starts from 0 and j starts from gap value

[![1.jpg](https://i.postimg.cc/Fs1QPVgL/1.jpg)](https://postimg.cc/zVmMvWQz)

### Condition for true in all three expressions

Truth tables : 

[![2.png](https://i.postimg.cc/MGsrhhYb/2.png)](https://postimg.cc/8F6HvX9j)

Any expression can be divided into 3 parts

LHS - operator - RHS

Left side of the expression can either have true value or false value
Right side of the expression can either have true value or false value

+ ltc -> Left true count
+ rtc -> right true count
+ lfc -> right false count
+ rfc -> right false count

[![3.png](https://i.postimg.cc/NMKHkfkX/3.png)](https://postimg.cc/ZBhnTmgY)

The matrix for true values of an expression can be drawn as 

[![4.jpg](https://i.postimg.cc/G2zbtkyJ/4.jpg)](https://postimg.cc/2bqsXLTV)

Similary for false values , 

[![Whats-App-Image-2021-06-22-at-9-38-49-PM.jpg](https://i.postimg.cc/tRZrXFVh/Whats-App-Image-2021-06-22-at-9-38-49-PM.jpg)](https://postimg.cc/pyvQChCT)


Example , 
recursion tree for expression T&F|T

[![5.jpg](https://i.postimg.cc/XvgvBZGL/5.jpg)](https://postimg.cc/qtzr9vG6)

For expression -> (T) & (F|T)

Left side  = T
Right side = F|T

True for and operator -> ltc*rtc i.e Left true count * Right true count
From the true matrix , find the true values for both left and right expressions

If i is the zeroth position of the string and j is the last index of the string
Right side of an expression can be found from index i to k and the Left side can be founf out by k + 1 to j 

The above table's expression can be further minimized , 

If
Total(i,j) = T(i , j) + F(i , j)

AND:

T(i , k)*Total(k+1 , j)

OR:

Total( i ,k )* Total(k+1 , j) - F(i,k) * F(k+1 , j)

XOR:

T(i , k) * F(k+1 , j) + F(i , k)*T( k+1 )



