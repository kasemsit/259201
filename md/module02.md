---
jupyter:
  jupytext:
    formats: notebook//ipynb,md//md
    main_language: python
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.4
  kernelspec:
    display_name: Python 3
    name: python3
---

<!-- #region -->
# Variables and Types, Operators, Input/Output


```{admonition} Topics
- โครงสร้างของ Python โปรแกรม (program structure)
- ตัวแปร (variables)
 - ชนิดของข้อมูล (data types)
 - การกำหนดชื่อตัวแปร (variable name)
- ตัวดำเนินการ (operators)
 - คำสั่งทางคณิตศาสตร์ (math module)
- การนำข้อมูลเข้าและการแสดงผล (input/output)
 - การจัดรูปแบบการแสดงผลด้วย *f-string*
```

## Example of Python Script

```{code-block} python
# นำเข้าคำสั่งภายนอก (bring in external functions)
import datetime

print("----- Age Calculate Program -----")
# รับค่าอินพุตนำไปกำหนดค่าตัวแปร (get input, store in a variable)
yob = input("What's your year of birth? (e.g., 2004): ")

# ประมวลผล (process data using variables)
today = datetime.date.today()       # ดึงค่า วัน-เวลา ปัจจุบัน (get current date)
year = today.year                   # สนใจเฉพาะ ปี ปัจจุบัน (get only year part)
age = year - int(yob)               # คำนวณอายุ (caculate age)

# แสดงผล (display output)
print("You are", age , "years old.")       # ดึงค่าของตัวแปร (access variable)
print()
print("Congratulations on your first Python program.")
```


## Variables

- **ตัวแปร** (Variable) – การกำหนดชื่อให้พื้นที่ในหน่วยความจำ
 - สามารถใช้ชื่อตัวแปร ในการอ้างอิงภายหลังได้
- ผู้เขียนโปรแกรมควรกำหนด**ชื่อตัวแปร**ให้สอดคล้องกับข้อมูลที่จัดเก็บ
- กฎการตั้งชื่อ **Python Identifier** (ชื่อตัวแปรหรือชื่อฟังก์ชัน)
 - ใช้อักษร lowercase (`a`-`z`) หรือ uppercase (`A`-`Z`)
 - ใช้ underscore (`_`) ได้ เช่น `var_1`, `print_this_to_screen`
 - **ห้าม**ขึ้นต้นด้วยตัวเลข เช่น `1variable` (ไม่ถูกต้อง)
 - **ห้าม**ใช้เครื่องหมายพิเศษอื่นๆ เช่น `!`, `@`, `#`, `$`, `%`
 - **ห้าม**ตั้งชื่อตรงกับ Keyword ของภาษา Python


### Python Keywords
<!-- #endregion -->

```python tags=["hide-output"]
import keyword
print(keyword.kwlist)
```

<!-- #region -->
## Data Types

การเลือก**ชนิดของข้อมูล**ที่จัดเก็บในตัวแปรให้เหมาะสมกับการใช้งาน ถือเป็นเรื่องสำคัญของการเขียนโปรแกรมคอมพิวเตอร์


### ชนิดข้อมูลพื้นฐาน

ชนิดของข้อมูลพื้นฐานที่สำคัญในการเขียนโปรแกรม ได้แก่

- `string` : ข้อความ
- `int` : เลขจำนวนเต็ม
- `float` : เลขทศนิยม
- `boolean` : ค่าความจริง (`True`/`False`)

**ตัวอย่าง**

```python
str1 = 'hello' # ข้อความ (string)
str2 = "2345"  # ข้อความ (string)
var1 = 50000   # จำนวนเต็ม (int)
var2 = 10/2    # จำนวนจริง (float)
var3 = 1.23e9  # จำนวนจริง (float)
var4 = False   # ค่าความจริง (boolean)
```
<!-- #endregion -->

```python tags=["hide-output"]
var1 = 100*2
print(var1)
```

```python tags=["hide-output"]
var2 = 1_000_000+1
print(var2)
```

```python tags=["hide-output"]
var3 = 10/2
print(var3)
```

```python tags=["hide-output"]
s1 = "this is a string"
print(s1)
```

### ข้อความ (string) ในภาษา Python

- ข้อความสั้น ๆ, ประโยค, ตัวเลข ซึ่ง**อยู่ภายใต้เครื่องหมาย `quote`**
- เครื่องหมาย `quote` ได้แก่ **`'...'`** (single), **`"..."`** (double), **`'''...'''`** (triple)
- บางกรณีอาจต้องเลือกใช้ชนิดของ `quote` ให้เหมาะสมกับข้อความที่จัดเก็บ

```python tags=["hide-output"]
# simple string
print('this is a simple string.')
```

```python tags=["hide-output"]
# string with single quote inside
print("this isn't a simple string.")
```

```python tags=["hide-output"]
# string with double quote inside
print('this is how to print "double quote" in sentence.')
```

```python tags=["hide-output"]
# string that spans multiple lines
s2 = '''this is another string
this is 2nd line
this is 3rd line'''

print(s2)
```

<!-- #region -->
### อักขระพิเศษ (Escape Code)

 - ในภาษาคอมพิวเตอร์ มักมีการใช้งานอักขระพิเศษร่วมกับข้อความ (string) เพื่อให้เกิดการแสดงผลแบบต่าง ๆ เช่น การขึ้นบรรทัดใหม่ การแท็บ การลบอักขระ
 - อักขระเหล่านี้เมื่ออยู่ในโค้ดของโปรแกรม ปกติแล้วจะนำหน้าด้วย **`Escape Character`** ( **`\`** )
 - อักขระพิเศษที่มีการใช้งายบ่อย ๆ ได้แก่ `\n`, `\t`


Escape Code | Description
------------|-------------
`\n` | newline
`\r` | carriage return
`\t` | tab
`\v` | vertical tab
`\b` | backspace
`\f` | form feed (page feed)
`\a` | alert (beep)
`\'` | single quote (\')
`\"` | double quote (\")
`\\` | backslash (\\)
<!-- #endregion -->

```python tags=["hide-output"]
print('This is 1st line')
print('This is 2nd line \nThis is 3rd line')
print()
print('This is 4th line \t\tand this is separated by 2 tabs')
```

<!-- #region -->
### ตัวแปรในภาษา Python อาจมีชนิดข้อมูลไม่ตายตัว

- ตัวแปรในภาษา Python แต่ละตัวไม่จำเป็นต้องมีชนิดตายตัว (เหมือนกับในภาษา C/C++, Java, C#)

- **เราสามารถใช้ตัวแปรเดียวกันเปลี่ยนไปเก็บข้อมูลชนิดอื่น ๆ ได้หากต้องการ**  จุดนี้ทำให้สะดวกต่อการใช้งาน แต่ในขณะเดียวกันก็อาจ**เสี่ยงต่อการเกิดข้อผิดพลาด**ได้เช่นกัน

- การ**ตรวจสอบประเภทของข้อมูลที่จัดเก็บ**ในตัวแปร ทำได้ด้วยคำสั่ง `type()`

```python
type(ข้อมูล)
```

**ตัวอย่าง**
<!-- #endregion -->

```python tags=["hide-output"]
type('Hello')
```

```python tags=["hide-output"]
type(1)
```

```python tags=["hide-output"]
type(1.234)
```

```python tags=["hide-output"]
type(1.23e11)
```

```python tags=["hide-output"]
s2 = 2500+1000            # int
print(s2)
print( type(s2) )
```

```python tags=["hide-output"]
s2 = s2/2                 # float
print(s2)
print( type(s2) )
```

```python tags=["hide-output"]
s2 = 'hello ' + 'there'   # string concatenation
print(s2)
print( type(s2) )
```

เลือกใช้ operator ให้สอดคล้องกับชนิดของข้อมูล เช่น

- `number` (ตัวเลข) `+` `number` (ตัวเลข) ได้ตามหลักคณิตศาสตร์
- `string` (ข้อความ) `+` `string` (ข้อความ) ได้ แต่มักหมายถึงการนำข้อความมาเรียงต่อกัน (concatenation)
- **`string` (ข้อความ) `+` `number` (ตัวเลข) ไม่ได้ จะเกิด `Type error`**

```python tags=["raises-exception"]
s2 + 1
```

<!-- #region -->
## Type Conversions

- **การเปลี่ยนชนิดของข้อมูล**ให้เหมาะสมก่อนใช้งานเป็นเรื่องที่เกิดขึ้นได้
- บางครั้ง Python จะเปลี่ยนชนิดข้อมูลให้อัตโนมัติ เช่น เมื่อคำนวณค่า `int` ร่วมกับ `float` ค่าของ `int` จะถูกแปลงเป็น `float` โดยอัตโนมัติ


### Number Conversions

เราสามารถแปลงข้อมูลตัวเลข (number) ไปมาระหว่าง `int` กับ `float` ได้ด้วยคำสั่ง

- `int()` : แปลงให้ข้อมูลเป็น**จำนวนเต็ม**
- `float()` : แปลงให้ข้อมูลเป็น**จำนวนทศนิยม**
<!-- #endregion -->

```python tags=["hide-output"]
print(99+1.23)
```

```python tags=["hide-output"]
i = int(42+3.5)
print(i)
print( type(i) )
```

```python tags=["hide-output"]
f = float(i)
print(f)
print( type(f) )
```

<!-- #region -->
### String Conversions

- เราสามารถใช้ `int()` และ `float()` เพื่อแปลง**ข้อความ (string) ที่มีรูปแบบตัวเลข** ให้มีค่าเป็นตัวเลข (number) ได้เช่นกัน
```python
c = float('30.5') # c=30.5
d = int('100')    # d=100
```

- หาก**ข้อความไม่อยู่ในรูปของตัวเลขที่เหมาะสม**จะเกิด `value error`

- เราสามารถแปลงข้อมูลตัวเลขให้เป็นข้อความได้ด้วยคำสั่ง `str()`
<!-- #endregion -->

```python tags=["hide-output"]
# convert string in int format to int >> ok!
print(int('1234'))
```

```python tags=["hide-output"]
str1 = '123.456'
print(str1)
print( type(str1) )
```

```python tags=["hide-output"]
# convert string in float format to float >> ok!
print( float(str1)+1000 )
```

```python tags=["hide-output"]
# convert string in float format to float >> ok!
f = float('987.654')
print(f)
print( type(f) )
```

```python tags=["hide-output"]
print( f+1000 )
```

```python tags=["raises-exception", "hide-output"]
# convert string in float format to int >> Value error!
print( int('123.456') )
```

```python tags=["hide-output"]
# convert "string in float format" to float,
# then convert from float to int >> ok!
value = int( float('123.456') )
print(value)
print( type(value) )
```

```python tags=["raises-exception", "hide-output"]
# covert string to int >> Value error
print(int('Hello'))
```

```python tags=["hide-output"]
# convert float to string >> ok!
s = str(f)
print(s)
type(s)
```

## Operators

- `Operator` คือสัญลักษณ์หรือเครื่องหมายที่แทนการคำนวณต่าง ๆ ทางคณิตศาสตร์
- ข้อมูลที่ `operator` ใช้ในการคำนวณเรียกว่า `operand`

**ตัวอย่าง**

```python tags=["hide-output"]
2 + 3
```

<!-- #region -->
- เครื่องหมาย + คือ operator สำหรับการบวก
- ตัวเลข 2 และ 3 คือ operand และ 5 คือผลลัพธ์



### Arithematic Operators

ตัวดำเนินการทางคณิตศาสตร์
<!-- #endregion -->

```python tags=["hide-output"]
x = 16
y = 4

print('x + y =', x + y)   # การบวก
print('x - y =', x - y)   # การลบ
print('x * y =', x * y)   # การคูณ
print('x / y =', x / y)   # การหาร (ได้ผลลัพธ์เป็น float)
```

**`%` : การหารที่ได้เศษของการหารเป็นผลลัพธ์ (modulus)**

```python tags=["hide-output"]
x = 17
y = 4
print('x % y =', x % y)
```

**`//` : การหารที่ปัดเศษของการหารทิ้ง**

```python tags=["hide-output"]
x = 17
y = 4
print('x // y =', x // y)
```

`**` : การคำนวณหาค่ายกกำลัง (exponent) **bold text**

```python tags=["hide-output"]
x = 2
y = 4
print('x ** y =', x ** y)
```

```python tags=["hide-output"]
16**0.5
```

### Comparison Operators

ตัวดำเนินการสำหรับการเปรียบเทียบ ให้ผลลัพธ์เป็นค่าความจริง (boolean) ได้แก่ **True** หรือ **False**

ผลลัพธ์ที่ได้จากการเปรียบเทียบมักถูกนำไปใช้ในการ**สร้างเงื่อนไข (condition)** ในการทำงานของโปรแกรมต่อไป

```python tags=["hide-output"]
x = 10
y = 12

print('x > y is', x > y)
```

```python tags=["hide-output"]
print('x < y is', x < y)
```

**x เท่ากับ y หรือไม่?** (สังเกตุว่าไม่ได้ใช้เครื่องหมาย **=** ในการเปรียบเทียบ)

```python tags=["hide-output"]
print('x == y is', x == y)
```

**x ไม่เท่ากับ y หรือไม่?**

```python tags=["hide-output"]
print('x != y is', x != y)
```

**x มากกว่าหรือเท่ากับ y หรือไม่?**

```python tags=["hide-output"]
print('x >= y is', x >= y)
```

**x น้อยกว่าหรือเท่ากับ y หรือไม่?**

```python tags=["hide-output"]
print('x <= y is', x <= y)
```

### Logical Operators

**ตัวดำเนินการด้านตรรกะ** ใช้ในการประเมินค่าความจริงในเงื่อนไขที่มีความซับซ้อน โดยใช้กับ**ชุดคำสั่งที่ให้ผลลัพธ์เป็น boolean** เช่น ผลลัพธ์จากการเปรียบเทียบ (comparison)

มีตัวดำเนินการพื้นฐานได้แก่ `and`, `or`, `not`

```python tags=["hide-output"]
x = True
y = False

print('x and y is', x and y)
print('x or y is', x or y)
print('not x is', not x)
```

### Assignment Operators

ตัวดำเนินการสำหรับ**การกำหนดค่า** จะใช้**เครื่องหมายเท่ากับ (`=`)** เป็นพื้นฐาน และสามารถประยุกต์ใช้ร่วมกับ**ตัวดำเนินการทางคณิตศาสตร์**อื่น ๆ ได้

เช่น `+=`, `-=`, `*=`, `/=`, `**=`

```python tags=["hide-output"]
x = 10
y = x+100
print(x,y)
```

```python tags=["hide-output"]
x = x+1
z = y/2
print(x, z)
```

```python tags=["hide-output"]
x += 10   # x = x+10
z /= 5    # z = z/5
print(x,z)
```

<!-- #region -->
## Operators Precedence

ลำดับการประมวลผลของตัวดำเนินการ เมื่อมีการนำเอาตัวดำเนินการหลายประเภทมาใช่ร่วมกันในการประมวลผล โปรแกรมจะมี**ลำดับในการประมวลผล operand คู่ก่อนหลัง จากบนลงล่าง** ดังที่แสดงในตารางต่อไปนี้


| Operators             | Description                           |
| :-------------------- | :------------------------------------ |
| `()`                 | Parentheses                           |
| `**`                    | Exponentiation (raise to the power)   |
| `+x`, `-x`, `~x`            | Unary plus, Unary minus, Bitwise NOT  |
| `*`, `/`, `//`, `%`           | Multiplication, Division, Floor division, Modulus                           |
| `+`, `-`                  | Addition, subtraction                 |
| `<<`, `>>`                | Bitwise shift operators         |
| `&`                     | Bitwise AND                     |
| `^`, `\`                 | Bitwise XOR and OR        |
| `>`, `>=`, `<`, `<=`          | Comparison operators                  |
| `==`, `!=`                | Equality operators                    |
| `=`,`+=`,`-=`,`*=`,`**=`,`/=`,`//=` | Assignment operators                  |
| `is`, `is not`            | Identity operators                    |
| `in`, `not in`            | Membership operators                  |
| `not`, `or`, `and`          | Logical operators                     |
<!-- #endregion -->

```python tags=["hide-output"]
a = 20
b = 10
c = 15
d = 5

print(a + b * c / d)
```

```python tags=["hide-output"]
print((a + b) * c / d)
```

```python tags=["hide-output"]
print(a + b * (c / d))
```

```python tags=["hide-output"]
print((a + (b * c)) / d)
```

### Example

$$
y = -3x - \frac{2}{10^2}
$$

```python tags=["hide-output"]
x = 5
y = -3*x-2/10**2
print(y)
```

<!-- #region -->
## Python `math` module

- การคำนวณทางคณิตศาสตร์ที่ซับซ้อนทำได้ยากด้วย `operator` พื้นฐาน
- Python เตรียมชุดคำสั่ง (หรือฟังก์ชัน) ในการคำนวณที่จำเป็นทางคณิตศาสตร์เพิ่มเติมให้ผู้พัฒนาโปรแกรมได้เรียกใช้งาน
- คำสั่งเหล่านี้ถูกจัดเตรียมรวมกันไว้ในโมดูล (module) ที่ชื่อว่า `math`
- ก่อนจะใช้งานคำสั่งเหล่านี้เราต้อง `import` โมดูลเข้าสู่โปรแกรมเสียก่อน
```python
import math
```

- กลุ่มของชุดคำสั่งพื้นฐานทางคณิตศาสตร์ที่ Python มีให้เรียกใช้งาน
 - Trigonometric – `sin`, `cos`, `tan`, `asin`, `acos`, …
 - Exponential and Logarithmic – `exp`, `log`, `log2`, `log10`, …
 - Power – `pow, sqrt`, …
 - Rounding – `ceil, floor`
 - Others – `abs`, …
 - ค่าคงที่ - `pi, e`
<!-- #endregion -->

```python
# import built-in math module
import math
```

```python tags=["hide-output"]
# using square root (sqrt) function in math module
print(math.sqrt(25))
print(25**0.5)
```

```python tags=["hide-output"]
# pi and e value
print(math.pi, math.e)
# area of circle with radius of 10
print(math.pi * 10**2)
```

```python tags=["hide-output"]
# 2 radians = 114.59 degrees
print(math.degrees(2))
```

```python tags=["hide-output"]
# 60 degrees = 1.04 radians
print(math.radians(60))
```

```python tags=["hide-output"]
# Sine of 2 radians
print(math.sin(2))
```

```python tags=["hide-output"]
# Cosine of 0.5 radians
print(math.cos(0.5))
```

```python tags=["hide-output"]
# Sine of 30 radians
print(math.sin(30))

# Sine of 30 degree
# แปลง degree ให้เป็น radians
# 360 degree = 2*Pi radians
# 1   degree = 2*Pi/360 = Pi/180
# 30  degree = 30*(Pi/180)
print(math.sin(30*math.pi/180))

# หรือแปลงโดยใช้คำสั่งต่อไปนี้
rad = math.radians(30)
print(math.sin(rad))

# แปลง radians ให้เป็น degree โดยใช้คำสั่งต่อไปนี้
print(math.degrees(rad))
```

```python tags=["hide-output"]
# 4! = 1 * 2 * 3 * 4 = 24
print(math.factorial(4))
```

```python tags=["hide-output"]
# ceil
print(math.ceil(5.23))
# floor
print(math.floor(5.99))
```

<!-- #region -->
## `input()` function

- ใช้คำสั่ง input() สำหรับการรับค่าข้อมูลจากผู้ใช้ผ่านคีย์บอร์ด เช่น
```python
a = input()
```

- ข้อมูลที่ผู้ใช้ผ่านจะถูกเก็บไว้ในตัวแปร `a`
- โดยปกติข้อมูลที่ได้จากคำสั่ง `input()` จะมีชนิดเป็น**ข้อความ (string)**

- หากต้องการให้ข้อมูลที่ได้ถูกจัดเก็บในรูปแบบตัวเลข (number) จะต้อง**แปลงชนิดข้อมูล**ตามความเหมาะสม เช่น
```python
a = int(input())     # แปลงข้อมูลที่รับมาแบบข้อความ เป็น int
a = float(input())   # แปลงข้อมูลที่รับมาแบบข้อความ เป็น float
```
<!-- #endregion -->

```python tags=["raises-exception", "remove-output"]
import math

# รับ input แล้วแปลงจาก string เป็น float ด้วยคำสั่งภายในบรรทัดเดียว
r = float( input() )
print(math.pi*r*r)
```

<!-- #region -->
- หากต้องการให้มีการ**แสดงข้อความอธิบายผู้ใช้งานโปรแกรม**ในขณะรับ input สามารถทำได้ดังนี้คือ
```python
name = input('Please enter your name:')
print('My name is',name)
```

- เมื่อโปรแกรมทำงาน จะแสดงผลการทำงานดังต่อไปนี้
```
Please enter your name: John Doe
My name is John Doe
```

- หากต้องการรับข้อมูลพร้อมกันหลายๆ ตัว เราสามารถใช้คำสั่ง `input().split()` ช่วยได้
```python
fname, lname = input('Enter your name:').split()
```

- `.split()` จะตัดข้อความที่อ่านได้จากคำสั่ง `input()` ออกเป็นหลาย ๆ ส่วน โดยดูจากช่องว่าง (space) ระหว่างข้อความ

- ข้อความที่ถูกตัดแบ่งเป็นหลาย ๆ ส่วน แล้วจะถูกมากระจายเก็บในตัวแปรรอรับค่า (`fname`, `lname`)


- เมื่อโปรแกรมทำงาน โปรแกรมจะรอรับข้อมูลจากผู้ใช้
```console
Enter your name: John Doe
```

- หากผู้ใช้ป้อนข้อมูลเป็น  “John Doe” ข้อมูลจะถูกแบ่งออกเป็น 2 ส่วน
 - “John” จะถูกเก็บไว้ในตัวแปร `fname`
 - “Doe” จะถูกเก็บไว้ในตัวแปร `lname`
<!-- #endregion -->

```python tags=["raises-exception", "remove-output"]
fname, lname = input().split()
print('My firstname is ' + fname +' and ' + lname + ' is my last name.')
```

- แต่ถ้าใช้  `name = input('Enter your name:')` โดยไม่มี `split()` ต่อท้าย
 - “John Doe” ทั้งหมดจะถูกเก็บไว้ในตัวแปร `name`

```python tags=["raises-exception", "remove-output"]
name = input()
print('My name is ' + name)
```

<!-- #region -->
### ข้อควรระวังในการใช้ `input().split()`


เมื่อใช้ `input().split()` **ต้องมีจำนวนตัวแปรที่จะมารับค่าผลลัพธ์ของ `.split()` ให้พอดีกับข้อมูลที่ถูกแบ่งส่วนแล้ว** มิฉะนั้นจะเกิด error ได้

```{code-block} python

x,y,z = input().split()
x = float(x)
y = float(y)
z = float(z)
result = 2*x**2 + 3*y - 10*z
print()
```



## Formatting output using *f-string*

**`f-string`** คือการใช้ `f` นำหน้าข้อความเพื่อกำหนดรูปแบบพิเศษในข้อความนั้น และใช้เครื่องหมาย **`{}`** ในการ**กำหนดตำแหน่งและรูปแบบของข้อมูล**ที่จะแทรกลองไปในข้อความ ดังเช่นตัวอย่างต่อไปนี้
<!-- #endregion -->

```python tags=["hide-output"]
num1 = 83
num2 = 9
result = f"The product of {num1} and {num2} is {num1 * num2}."
print(result)
```

`f-string` สามารถนำไปใช้กำหนดรูปแบบพิเศษในข้อความที่จะแสดงออกด้วยคำสั่ง `print` เช่น

```python tags=["hide-output"]
city = 'Chiang Mai'
temp = 36.1
print(f'Temperature in {city} is {temp} degree Celsius.')
print('Temperature in ' + city + ' is ' + str(temp) + ' degree Celsius.')
```

`f-string` สามารถใช้กำหนดรูปแบบพิเศษ เช่น จำนวนตำแหน่งทศนิยม หรือขนาดความกว้างของช่องการแสดงผลของข้อมูลที่ระบุใน `{}` ได้ เช่น

```python tags=["hide-output"]
a = 3
print(f'We have {a:5} dogs.')
```

ความหมาย:
- **`{a:5}`** แสดงค่า `a` : ขนาด 5 ช่อง (ถ้าเป็นข้อมูล**ตัวเลขจะชิดขวา**)

```python tags=["hide-output"]
a = 'CMU'
print(f'I love {a:5}.')
```

ความหมาย:
- **`{a:5}`** แสดงค่า `a` : ขนาด 5 ช่อง (ถ้าเป็นข้อมูล**ข้อความจะชิดซ้าย**)

```python tags=["hide-output"]
a = 'Chiang Mai'
b = 36.12345
print(f'Temp in {a} is {b:.2f} degree Celsius.')
```

<!-- #region -->
ความหมาย:
- **`{b:8.2f}`** แสดงค่า `b` : ขนาด 8 ช่องชิดขวา **`.2f`** = แสดงทศนิยม 2 ตำแหน่ง


## Summary

- **ตัวแปร (variable)** ถูกนำมาใช้ในการช่วยจดจำข้อมูลเพื่อใช้งานในภายหลัง ต้องอาศัยการจองพื้นที่ในหน่วยความจำ และมีการอ้างอิงโดยใช้ชื่อ
- **ชนิดของตัวแปร** คือชนิดของข้อมูลที่จะถูกจัดเก็บไว้ในตัวแปร ได้แก่
 - ข้อความ (String)
 - เลขจำนวนเต็ม (Numerical Integer)
 - เลขทศนิยม (Floating-point)
 - ค่าทางตรรกะ (Boolean)
- การตั้งชื่อตัวแปร ต้องไม่ซ้ำกับคำสำคัญ (Keywords) ที่ได้มีการกำหนดไว้
- ชื่อตัวแปรใน Python นั้นเป็นแบบ case sensitive เช่น var และ Var ถือเป็นคนละตัวกัน
- **ตัวดำเนินการ (operators)** คือเครื่องหมายที่ถูกใช้เพื่อสั่งให้โปรแกรมประมวลผล มีหลายชนิด ได้แก่
 - กำหนดค่า (Assignment)
 - คำนวณทางเลขคณิต (Arithmetic)
 - ความสัมพันธ์ และเปรียบเทียบ (Relational and Comparison)
 - การคำนวณทางตรรกะ (Logical)
- เมื่อภายในคำสั่งประกอบไปด้วย operator มากกว่า 1 ตัว **ลำดับการประมวลผล (precedence)** ก่อนหลังจะเป็นไปตามที่ได้มีการกำหนดไว้
- การคำนวณทางคณิตศาสตร์ที่ซับซ้อนมากขึ้นสามารถกระทำได้โดยอาศัยชุดคำสั่ง (หรือฟังก์ชัน) ที่ Python ได้เตรียมไว้ให้เรียกใช้
 - ต้อง `import math` โมดูลจึงจะเรียกใช้งานคำสั่งทางคณิตศาสตร์เหล่านั้นได้
- การรับอินพุตจากผู้ใช้สามารถใช้ ฟังก์ชัน `input()`
- ใช้ `input().split()` ในการตัดแบ่ง String ที่รับเข้ามาเพื่อแยกเป็นข้อมูลหลายตัวได้
- Python f-string สามารถใช้สำหรับการกำหนดรูปแบบพิเศษให้กับข้อความได้
- การแสดงผลออกจอภาพสามารถใช้ฟังก์ชัน `print()` ร่วมกับ f-string เพื่อกำหนดรูปแบบการแสดงผลที่เหมาะสมได้
<!-- #endregion -->
