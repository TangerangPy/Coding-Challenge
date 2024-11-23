# Coding Challenge 2024-11-16: The Birthday Bar
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

The length of the segment matches Ron's birth month, and,
The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate.

Example 1
```python
s = [2, 2, 1, 3, 2]
d = 4
m = 2
res = birthday_bar(s, d, m)
print(res) # 2
```

Explanation

Lily wants to find segments summing to Ron's birth day, d = 4 with a length equalling his birth month, m=2. In this case, there are two segments meeting her criteria:  [2,2] and [1,3].

Function Description

Complete the birthday function in the editor below.

birthday has the following parameter(s):

int s[n]: the numbers on each of the squares of chocolate
int d: Ron's birth day
int m: Ron's birth month

Example 2
```python
s = [1, 2, 1, 3, 2]
d = 3
m = 2
res = birthday_bar(s, d, m)
print(res) # 2
```

Example 3
```python
s = [4]
d = 4
m = 1
res = birthday_bar(s, d, m)
print(res) # 1
```

Example 4
```python
s = [1, 1, 1, 1, 1, 1]
d = 3
m = 2
res = birthday_bar(s, d, m)
print(res) # 0
```

source: https://www.hackerrank.com/challenges/the-birthday-bar
