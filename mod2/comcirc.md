# Combinational logic circuits
_lcdf5 chapter 2_

Objectives
---
- describe combinational logic circuits in
  - boolean equations
  - schematics
  - HDL (hardware description language)
- optimize combinational logic circuits with
  - Karnaugh maps


Boolean algebra
---
- the math behind combinational logic
- the domain $D$ has only two values or constants: `TRUE (T, 1); FALSE (F, 0)`
- each variable $x$ takes value of `1` or `0` at a time
- three basic operators:
  - `AND`, ∩, ∧, ⋅
    - x AND y, x∩y, x∧y, x⋅y, `xy`
    - true only when both x and y are true
  - `OR`, ∪, ∨, +
    - x∪y, x∨y, `x+y`
    - false only when both x and y are false
  - `NOT`, ¬, ‾
    - ¬x, $\overline{x}$
    - negate or flip x


Truth table of basic operations
---
| A | B | A+B | AB| $\overline{A }$ |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | `1` | 1 | 0 |

Laws of Boolean algebra 
---
| law | equation |
|:---:|:---:|
| basic | $0+A=A$ <br>$1A=A$<br> $0A=0$ <br> $1+A=1$ <br> $\overline{A}+A=1$ <br> $\overline{A}A=0$ <br> $\overline{\overline{A}}=A$|
| commutation | $AB=BA$ <br> $A+B=B+A$ |
| association | $(A+B)+C=A+(B+C)$ <br> $(AB)C=A(BC)$ |
| distribution | $A(B+C)=AB+AC$ <br>⚠️ $A+(BC)=(A+B)(A+C)$ |
| idempotence <br>identity| $A+A=A$<br> $AA=A$  |
| absorption <br> redundance | $A+AB=A$ <br> $A(A+B)=A$ <br> $A+\overline{A}B=A+B$ <br> $A(\overline{A}+B)=AB$ |
| expansion | $A=AB+A\overline{B}$ <br> $A=(A+B)(A+\overline{B})$ |
| **De Morgan** | $\overline{A_1+A_2+⋯+A_n}=\overline{A_1}⋅\overline{A_2}⋯\overline{A_n}$ <br> $\overline{A_1A_2⋯A_n}=\overline{A_1}+\overline{A_2}+⋯+\overline{A_n}$ |


💡 Prove Boolean equations with truth table
---
- basic law
- De Morgan's law


💡 Prove Boolean equations with other equations
---
- identity law
- absorption law
- expansion law


The *dual* of an algebraic expression
---
- can be obtained by
  - interchanging OR and AND operators
  - flipping 1s and 0s
- the *duality principle* of Boolean algebra
  - a Boolean equation is valid ↔ its dual equation is valid
  - the duel equation of an equation is obtained by
    - taking duals of both sides of the equation, ex.


📝 Demo
---
- Find the pairs of dual equations in the table of Boolean equations
- Simplify $F=\overline{X}YZ+\overline{X}Y\overline{Z}+XZ$
  - ans: $F=\overline{X}Y+XZ$
  - verify your simplification with truth table


📝 Practice
---
- Prove the *consensus theorem*
  - $XY+\overline{X}Z+YZ=XY+\overline{X}Z$
- by
  - Algebraic manipulation
  - Truth table
- Find the duel equation of the consensus theorem
  - prove it holds
- Prove $(A+B)(\overline{A}+C) = AC+\overline{A}B$


The complement of a function $F$
---
- $\overline{F}$ can be obtained in three ways by
  - ➊ flipping `0s` and `1s` for the values of $F$ in its truth table
  - ➋ or applying DeMorgan's law
  - ➌ or interchange AND and OR operators, complement each constant and variable
    - i.e. taking dual form
    - complementing each variable


💡 Demo
---
- Find the complement of $F=\overline{X}Y\overline{Z}+\overline{X}⋅\overline{Y}Z$ using methods ➋ and ➌


📝 Practice
---
- Find the complement of $F=X(YZ+\overline{Y}⋅\overline{Z})$ using methods ➋ and ➌


XOR and XNOR
---
- XOR: exclusive or
  - $Y=A\overline{B}+\overline{A}B=A⊕B$
  - $Y$ is true only when $A$ is different from $B$
- XNOR: exclusive nor
  - $Y=AB+\overline{A}⋅\overline{B}=\overline{A⊕B}$
  - NXOR
  - $Y$ is true only when $A$ is same as $B$


XOR equations
---
| law | equation |
|:---:|:---:|
| basic | $0⊕A=A$ <br>$1⊕A=\overline{A}$<br> $\overline{A}⊕A=1$ <br> $A⊕A=0$ |
| commutation | $A⊕B=B⊕A$ |
| association | $(A⊕B)⊕C=A⊕(B⊕C)$ |



Logic gates
---
- A computer consists of many ICs (integrated chips)
- An IC consists of many logic gates
- Basic logic gates

![gates](./img/gates.png)


Gate extension and combination
---
- gate AND, OR, NAND, NOR can be extended to have more than two inputs
- each basic gate can be implemented with several other basic gates
  - ❶An AND gate can be implemented with a NAND gated output to a NOT gate
    - $Y=\overline{\overline{AB}}$
  - ❷An OR gate can be implemented with two NOT gates output to a NAND gate
    - $Y=\overline{\overline{A}⋅\overline{B}}$
  - ❸All basic gates can be implemented with several NAND gates
- many gates are combined to implement complex logic functions


💡 Demo
---
- Draw the circuits for ❶❷❸


Describe gates in HDL
---
- structural description
  - describes 
  - referred to as netlist
- dataflow description
  - describes circuit functions using concurrent assignments
  - ⚠️ *concurrent assignments executes in parallel*
- behavioral description
  - describes circuit behavior (algorithms) in both concurrent assignments and sequential statements
- Verilog hdl has primitives for logic gates
  - while VHDL use logic operators

| gate | Verilog <br>primitives | VHDL logic<br> operators |
|:---:|:---:|:---:|
| AND | and | and |
| OR | or | or |
| NOT | not | not |
| NAND | nand | nand |
| NOR | nor | nor |
| XOR | xor | xor |
| XNOR | xnor | xnor |

- example instances for Verilog primitives
  - `and(Y, A, B);`
  - `not(Y, A);`
- example statements for VHDL logic operators
  - `Y <= A and B;`
  - `Y <= not A;`


💡 Demo
---
- Design a control circuit for majority voting of three parties
  - at least two parties vote for pass then pass
- Describe this control system in 
  - boolean function
    - $P = AB\overline{C}+A\overline{B}C+\overline{A}BC+ABC$
  - truth table
    - number of rows: $2^{N_i}$
    - $N_i$ is the number of inputs
  - circuit diagram
  - HDL description
    - Verilog HDL
    - VHDL

```verilog
// verilog HDL description
// case sensitive
module majority_voter(P, A, B, C);
  output P;
  input A,B,C;
  wire nA, nB, nC;
  wire ab, ac, bc, abc;
  wire p1,p2,p3,p4,p12,p34;

  not(nA, A);
  not(nB, B);
  not(nC, C);

  and(ab, A, B);
  and(p1, ab, nC);
  and(bc, B, C);
  and(p2, bc, nA);
  and(ac, A, C);
  and(p3, ac, nB);
  and(p4, ac, C);

  or(p12, p1, p2);
  or(p34, p3, p4);
  or(P, p12, p34);
endmodule
```

```vhdl
-- VHDL description
-- case insensitive
library IEEE, LCDF_VHDL;
use IEEE.STD_LOGIC_1164.all, LCDF_VHDL.FUNC_PRIMS.all;

entity majority_voter is
  port
  (
    P       : out std_logic;
    A, B, C : in std_logic);
end majority_voter;

architecture structural of majority_voter is
  component NOT1
    port
    (
      X  : in std_logic;
      Y  : out std_logic);
  end component;  
  component AND3
    port
    (
      X1, X2, X3 : in std_logic;
      Y          : out std_logic);
  end component; 
  component OR4
    port
    (
      X1, X2, X3, X4 : in std_logic;
      Y          : out std_logic);
  end component;

  signal nA, nB, nC, ab, ac, bc, abc : std_logic;

  begin
    n1 : NOT1 port map (A, nA);
    n2 : NOT1 port map (B, nB);
    n3 : NOT1 port map (C, nC);
    a1 : AND3 port map (A, B, nC, ab);
    a2 : AND3 port map (A, nB, C, ac);
    a3 : AND3 port map (nA, B, C, bc);
    a4 : AND3 port map (A, B, C, abc);
    o1 : OR4 port map (ab, ac, bc, abc, Y);
end structural;
```

📝 Practice
---
- Describe Boolean function $D = R\overline{T} + A$ in 
  - truth table
  - circuit diagram
  - HDL description
    - Verilog HDL
    - VHDL


Number of descriptions of a logic circuit of each method
---
- There is only one way for truth table
- There are many ways for the other three methods
  - the simplest form is desired


Boolean function standard forms
---
- facilitate the simplification procedures
- facilitate implementing logic circuits
- contain two types of terms
  - *product terms* such as $AB\overline{C}$
  - *sum terms* such as $A+B+\overline{C}$
- two types of standard forms
  - *sum of products* such as $F=AB + \overline{B} + \overline{A}B\overline{C}$
  - *product of sums* such as $F=A(\overline{B}+C)(A+B+\overline{C})$


minterms and maxterms of a function $F$
---
- a *minterm* is a product term contains all the variables of $F$
  - each variable shows up exactly once, either complemented or uncomplemented
  - there are $2^n$ minterm for $n$ variables $A_1,A_2,⋯, A_n$
    - denoted as $m_0$ to $m_{2^n-1}$
    - $m_0=\overline{A_1}⋅\overline{A_2}⋯\overline{A_n}$
    - $m_i$ is the term has the binary number equals to decimal $i$ by substituting $A_k=1$ and $\overline{A_k}=0$
    - $m_{2^n-1}=A_1A_2⋯A_n$
- *maxterms* are the complements of minterms
  - denoted as $M_0$ to $M_{2^n-1}$
  - $M_i = \overline{m_i}$


💡 Demo
---
- Find all the minterms and maxterms for
  - one variable $A$
  - two variables $A,B$
- Derive the truth table for each term


📝 Practice
---
- Find all the minterms and maxterms for three variables
- Derive the truth table for each term


💡 Sum of minterms
---
- An example
  - $F=X\overline{Y}+XY=m_2+m_3=Σm(2,3)$
- the minterms of $\overline{F}$ are those minterms NOT in $F$, i.e.
  - $\overline{F}=Σm(0,1)$
- take the complement of $\overline{F}$ to get $F$
  - $F=\overline{\overline{F}}=\overline{Σm(0,1)}=\overline{m_0+m_1}=\overline{m_0}⋅\overline{m_1}=M_0M_1=(X+Y)(X+\overline{Y})=ΠM(0,1)$
  - we get the *product of maxterms* of $F$
- draw the *two-level circuits* for $F$ in the two forms


📝 Practice
---
- Apply the demo steps on
  - $F = \overline{X}⋅\overline{Y}⋅\overline{Z} + \overline{X}⋅Y⋅\overline{Z}+X\overline{Y}Z+XYZ$
- to find the PoM $F$
  - $F=ΠM(1,3,4,6)$
- draw the *two-level circuits* for $F$ in the two forms


💡 Demo
---
- Convert $F=\overline{Y}+\overline{X}Z$ into som and PoM using two ways: 
  - ➊ truth table and 
  - ➋ algebraic manipulation
  - ans: $F=∑m(0,1,2,4,5)=ΠM(3,6,7)$



📝 Practice
---
- Convert $F=XY+ \overline{Y}+\overline{X}Y\overline{Z}$ into som and PoM using two ways: 
  - ➊ truth table and 
  - ➋ algebraic manipulation
  - ans: $F=∑m(0,1,2,4,5)=ΠM(3,6,7)$


Properties of the standard forms
---
- Any Boolean function can be expressed as 
  - a logical sum of minterms (som)
  - or a logical product of maxterms  (PoM)
- A som function that includes all the $2^n$ `minterms` is equal to logic `1`
- A PoM function that includes all the $2^n$ `maxterms` is equal to logic `0`



Optimize two-level circuits
---
- som and PoM circuits can be implemented in two-level circuits
  - can be optimized by minimizing the gates used
- two popular ways for simplifying a Boolean function
  - algebraic manipulation
    - difficult to determine whether the simplest expression has been achieved
  - Karnaugh map (K-map)
    - a visual method
    - suitable for Boolean functions of up to four variables




# References
- [symbolab](https://www.symbolab.com/solver/boolean-algebra-calculator)
- [emathhelp](https://www.emathhelp.net/en/calculators/discrete-mathematics/boolean-algebra-calculator/)
- [dcode](https://www.dcode.fr/minterms-maxterms-calculator)
