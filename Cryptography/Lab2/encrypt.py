import sys
from gmpy2 import mpz  
from gmpy2 import invert
from gmpy2 import powmod  
from gmpy2 import f_mod
from gmpy2 import mul 
b=2**20 
B=mpz(b)  
p=mpz('13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171')  
g=mpz('11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568')  
h=mpz('3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333')  
g_power_b=powmod(g,B,p)   
hash_table={}  
for x1 in range(B):  
    hash_table[f_mod(mul(h,invert(powmod(g,x1,p),p)),p)]=x1
  
print "Table is completed"  
  
for x0 in range(B):  
    middle_value=powmod(g_power_b,x0,p)  
    if hash_table.has_key(middle_value):    
        print x0  
        x1=hash_table[middle_value]  
        print x1  
        break  
  
x=(x0*B+x1)%(p-1)  
print x