# Coding Challenge 2024-11-22: Is Sator Square
A Discovery
One fine day while Farmer Arepo Tenaciously Labored at Turning the soil, he discovered a field that was scattered with strange stone tablets. Noticing they were carved with letters in a square pattern, he wisely kept them in case some might be special.

Your Task
Please help Farmer Arepo by inspecting each tablet to see if it forms a valid [Sator Square](https://en.wikipedia.org/wiki/Sator_Square)

is a two-dimentional palindrome, made from words of equal length that can be read in these four ways:
1.    left-to-right    (across)
2.    top-to-bottom    (down)
3.    bottom-to-top    (up)
4.    right-to-left    (reverse)

Example:
```
B A T S
A B U T
T U B A
S T A B
```

Here are the four ways a word (in this case "TUBA") can be read:

```
                         down
                          ↓
           B A T S    B A T S    B A T S    B A T S
           A B U T    A B U T    A B U T    A B U T ← reverse
  across → T U B A    T U B A    T U B A    T U B A
           S T A B    S T A B    S T A B    S T A B
                                   ↑
                                   up
```

IMPORTANT
- In a true Sator Square, ALL of its words can be read in ALL four of these ways.
- If there is any deviation, it would be false to consider it a Sator Square.

source: https://www.codewars.com/kata/5cb7baa989b1c50014a53333
