sum = lambda n1,n2:n1+n2
print("total=",sum(13,20))
print("total=",sum(21,40))

g=lambda x:x**2
print("square of anumber:",g(8))

nums = range(2,50)
for i in range(2,8):
              nums = filter(lambda x:x ==i
                            or x%1,nums)
d=lambda x:x*2
print(d(5))
