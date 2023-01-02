### calculate O(n) for recursive

`T(N) = a*T(N/b) + O(N^d)`

```
n = size of input
a = number of subproblems in the recursion
n/b = size of each subproblem

1. log(b, a) > d -> O(N^log(b, a))
2. log(b, a) = d -> O(N^d * logN)
3. log(b, a) < d -> O(N^d)
```

for example

```java

public static int getMax(int[] arr) {
	return process(arr, 0, arr.lenght - 1);
}

public static int process(int[] arr, int L, int R) {
	if (L == R) {
		return arr[L]
	}
	
//	for (int i = L; i <= R; i++) {
//		System.out.print(arr[i]);
//	}

	int mid = L + ((R-L)/2);
	int leftMax = process(arr, L, mid);
	int rightMax = process(arr, mid + 1, R);
	return Math.max(leftMax, rightMax);
}

a = 2, b = 2, d = 0, so O(N^1)
why d = 0? because the rest of operations a O(N), therefore, d = 0

but if the system out print is discomment
a = 2, b = 2, d = n
```
