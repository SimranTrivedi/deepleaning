def factorial(n):
    p=1;
    for i in range(1,n+1):
       p=p*i;
    return p;

my_fact=factorial(4);
print(my_fact);

