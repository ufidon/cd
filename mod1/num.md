__Number System__

[Decimal numeral system](https://en.wikipedia.org/wiki/Decimal)
---
- contains symbols: `0,1,2,3,4,5,6,7,8,9` and `.`
- $\displaystyle a_{m}a_{m-1}\cdots a_{0}.b_{1}b_{2}\cdots b_{n} = \sum_{i=0}^m a_i10^i + \sum_{j=1}^nb_j10^{-j}$
- `10` is the `base` or `radix`
- the digit at different position relative to the `decimal point` has different weight
  - so it is called a _positional numeral system_


💡 Demo
---
- Expand $520.1314$
  - $520.1314 = 5×10^2 + 2×10^1 + 0×10^0+1×10^{-1} + 3×10^{-2}+1×10^{-3}+4×10^{-4}$


📝 Practice
---
- Expand the following numbers
- `643282.2324, 43.21, 876.45679`


General numeral system with base $b$
---
- $b$ is an integer larger than 1
- contains b different symbols for digits
  - and 1 symbol for the decimal point
- popular numeral systems and their digit symbols
  - binary: `0,1`
  - octal: `0,1,2,3,4,5,6,7`
  - decimal: `0,1,2,3,4,5,6,7,8,9`
  - hexadecimal: `0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f`


The first 20 numbers
---
| decimal | binary | octal | hex |
| --- | --- | --- | --- |
| $(0)_{10}$ | $(0)_2$ | $(0)_8$ | $(0)_{16}$ |
| $(1)_{10}$ | $(1)_2$ | $(1)_8$ | $(1)_{16}$ |
| $(2)_{10}$ | $(10)_2$ | $(2)_8$ | $(2)_{16}$ |
| $(3)_{10}$ | $(11)_2$ | $(3)_8$ | $(3)_{16}$ |
| $(4)_{10}$ | $(100)_2$ | $(4)_8$ | $(4)_{16}$ |
| $(5)_{10}$ | $(101)_2$ | $(5)_8$ | $(5)_{16}$ |
| $(6)_{10}$ | $(110)_2$ | $(6)_8$ | $(6)_{16}$ |
| $(7)_{10}$ | $(111)_2$ | $(7)_8$ | $(7)_{16}$ |
| $(8)_{10}$ | $(1000)_2$ | $(10)_8$ | $(8)_{16}$ |
| $(9)_{10}$ | $(1001)_2$ | $(11)_8$ | $(9)_{16}$ |
| $(10)_{10}$ | $(1010)_2$ | $(12)_8$ | $(a)_{16}$ |
| $(11)_{10}$ | $(1011)_2$ | $(13)_8$ | $(b)_{16}$ |
| $(12)_{10}$ | $(1100)_2$ | $(14)_8$ | $(c)_{16}$ |
| $(13)_{10}$ | $(1101)_2$ | $(15)_8$ | $(d)_{16}$ |
| $(14)_{10}$ | $(1110)_2$ | $(16)_8$ | $(e)_{16}$ |
| $(15)_{10}$ | $(1111)_2$ | $(17)_8$ | $(f)_{16}$ |
| $(16)_{10}$ | $(10000)_2$ | $(20)_8$ | $(10)_{16}$ |
| $(17)_{10}$ | $(10001)_2$ | $(21)_8$ | $(11)_{16}$ |
| $(18)_{10}$ | $(10010)_2$ | $(22)_8$ | $(12)_{16}$ |
| $(19)_{10}$ | $(10011)_2$ | $(23)_8$ | $(13)_{16}$ |


A general number in the numeral system with base $b$
---
- ${\displaystyle (a_{n}a_{n-1}\cdots a_{1}a_{0}.c_{1}c_{2}c_{3}\cdots c_m)_{b}=\sum _{k=0}^{n}a_{k}b^{k}+\sum _{k=1}^{m }c_{k}b^{-k}}$
- this gives us a way to convert $(N)_b$ into decimal number
  - if we represent $a_k,c_k,b$ on the RHS in decimal numbers
  - or into a numeral system with base $B$ by representing $a_k,c_k,b$ on the RHS in this numeral system


💡 Demo
---
- binary to decimal: 
  - $(1101.11)_2 = 1×2^3 + 1×2^2 + 0×2^1 + 1×2^0 + 1×2^{-1} + 1×2^{-2}$
- octal to decimal:
  - $(520.1314)_8 = 5×8^2 + 2×8^1 + 0×8^0+1×8^{-1} + 3×8^{-2}+1×8^{-3}+4×8^{-4}$
- hex to decimal:
  - $(be.ef)_{16}=11×16^1 + 14×16^0 + 14×16^{-1}+15×16^{-2}$



📝 Practice
---
- convert the following numbers to decimal
- binary: `1011101.11, 111.1, 100001.101`
- octal: `3423.12, 435.32, 7766.5544`
- hex: `fa.af, dead.beef, 5a6b.7c8d`
- reference answers

```
1011101.11->93.75
111.1->7.5
100001.101->33.625
3423.12->1811.16
435.32->285.406
7766.5544->4086.71
fa.af->250.68359375
dead.beef->57005.7458343505859375
5a6b.7c8d->23147.4865264892578125
```


☠ Challenge
---
- Which answers are inaccurate above?


Convert decimal to the system with base b
---
- Given $\displaystyle D.F = \sum _{k=0}^{n}a_{k}b^{k}+\sum _{k=1}^{m }c_{k}b^{-k} =(a_{n}a_{n-1}\cdots a_{1}a_{0}.c_{1}c_{2}c_{3}\cdots c_m)_{b}$, find $a_k$ and $c_k$
- $\displaystyle a_k = ⌊\frac{D}{b^k}⌋\mod b$
- $\displaystyle c_s =⌊ b^sF - ∑_{k=1}^{s-1}c_kb^{s-k}⌋$


Integer division
---
Given integer $a, b>0$, there exist integer $q,r$ such that
$$a=b×q+r$$
Divide $a$ by $b$, we get the *quotient* $q$ and the *remainder* r $(0≤r<b)$.

🍎 Example
---
| | |
|:---:|:---:|
| $8=2×4+0$ | $7=2×3+1$ |
| $35=8×4+3$ | $71=8×8+7$ |
| $31=16×1+15$ | $11 = 0×16+11$ |


💡 Demo
---
- `8.25` to binary
  - Integer part:
    - $8=2×4+\mathbf{0}$
    - $4=2×2+\mathbf{0}$
    - $2=2×1+\mathbf{0}$
    - $1=2×\underline{0}+\mathbf{1}$
    - collect the remainders from last to first: $(1000)_2$
  - Fraction part:
    - $.25×2 = \mathbf{0}.5$
    - $.5×2  = \mathbf{1}.\underline{0}$
    - collect the integers from first to last: $(.01)_2$
  - ans: $(1000)_2 + (.01)_2 = (1000.01)_2$
- `70.5` to octal
  - Integer part:
    - $70 = 8×8+\mathbf{6}$
    - $8  = 8×1+\mathbf{0}$
    - $1  = 8×\underline{0}+\mathbf{1}$
    - collect the remainders from last to first: $(106)_8$
  - Fraction part:
    - $.5×8=\mathbf{4}.\underline{0}$
    - collect the integers from first to last: $(.4)_8$
    - ans: $(106)_8+(.4)_8=(106.4)_8$
- `132.7` to hex
  - Integer part:
    - $132=16×8+\mathbf{4}$
    - $8  =16×\underline{0}+\mathbf{8}$
    - collect the remainders from last to first: $(84)_{16}$
  - Fraction part:
    - $0.7×16=\mathbf{11}.2$
    - $.2×16=\mathbf{3}.2$
    - $.2×16=\mathbf{3}.2$
    - $⋯$
    - collect the integers from first to last: $(.B3333⋯)_{16}$
  - ans: $(84)_{16}+(.B3333⋯)_{16}=(84.B3333⋯)_{16}=(84.B\dot{3})_{16}$


📝 Practice
---
- Convert decimal to other systems
- `93.75, 7.5, 33.625` to binary
  - ⚠️ `1.1` to binary
- `1811.16, 285.406, 4086.71` to octal
- `250.68359375, 57005.7458343505859375, 23147.4865264892578125` to hex


Convert between binary, octal and hex
---
- binary to octal: group bits into groups each of 3 bits
  - octal to binary: each octal digit converts to 3 binary digits
- binary to hex: group bits into groups each of 4 bits
  - hex to binary: each hex digit converts to 4 binary digits
- octal to hex: octal -> bin -> hex
- hex to octal: hex -> bin -> octal


💡 Demo
---
- $(11\_011. 111\_1)_2  = (\mathbf{0}11\_011. 111\_1\mathbf{00})_2 = (33.74)_8$
- $(73.12)_8=(111\_ 011. 001\_ 01\mathbf{0})_2=(111\_ 011. 001\_ 01)_2$
- $(1\_ 0110\_ 1011. 1111\_ 0000\_ 11)_{2}=(\mathbf{000}1\_ 0110\_ 1011. 1111\_ 0000\_ 11\mathbf{00})_{2}=(16B.F0C)_{16}$
- $(A6.C)_{16}=(1010\_ 0110.11\mathbf{00})_2=(1010\_ 0110. 11)_2$


📝 Practice
---
- Do the reverse of the conversions above
- Convert the octal above to hex, hex to octal


Arithmetic operations
---
- addition, subtraction, multiplication, division
- carry 1 from position $k$ to $k+1$
- borrow $b$, i.e. $(10)_b$ from position $k+1$ to $k$


📝 Practice
---
- Find the addition and multiplication tables for binary, octal and hex
- binary addition table

|  0 |  1 |
| -- | -- |
|  0 |  1 |
|  1 | 10 |

- octal addition table

|  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |
| -- | -- | -- | -- | -- | -- | -- | -- |
|  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |
|  1 |  2 |  3 |  4 |  5 |  6 |  7 | 10 |
|  2 |  3 |  4 |  5 |  6 |  7 | 10 | 11 |
|  3 |  4 |  5 |  6 |  7 | 10 | 11 | 12 |
|  4 |  5 |  6 |  7 | 10 | 11 | 12 | 13 |
|  5 |  6 |  7 | 10 | 11 | 12 | 13 | 14 |
|  6 |  7 | 10 | 11 | 12 | 13 | 14 | 15 |
|  7 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |

- hex addition table

|  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 |  a |  b |  c |  d |  e |  f |
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
|  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 |  a |  b |  c |  d |  e |  f |
|  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 |  a |  b |  c |  d |  e |  f | 10 |
|  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 |  a |  b |  c |  d |  e |  f | 10 | 11 |
|  3 |  4 |  5 |  6 |  7 |  8 |  9 |  a |  b |  c |  d |  e |  f | 10 | 11 | 12 |
|  4 |  5 |  6 |  7 |  8 |  9 |  a |  b |  c |  d |  e |  f | 10 | 11 | 12 | 13 |
|  5 |  6 |  7 |  8 |  9 |  a |  b |  c |  d |  e |  f | 10 | 11 | 12 | 13 | 14 |
|  6 |  7 |  8 |  9 |  a |  b |  c |  d |  e |  f | 10 | 11 | 12 | 13 | 14 | 15 |
|  7 |  8 |  9 |  a |  b |  c |  d |  e |  f | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|  8 |  9 |  a |  b |  c |  d |  e |  f | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
|  9 |  a |  b |  c |  d |  e |  f | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|  a |  b |  c |  d |  e |  f | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|  b |  c |  d |  e |  f | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 1a |
|  c |  d |  e |  f | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 1a | 1b |
|  d |  e |  f | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 1a | 1b | 1c |
|  e |  f | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 1a | 1b | 1c | 1d |
|  f | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 1a | 1b | 1c | 1d | 1e |

- octal multiplication table

|  1 |  2 |  3 |  4 |  5 |  6 |  7 |
| -- | -- | -- | -- | -- | -- | -- |
|  1 |  2 |  3 |  4 |  5 |  6 |  7 |
|  2 |  4 |  6 | 10 | 12 | 14 | 16 |
|  3 |  6 | 11 | 14 | 17 | 22 | 25 |
|  4 | 10 | 14 | 20 | 24 | 30 | 34 |
|  5 | 12 | 17 | 24 | 31 | 36 | 43 |
|  6 | 14 | 22 | 30 | 36 | 44 | 52 |
|  7 | 16 | 25 | 34 | 43 | 52 | 61 |

- hex multiplication table

|  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 |  a |  b |  c |  d |  e |  f |
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
|  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 |  a |  b |  c |  d |  e |  f |
|  2 |  4 |  6 |  8 |  a |  c |  e | 10 | 12 | 14 | 16 | 18 | 1a | 1c | 1e |
|  3 |  6 |  9 |  c |  f | 12 | 15 | 18 | 1b | 1e | 21 | 24 | 27 | 2a | 2d |
|  4 |  8 |  c | 10 | 14 | 18 | 1c | 20 | 24 | 28 | 2c | 30 | 34 | 38 | 3c |
|  5 |  a |  f | 14 | 19 | 1e | 23 | 28 | 2d | 32 | 37 | 3c | 41 | 46 | 4b |
|  6 |  c | 12 | 18 | 1e | 24 | 2a | 30 | 36 | 3c | 42 | 48 | 4e | 54 | 5a |
|  7 |  e | 15 | 1c | 23 | 2a | 31 | 38 | 3f | 46 | 4d | 54 | 5b | 62 | 69 |
|  8 | 10 | 18 | 20 | 28 | 30 | 38 | 40 | 48 | 50 | 58 | 60 | 68 | 70 | 78 |
|  9 | 12 | 1b | 24 | 2d | 36 | 3f | 48 | 51 | 5a | 63 | 6c | 75 | 7e | 87 |
|  a | 14 | 1e | 28 | 32 | 3c | 46 | 50 | 5a | 64 | 6e | 78 | 82 | 8c | 96 |
|  b | 16 | 21 | 2c | 37 | 42 | 4d | 58 | 63 | 6e | 79 | 84 | 8f | 9a | a5 |
|  c | 18 | 24 | 30 | 3c | 48 | 54 | 60 | 6c | 78 | 84 | 90 | 9c | a8 | b4 |
|  d | 1a | 27 | 34 | 41 | 4e | 5b | 68 | 75 | 82 | 8f | 9c | a9 | b6 | c3 |
|  e | 1c | 2a | 38 | 46 | 54 | 62 | 70 | 7e | 8c | 9a | a8 | b6 | c4 | d2 |
|  f | 1e | 2d | 3c | 4b | 5a | 69 | 78 | 87 | 96 | a5 | b4 | c3 | d2 | e1 |


💡 Demo
---
- binary arithmetic
  - 11011 + 10101
  - 10001 - 111
  - 101 × 11
  - ⚠️ 1101 ÷ 10
- octal arithmetic
  - 311 + 737
  - 715 - 476
  - 17 × 121
  - ⚠️ 756 ÷ 21
- hex arithmetic
  - 1fa + eff
  - f12 - aee
  - fa × aeb
  - ⚠️ beef ÷ ae



# References
- [Numeral system](https://en.wikipedia.org/wiki/Numeral_system)
  - [List of numeral systems](https://en.wikipedia.org/wiki/List_of_numeral_systems)
- [Computer number format](https://en.wikipedia.org/wiki/Computer_number_format)