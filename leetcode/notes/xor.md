#### xor 
[source](https://www.bilibili.com/video/BV13g41157hK/?p=3&spm_id_from=pageDriver&vd_source=d83d468f086d13c082a5571ce1ae896d) @ 35
same value is 0
different is 1

1 1 0
1 0 1
0 1 1
0 0 0

* other example
1. 0 ^ N = N
2. N ^ N = 0
3. a ^ b = b ^ a
4. (a^b)^c=a^(b^c)

* example 
```
// this method works only when these two variables are in different memory
// location, otherwise it will become 0 because same value is 0
int a = 17
int b = 23

// swap value
a = a ^ b;

// b = (a ^ b) ^ b = a ^ 0 = a
b = a ^ b;

// a = a ^ b ^ a = 0 ^ b = b
a = a ^ b;
```


* & both 1 equal 1
  * 0&0 = 0
  * 0&1 = 0
  * 1&0 = 0
  * 1&1 = 1
* | both 0 equal 0
  * 0|0 = 0
  * 0|1 = 1
  * 1|0 = 1
  * 1|1 = 1
* ^ equal 0, otherwise 1
* ~ 0 -> 1, 1 -> 0