import random
def power(x,y,p):
 result = 1;
 x = x%p;
 while ( y > 0):
  if ( y & 1 ):
   result =  (result * x ) % p ;
  y = y>>1;
  x = ( x * x ) % p ;
 return result;
def test(d,n):
 a= 2 + random.randint(1 , n-4 );
 x = power(a,d,n);
 if ( x == 1 or x == n-1 ):
  return True ;
 while ( d != n-1 ):
  x= ( x * x ) % n ; 
  d *= 2 ;
  if ( x== 1):
    return False;
  if ( x== n-1 ):
    return True;
 return False;
def prime(n,k):
 if ( n <= 1 or n == 4):
  return False;
 if ( n <= 3 ):
  return True ;
 d = n - 1;
 while ( d % 2 == 0 ):
  d //= 2 ;
 for i in range(k):
  if (test(d,n) == False):
    return False;
 return True;
k = 4 ;
print(" All primes smaller than  90: " );
for n in range ( 1 , 90):
 if ( prime(n,k)):
  print( n , end = " ");

