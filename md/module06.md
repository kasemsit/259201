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

<!-- #region id="LVWjo8GPhlGg" -->
# Iterations and Collections


```{admonition} Topics
- ทบทวนเรื่อง Collections
- การใช้ While-loop กับ Collections
- การใช้ For-loop กับ Collections
```


## Review of Python Collections




## List

การใช้ตัวแปรจำนวนมาก อาจไม่เหมาะกับการทำงานกับข้อมูลจำนวนมาก เช่น
- ชื่อของนักศึกษาหลายคน อาจใช้ตัวแปร `name1, name2, name3, …`
- คะแนนของนักศึกษาในห้อง อาจใช้ตัวแปร `score1, score2, score3, …`

ลิสต์ (List) คือการเก็บชุดข้อมูลที่เกี่ยวข้องกันจำนวนหลาย ๆ ตัวให้อยู่ภายใต้ตัวแปรเดียวกัน

<img src='https://drive.google.com/uc?id=1YnpVQlEPDf1Zh5L5xHw9uvBee8sL-BSu' width='550'>

- พื้นที่เก็บข้อมูลแต่ละช่อง คือพื้นที่สำหรับจัดเก็บข้อมูลแต่ละตัว (Element)
- พื้นที่เก็บข้อมูลแต่ละ item จะอ้างอิงด้วย ชื่อลิสต์และหมายเลขระบุตำแหน่ง (Index)
 - `data[index]`
 - `index` มีค่าเริ่มต้นเป็น `0` เสมอ : ระบุถึงพื้นที่ตำแหน่งแรก (หรือช่องแรก)
 - `index` มีค่ามากที่สุดคือ `n-1` : ใช้ระบุพื้นที่ตำแหน่งสุดท้าย เมื่อ `n` จำนวนพื้นที่ทั้งหมดของลิสต์

ลิสต์ใน Python เทียบเคียงได้กับ **array** ในภาษาคอมพิวเตอร์อื่น ๆ



### การเพิ่มข้อมูลลงในลิสต์

ตัวแปร List มีความสามารถ/คำสั่งติดตัว ที่ช่วยในการเพิ่มข้อมูลใหม่ให้กับ List คือ
- `.append()` เพิ่มข้อมูล**ต่อท้าย** List
- `.insert()` **แทรกข้อมูล**ในตำแหน่ง `index` ที่ต้องการ

นอกจากนี้ยังมี `operator` ที่ช่วยในการเพิ่มข้อมูลต่อท้าย List ได้แก่
- `+` ใช้**เชื่อมต่อ** List เข้าด้วยกัน (concatenation)
- `*` ใช้เพิ่มข้อมูลให้มีหลายชุดตาม**จำนวน**ที่ต้องการ
<!-- #endregion -->

```python id="pCBLqnerkvIC"
a = [16.5, 2.0, 77.5, 40.0, 0.5, 11.15, 0.0, 1.0, 1.0, 1.0, 112071.5]
print( f'len(a): {len(a)}' )
print( f'1st item: {a[4]}, last item = {a[len(a)-1]}')
print( f'a[1]+a[2]+a[3]: {a[1]+a[2]+a[3]}')

print()
a.append(999)
print(f'After append(999):\n{a}')
a.insert(0,888)
print(f'After insert(0,888):\n{a}')
```

### การลบข้อมูลจากลิสต์

ตัวแปร List มีคำสั่งติดตัวที่ใช้ในการลบข้อมูล คือ
- `.remove()` ลบข้อมูลที่มีค่าตามที่ระบุจาก List
- `.pop()` ลบข้อมูลในตำแหน่ง `index` ที่ระบุออกจาก List
- `.clear()` ลบข้อมูลทั้งหมดจาก List

```python id="LDeke4FT2TFq"
a = [16.5, 2.0, 77.5, 40.0, 0.5, 11.15, 0.0, 1.0, 1.0, 1.0, 112071.5]
print(a)
a.remove(1.0)
print(f'After remove(1.0):\n{a}')

a.pop()
print(f'After pop():\n{a}')
a.pop(0)
print(f'After pop(0):\n{a}')

a.clear()
print(f'After clear():\n{a}')
```

## Tuple

- มีการเก็บข้อมูลในลักษณะเดียวกันกับลิสต์ แต่**ไม่สามารถเปลี่ยนแปลงค่าในภายหลังได้** (immutable)
- ใช้เครื่องหมายวงเล็บ `(...)` ในการสร้างลิสต์ โดยการระบุรายการชุดข้อมูลไว้ภายใน แล้วขั้นข้อมูลแต่ละตัวด้วย `,`
- การอ้างอิงข้อมูลแต่ละ item จะใช้ค่า `index` ซึ่งเป็นค่า int เหมือนกันกับลิสต์

```python id="ZshPbnm33mjM"
b = (100,200,300,400,500,2.5,3.5,4.5,'hello')
print( f'b[2]+b[3]+b[4] = {b[2]+b[3]+b[4]}')
```

```python id="PNqyvtsG5NPv"
print( b[len(b)-1] )
# b[len(b)-1] = 5.5                  # assignment error
```

### Slice operation

การเข้าถึง**ช่วงของข้อมูล**ใน List และ Tuple ด้วยการ slice โดยการกำหนดค่า `index` ในรูปแบบ **`ตัวแปรลิสต์[start:stop:step]`**
- `start` คือ ค่า index ที่เป็น**จุดเริ่มต้น**
- `stop` คือ ค่า index ที่เป็น**จุดสิ้นสุด** (แต่ไม่รวม item นี้)
- `step` คือ **การเพิ่มค่า** index ทีละ +step

ผลลัพธ์จากการ slice คือ **ลิสต์ของข้อมูล**

```python id="3_KRlvo06TTR"
a = [100,200,300,400,500,2.5,3.5,4.5,5.5]
b = (100,200,300,400,500,2.5,3.5,4.5,5.5)

print( f'a[0:5] = {a[0:5]}')          # start=0, stop=5, step=1 >> [0,1,2,3,4]
print( f'a[4:] = {a[4:]}')            # start=4, stop=last, step=1 >> [4,5,6,7,8]
print( f'b[:6] = {b[:6]}')            # start=0, stop=6, step=1 >> [0,1,2,3,4,5]
print( f'b[1:7:2] = {b[1:7:2]}')      # start=1, stop=7, step=2 >> [1,3,5]

print( f'sum(a[4:]) = {sum( a[4:] )}')        # start=4, stop=last, step=1 >> [4,5,6,7,8]
print( f'sum(b[1:7:2]) = {sum( b[1:7:2] )}')  # start=1, stop=7, step=2 >> [1,3,5]
```

### การแปลงค่าระหว่าง Tuple และ List

หากต้องการแปลงค่าระหว่าง Tuple และ List สามารถทำได้ด้วยคำสั่ง
- `list(ตัวแปร tuple)` ได้ผลลัพธ์เป็น List
- `tuple(ตัวแปร list)` ได้ผลลัพธ์เป็น Tuple

```python id="tMVVYUlY5k5v"
b = (100,200,300,400,500,2.5,3.5,4.5,5.5)
print(f'tuple b:\n{b}')

b = list(b)
print(f'list b:\n{b}')

b = b+b[0:5]
b = tuple(b)
print(f'tuple b:\n{b}')
```

<!-- #region -->
## Set

- ใช้จัดเก็บชุดข้อมูลที่จะนำมาประมวลผลแบบเซ็ตในทางคณิตศาสตร์
- ใช้เครื่องหมาย `{...}` ในการสร้างเซ็ต โดยการระบุรายการชุดข้อมูลไว้ภายใน แล้วขั้นข้อมูลแต่ละตัวด้วย `,`
- **ไม่สามารถเก็บข้อมูลซ้ำกันได้** (unique)
- ไม่รองรับการอ้างอิงข้อมูลด้วยค่า `index` เนื่องจากการเก็บข้อมูลไม่มีลำดับ (unordered)
- รองรับตัวดำเนินการแบบ `Union`, `intersection`, `-`



### การเพิ่มข้อมูลและลบข้อมูลใน Set

ตัวแปร Set มีคำสั่งติดตัวที่ใช้ในการจัดการข้อมูล คือ
- `.add()`
- `.update()`
- `.remove()`
- `.discard()`
- `.clear()`
<!-- #endregion -->

```python id="1XzitggR-vmA"
c = {1,2,2,3,3,5,8}
print(c)

# เพิ่มข้อมูลทีละตัว
c.add(4)
print(f'After .add(10):\n{c}')

# เพิ่มข้อมูลจาก set อื่น
c.update({100,200,300})
print(f'After .update(100,200,300):\n{c}')

# discard ค่าที่ไม่มีใน Set ไม่ทำให้เกิด error
c.discard(1000)
c.discard(100)
print(f'After .discard(100):\n{c}')

c.clear()
print(f'After .clear():\n{c}')
```

## Dictionary

- เก็บข้อมูลเป็น item คล้ายกับลิสต์ แต่ใช้ค่า **key** ซึ่งไม่จำเป็นต้องมีค่าแบบ `int` ในการอ้างอิงข้อมูล
- ค่า **key** สำหรับการอ้างอิง สามารถเป็นข้อมูลแบบ `int`, `float`, `string`, `tuple` ก็ได้
- ค่า **key** เมื่อกำหนดไปแล้ว **จะไม่สามารถเปลี่ยนแปลงได้**

```python id="Cd4htT48hiqu"
p = {"name":"Harry Potter", "isMale": True, "midterm":25, "final":30}
print( f'Name = {p["name"]}' )
print( f'Score = {p["midterm"] + p["final"]}')

p['name'] = 'Rionel Messi'
print(p)
```

<!-- #region id="BrG5zUZPkPZD" -->
### การเพิ่มข้อมูลให้กับ Dict
เราสามารถเพิ่มข้อมูล item ใหม่ใน Dict ได้ด้วยการกำหนดค่าให้กับ `key` ที่ไม่เคยมีมาก่อนใน Dict
<!-- #endregion -->

```python id="-U7CNX3O8vzS"
p["weight"] = 65.25
p["height"] = 180.0
print(p)
```

### การลบข้อมูลจาก Dict

ตัวแปร Dict มีคำสั่งติดตัวสำหรับการลบข้อมูล เช่น
- `.pop()` ลบข้อมูลด้วยค่า `key` ที่ระบุ
- `.popitem()` ลบข้อมูลรายการสุดท้ายใน Dict
- `.clear()`ลบข้อมูลทั้งหมดใน Dict

```python id="M5jHA_e08o0F"
p = {'name': 'Rionel Messi', 'isMale': True, 'midterm': 25, 'final': 30, 'weight': 65.25, 'height': 180.0}
print(p)

weight = p.pop('weight')       # remove 'weight" key-value pair
print(p)

height = p.popitem()
print(p)

p.clear()
print(p)
```

### การดูรายการ key ทั้งหมดใน Dict

สามารถใช้คำสั่ง `.keys()` ในการแสดงรายการ `key` ทั้งหมดได้

```python id="hjp4wVYM9-QJ"
p = {'name': 'Rionel Messi', 'isMale': True, 'midterm': 25, 'final': 30, 'weight': 65.25, 'height': 180.0}
print(p)

keys = p.keys()
print( list(keys) )
```

### การดูรายการข้อมูลทั้งหมดใน Dict

สามารถใช้คำสั่ง `.items()` ในการแสดงรายการข้อมูลทั้งหมดใน Dict ได้

สังเกตุได้ว่าผลลัพธ์ที่ได้จะอยู่ในรูปแบบ **`List ของ Tuple จำนวนมาก`**

```
[(key1, value1),(key2, value2),(key3, value3),...,(keyN,valueN)]
```

```python id="FEFZ4hj6-BNW"
p = {'name': 'Rionel Messi', 'isMale': True, 'midterm': 25, 'final': 30, 'weight': 65.25, 'height': 180.0}
print(p)

items = p.items()
print( list(items) )
```

## การใช้ Iteration กับ Collections

ในกรณีที่มีข้อมูลจัดเก็บอยู่ใน collection เป็นจำนวนมาก การเข้าถึงข้อมูลแต่ละตัวด้วยการระบุ **index** ของแต่ละ **item** ภายใน collection เองถือเป็นเรื่องที่ไม่สะดวกนัก เช่น

```python id="PZqBW6X1-T42"
d = [10,30,40,15,50,60,5,10,35,50]
print(f'{d[0]} {d[1]} {d[2]} {d[3]} {d[4]} {d[5]} {d[6]} {d[7]} {d[8]} {d[9]}')
```

<!-- #region -->
เราสามารถนำเอา iteration/loop มาใช้ในการประมวลผลเพื่อช่วยให้การเข้าถึงข้อมูลภายใน collection ทำได้สะดวกขึ้นได้


## การใช้ loop เพื่อสร้างตัวเลข index เพื่อเข้าถึงข้อมูลใน collection

เราสามารถใช้ **While-loop** เพื่อสร้างตัวเลขที่ใช้เป็น **index** สำหรับ collection แทนได้ เช่น
<!-- #endregion -->

```python id="SumWJXp3HouK"
# from left-to-right
d = [10,30,40,15,50,60,5,10,35,50]
i = 0                     # index=0

while i<len(d):           # index<10 : [0,1,2,3,4,5,6,7,8,9]
  print(d[i],end=" ")     # d[i] คือ ข้อมูลแต่ละตัวที่เก็บภายใน collection
  i+=1
```

```python id="IqaJBWH4IQOT"
# from right-to-left
d = [10,30,40,15,50,60,5,10,35,50]
i = len(d)-1              # index=9

while i>=0:               # index>=0 : [9,8,7,6,5,4,3,2,1,0]
  print(d[i],end=" ")
  i-=1
```

<!-- #region id="jrG6AB1ZI831" -->
ในทำนองเดียวกัน เราสามารถใช้ **For-loop** และคำสั่ง **`range()`** เพื่อสร้างตัวเลขที่ใช้เป็น **index** ได้เช่นกัน
<!-- #endregion -->

```python id="8TnIMQ5GJO1_"
# from left-to-right
d = [10,30,40,15,50,60,5,10,35,50]

for i in range(len(d)):     # range(10) : [0,1,2,3,4,5,6,7,8,9]
  print(d[i],end=" ")       # d[i] คือ ข้อมูลแต่ละตัวที่เก็บภายใน collection
```

```python id="uPjWGk4ZJi-h"
# from right-to-left
d = [10,30,40,15,50,60,5,10,35,50]

for i in range(len(d)-1,-1,-1): # range(9,-1,-1) : [9,8,7,6,5,4,3,2,1,0]
  print(d[i],end=" ")
```

เราสามารถประยุกต์ใช้ Condition ร่วมกับ loop ได้ เช่น

```python id="jQsD-bteK000"
# หาผลรวมข้อมูลที่มากกว่า 25
d = [10,30,40,15,50,60,5,10,35,50]
i = 0                   # index=0
sm = 0                  # sum=0

while i<len(d):         # index<10 : [0,1,2,3,4,5,6,7,8,9]
  if d[i] > 25:
    sm+=d[i]            # ผลรวมสะสมของข้อมูลที่ > 25
    print(d[i],end=" ")
  i+=1

print(f'\nsum(>25): {sm}')
```

<!-- #region id="xlF1d8PfL10J" -->
หรือ หากใช้ For-loop กับ Condition ดังตัวอย่างต่อไปนี้
<!-- #endregion -->

```python id="YUwEJpTgL-cO"
d = [10,30,40,15,50,60,5,10,35,50]
sm = 0
for i in range(len(d)): # range(10) : [0,1,2,3,4,5,6,7,8,9]
  if d[i] > 25:
    print(d[i],end=" ")
    sm += d[i]          # ผลรวมสะสมของข้อมูลที่ > 25

print(f'\nsum(>25): {sm}')
```

<!-- #region id="W7Cm4OaXKf0d" -->
---

## การใช้ For-loop เพื่อเข้าถึงข้อมูลใน collection โดยตรง

นอกจากการใช้ loop สร้างค่า index สำหรับเข้าถึงข้อมูลใน collection คล้ายกับที่มีในภาษาคอมพิวเตอร์อื่น ๆ แล้ว ภาษา **Python** ยังมีรูปแบบการใช้งาน For-loop อีกรูปแบบหนึ่งที่**สามารถเข้าถึงข้อมูลโดยไม่จำเป็นต้องสร้างค่า index ก่อน** โดยมีรูปแบบการใช้งานดังตัวอย่างต่อไปนี้

### For-loop และ List

```python
collection_variable = [1,2,3,4,5,...]

for x in collection_variable:
  print(x)

```
ตัวแปร **x** ในแต่ละรอบการทำงานคือ ***item*** หรือข้อมูลแต่ละรายการที่เก็บอยู่ใน collection (เรียงลำดับจากห้องที่มีค่า **index=0,1,2,...**)
<!-- #endregion -->

```python id="ZtMn7UdvJ80q"
d = [10,30,40,15,50,60,5,10,35,50]

for x in d:
  print(x, end=" ")   # x คือ ข้อมูลแต่ละตัวที่เก็บภายใน collection
```

<!-- #region id="UbunefYiPGMx" -->
เมื่อเปรียบเทียบกับ For-loop แบบเดิมที่ใช้คำสั่ง **`range()`** สร้างค่า **index** ดังตัวอย่างก่อนหน้านี้

```python
d = [10,30,40,15,50,60,5,10,35,50]

for i in range(len(d)): # range(10) : [0,1,2,3,4,5,6,7,8,9]
  print(d[i],end=" ")   # d[i] คือ ข้อมูลแต่ละตัวที่เก็บภายใน collection

```

ที่ตัวแปร **`i`** จะเก็บค่าตัวเลขที่ใช้เป็น index ดังนั้นถ้าต้องการ ตัว**ข้อมูล**จะต้องอ้างอิงด้วย **`d[i]`** อีกครั้ง
<!-- #endregion -->

<!-- #region id="TyUMKxSvUZdC" -->
---
### **การใช้ Enumerate**

ในบางกรณีที่ยังต้องการค่า **index** ของข้อมูลแต่ละตัว เพื่อประกอบการแสดงผล ก็ยังสามารถทำได้โดยใช้คำสั่ง **`enumerate()`** ดังตัวอย่างต่อไปนี้
<!-- #endregion -->

```python id="W0iRiLIJPFhw"
d = [10,30,40,15,50,60,5,10,35,50]

for i,x in enumerate(d):      # d=[10,30,40,15,50,60,5,10,35,50]
  print(f'{i+1}.{x}')         # i คือ ค่า index ของข้อมูลแต่ละตัว = 0,1,2,...
                              # x คือ ข้อมูลแต่ละตัวที่เก็บภายใน collection
```

<!-- #region id="oYISIrz1VBBp" -->
คำสั่ง **`enumerate()`** จะสร้างรายการ Tuple ของ `(index, value)` สำหรับข้อมูลแต่ละ item ภายใน collection ดังที่แสดงในโค้ดด้านล่าง
<!-- #endregion -->

```python id="f3wsEVXoU3vH"
list(enumerate(d))
```

<!-- #region id="SUZ5Ly4kQpbP" -->
---
### **การใช้ For-loop กับ Tuple**
<!-- #endregion -->

```python id="ZYdcTcu3QMZl"
names = ('Lisa','Jisoo','Rose','Jennie')
for name in names:
  print(name)
```

```python id="N-_zwfzmVu5U"
names = ('Lisa','Jisoo','Rose','Jennie')
for i,name in enumerate(names):
  print(f'{i+1}.{name}')
```

<!-- #region id="MRzl7skGSoyE" -->
---
### **การใช้ For-loop กับ Set**
<!-- #endregion -->

```python id="4JdmKs-CRRBJ"
teams = {'Manchester United','Barcelona','Juventus','PSG','Barcelona','Liverpool'}
for team in teams:
  print(team)
```

```python id="P77G-dpmWCGT"
teams = {'Manchester United','Barcelona','Juventus','PSG','Barcelona','Liverpool'}
for i,team in enumerate(teams):
  print(f'{i+1}.{team}')
```

<!-- #region id="m607013VSrJk" -->
---
### **การใช้ For-loop กับ Dictionary**
<!-- #endregion -->

```python id="3te9MGecSZWH"
person = {'name': 'Rionel Messi', 'isMale': True, 'midterm': 25, 'final': 30, 'weight': 65.25, 'height': 180.0}
print(person)
```

```python id="kIPKB8sbRfpy"
for k in person:
  print(k)          # k คือชื่อของ key
```

```python id="Y54eNhfNS_Uy"
for k in person:
  print(person[k])  # p[k] คือค่า value ของ key แต่ละตัว
```

```python id="MTR--OScWsHe"
for k in person:
  print(f'{k}: {person[k]}')
```

```python id="GRRy9YhdTTft"
for i,k in enumerate(person):
  print(f'{i+1}.{k}: {person[k]}')
```

<!-- #region id="JSQAqAGDX6M2" -->
---
### **การใช้ For-loop กับ Collection หลายมิติ**

**List of Dict**
<!-- #endregion -->

```python id="jXimlqfYWhmh"
# List of Dict
students = [
    {"name":"John","gender":"male","height":180.5,"weight":80},
    {"name":"Jane","gender":"female","height":176,"weight":60.5},
    {"name":"Steve","gender":"male","height":177.5,"weight":82}
]
```

```python id="Q3SLAtWSdzQi"
max_height = 0                    # ตัวแปรเก็บความสูงที่มากที่สุด
tallest_student = ''              # ตัวแปรเก็บชื่อคนที่สูงที่สุด

for s in students:
  print(f"{s['name']} is {s['height']} cm tall.")

  if s['height'] > max_height:    # ถ้าความสูงของนร.คนนี้ สูงกว่า ค่าความสูงที่สุด
    max_height = s['height']      # ค่าความสูงที่สุด คือ ความสูงของนร.คนนี้
    tallest_student = s['name']   # เก็บชื่อของนร.คนนี้

print(f'The tallest person in the group is "{tallest_student}".')
```

<!-- #region id="AOOifCDry1yI" -->
คำนวณหาค่า **BMI** ของ นร. แต่ละคน
https://www.khonkaenram.com/th/services/health-information/health-articles/med/program-bmi

BMI = น้ำหนักตัว(kg.) / (ส่วนสูง(m.))^2
<!-- #endregion -->

```python id="glxJw82eyfEd"
# Calculate BMI: Body Mass Index
for s in students:
  s['bmi'] = round( s['weight']/(s['height']/100)**2 ,2)

for s in students:
  print(s)
```

<!-- #region id="Y9yvS7AabmHQ" -->
**Dict of List**
<!-- #endregion -->

```python id="rwZ_Bz9YaL4d"
# Dict of List
persons = {
    "John":  ["male",180.5,80],
    "Jane":  ["female",176,60.5],
    "Steve": ["male",187.5,82]
}
```

```python id="XNAc8GU_ctlE"
max_weight = 0                # ตัวแปรเก็บนน.มากที่สุด
heaviest_student = ''         # ตัวแปรเก็บชื่อคนที่นน.มากที่สุด

for name in persons:
  weight = persons[name][2]   # ดึงค่านน.ของนร.คนนี้ มาเก็บในตัวแปร weight
  print(f'{name} is {weight} kilogram.')

  if weight > max_weight:     # ถ้านน.ของนร.คนนี้ สูงกว่า ค่าความสูงที่สุด
    max_weight = weight       # ค่านน.มากที่สุด คือ นน.ของนร.คนนี้
    heaviest_student = name   # เก็บชื่อของนร.คนนี้

print(f'The heaviest person in the group is "{heaviest_student}".')
```

```python id="P0_o9ajYd9G9"

```
