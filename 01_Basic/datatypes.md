# Python Built-in Data Types

This document lists all the built-in data types in Python, along with definitions and code examples.

---

## 1. Number

Numeric types represent numbers in Python.

* **int** – Integer values.
* **float** – Floating-point (decimal) values.
* **complex** – Complex numbers (a + bj).

```python
# Integer
a = 10           
# Floating point
b = 3.14         
# Complex number
c = 2 + 3j       

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'complex'>
```

---

## 2. String

String is a sequence of Unicode characters.

```python
s1 = "raj"
s2 = 'hello'
s3 = 'He said "hi"'

print(type(s1))  # <class 'str'>
print(s3)        # He said "hi"
```

---

## 3. Boolean

Boolean type stores `True` or `False`.

```python
is_valid = True
is_ready = False

print(type(is_valid))  # <class 'bool'>
```

---

## 4. List

List is an ordered, mutable collection of items.

```python
lst = [1, 2, 3]
names = ["raj", "dev"]
mixed = [1, "raj", 3.14]

print(type(lst))    # <class 'list'>
print(lst[1])       # 2
```

---

## 5. Tuple

Tuple is an ordered, immutable collection of items.

```python
t = (1, 2, 3)
single = (42,)  # Single-item tuple

print(type(t))      # <class 'tuple'>
print(type(single)) # <class 'tuple'>
```

---

## 6. Set

Set is an unordered collection of unique items.

```python
s = {1, 2, 3, 2}
fruits = {"apple", "banana"}

print(type(s))      # <class 'set'>
print(s)            # {1, 2, 3}
```

---

## 7. Dictionary

Dictionary stores data as key-value pairs.

```python
person = {"name": "raj", "age": 21}
codes = {1: "one", 2: "two"}

print(type(person))     # <class 'dict'>
print(person["name"])   # raj
```

---

## 8. NoneType

Represents the absence of a value.

```python
x = None

print(type(x))  # <class 'NoneType'>
```

---

## 9. Bytes

Immutable sequence of bytes.

```python
b = b"raj"
b2 = bytes([65, 66, 67])

print(type(b))   # <class 'bytes'>
print(b2)        # b'ABC'
```

---

## 10. Bytearray

Mutable sequence of bytes.

```python
ba = bytearray([65, 66, 67])

print(type(ba))   # <class 'bytearray'>
print(ba)         # bytearray(b'ABC')
```

---

## 11. Range

Represents a sequence of numbers.

```python
r = range(5)

print(type(r))    # <class 'range'>
print(list(r))    # [0, 1, 2, 3, 4]
```

---

## 12. Memoryview

A memoryview object is a general way of viewing byte data.

```python
mv = memoryview(b"hello")

print(type(mv))         # <class 'memoryview'>
print(mv[0])            # 104 (ASCII of 'h')
```

---
