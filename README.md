# 1405. Longest Happy String

__Type__: Medium <br>
__Topics:__ String, Greedy, Heap (Priority Queue) <br>
__Companies:__ Google, Microsoft, Amazon, Wayfair, Capgemini, Geico, Bloomberg, Adobe, TikTok <br>
__Leetcode Link:__ [Longest Happy String](https://leetcode.com/problems/longest-happy-string/description/)
<hr>

A string `s` is called **happy** if it satisfies the following conditions:
- `s` only contains the letters `'a'`, `'b'`, and `'c'`.
- `s` does not contain any of `"aaa"`, `"bbb"`, or `"ccc"` as a substring.
- `s` contains at most `a` occurrences of the letter `'a'`.
- `s` contains at most `b` occurrences of the letter `'b'`.
- `s` contains at most `c` occurrences of the letter `'c'`.

Given three integers `a`, `b`, and `c`, return *the **longest possible happy** string*. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string `""`.

A __substring__ is a contiguous sequence of characters within a string.
<hr>

### Examples

- __Example 1:__ <br>
__Input:__ a = 1, b = 1, c = 7 <br>
__Output:__ "ccaccbcc" <br>
__Explanation:__ "ccbccacc" would also be a correct answer.

- __Example 2:__ <br>
__Input:__ a = 7, b = 1, c = 0 <br>
__Output:__ "aabaa" <br>
__Explanation:__ It is the only correct answer in this case.
<hr>

### Constraints:
- `0 <= a, b, c <= 100`
- `a + b + c > 0`
<hr>

### Hints:
- Use a greedy approach.
-  Use the letter with the maximum current limit that can be added without breaking the condition.