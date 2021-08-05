#!/usr/bin/env python
# -*- coding: utf-8 -*- 

""" 
Bài 1: (Amazon, Facebook) 
Cho 1 xâu kí tự (string) s, tìm kí tự không lặp lại đầu tiên và trả về vị trí (index). 

Ví dụ 1:
Input: s = "leetcode"
Output: 0

Ví dụ 2:
Input: s = "loveleetcode"
Output: 2

Ví dụ 3:
Input: s = "aabb"
Output: -1  
"""
s1 = "leetcode"
s2 = "loveleetcode"
s3 = "aabb"

# Cách 1: Sử dụng Counter

import collections
def firstUniqChar(s):
        # Tạo hash map số lần xuất hiện các ký tự
        count = collections.Counter(s)
        
        # Tìm index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        # Nếu ko tìm thấy kí tự nào thì trả về -1
        return -1

print(" Test cách 1: ")
a = firstUniqChar(s1)
print("a: ", a)
b = firstUniqChar(s2)
print("b: ", b)
c = firstUniqChar(s3)
print("c: ", c)

# Cách 2: 

def firstUniqChar2(s):
    # Taọ biến gồm các ký tự trong bảng chữ cái
    letters='abcdefghijklmnopqrstuvwxyz'
    # Tìm index của các kí tự xuất hiện 1 lần
    index=[s.index(l) for l in letters if s.count(l) == 1]
    # Trả về index nhỏ nhất hoặc -1
    return min(index) if len(index) > 0 else -1

print(" Test cách 2: ")
a = firstUniqChar2(s1)
print("a: ", a)
b = firstUniqChar2(s2)
print("b: ", b)
c = firstUniqChar2(s3)
print("c: ", c)


# Cách 3: 

def firstUniqChar3(s):
    # Tạo từ điển d
    d = {}
    # Tạo set seen
    seen = set()
    # duyệt các kí tự trong xâu s
    for idx, c in enumerate(s):
        # Nếu kí tự c chưa có trong set seen
        if c not in seen:
            # Lưu kí tự tiếp theo vào từ điển d, có value là index idx
            d[c] = idx
            # Thêm kí tự c vào set seen
            seen.add(c)
        # nếu c đã có trong set seen, tức là c xuất hiện trong xâu s từ 1 lần trở lên
        # -> xóa c trong từ điển d -> trong d gồm các kí tự xuất hiện 1 lần có value là index idx
        elif c in d:
            del d[c]
    return min(d.values()) if d else -1

print(" Test cách 3: ")
a = firstUniqChar3(s1)
print("a: ", a)
b = firstUniqChar3(s2)
print("b: ", b)
c = firstUniqChar3(s3)
print("c: ", c)


# Having fun!