# Registers and Register Transfers
_lcdf5 chapter 6_


Topics
---
- registers and counters
- datapath = registers + processing logic + control unit
- microoperations: register transfers


Registers and counters
---
- a register =  a set of flip-flops + state transition logic
- A counter is a register that goes through a predetermined sequence of states on clock ticks


Registers with parallel load
---
- p1.a 4-bit register with asynchronous clear'
  - p1.b symbol
  - p1.c apply load' control: C inputs = load' + clock
    - this technique is called `clock gating`
- p2. 4-bit register with parallel load


Register transfers
---
- p3. digital system design can be partitioned into two types of modules
  - `datapath`: performs data-processing operation
  - `control unit': coordinates those operations
- elementary register operations (microoperations):
  - load, clear, shift, add, subtract, and count
- `register transfer operations` move and process data stored in registers, 
  - specified by three components
    - the set of registers in the system
    - the operations performed on the data stored in the registers
    - the control that supervises the sequence of operations in the system
  - described in `register transfer language (RTL)`


Register transfer operations
---
- registers are typically denoted with uppercase letters
  - AR: address register 
  - PC: program counter
  - IR: instruction register
  - Rₙ such as R₀, R₁, etc. general-purpose registers
  - two layouts of binary string in a register
    - little-endian: the 0 bit is on the right
    - big-endian: the 0 bit is on the left
- registers are graphically represented as a rectangle box p4.
- transfer data from R1 to R2: 
  - R2 ← R1
  - with a condition: K₁: R2 ← R1
    - if (K₁=1) then (R2 ← R1)
    - p5. hardware implementation


Basic symbols for register transfers
---
- p6. 
- two or more parallel register transfers:
  - K₃: R2 ← R1, R3 ← R4
- description in HDL p7


Four types of microoperations
---
- `Transfer microoperations` transfer binary data from one register or memory cell to another
- `Arithmetic microoperations` perform `arithmetic` operations on data in registers
- `Logic microoperations` perform bit manipulation on data in registers
- `Shift microoperations` shift data in registers
- A given microoperation may be of more than one type such as
  - a 2s complement operation is both an arithmetic microoperation and a logic microoperation


Arithmetic microoperations
---
- p8.  add, subtract, increment, decrement, and complement
- p9. Implementation of Add and Subtract Microoperations
  - X'K₁: R1 ← R1 + R2 (S=0)
  - XK₁: R1 ← R1 + R2' + 1 (S=1)
  - K₁ loads the result into R1


Logic microoperations
---
- p10.


Shift microoperations
---
- p11.


Microoperations on a single register
---
- microoperations are implemented with combinational logic
  - the logic may be `dedicated` to a single register or
  - shared by a set of destination registers
- the source of multiple registers can be selected with multiplexer, e.x.
  - if (K₁=1) then (R0←R1) else if (K₂=1) then (R0←R2)
  - which can be implemented as: K₁:R0←R1, K₁'K₂:R0←R2
- p12-13


Shift registers
---
- p14. `unidirectional shift register` can shift its stored bits laterally in  one direction
- p15. with parallel load
  - shift:Q←sl Q
  - shift'⋅load:Q←D
  - p16. function table
- p17. `bidirectional shift register` with parallel load
  - can shift in both directions
  - p17.a each stage consists of a D flip-flop and a 4–to–1-line multiplexer
    - S1'S0: Q←sl Q
    - S1S0': Q←sr Q
    - S1S0 : Q← Q
  - p18. function table


Ripple counter
---
- A `counter` goes through a prescribed sequence of distinct states
- A `binary counter` follows the binary number sequence
  - An n-bit binary counter consists of n flip-flops and can count in binary 
    - from 0 through 2ⁿ-1
- two types of counters
  - ripple counters: the flip-flop output transitions serve as the sources for triggering the changes in other flip-flops
    - p19. a 4-bit ripple counter
    - p20. counting sequence, 💡show 0011 to 0100
  - synchronous counters


Synchronous binary counters
---
- a clock applied to the C inputs of all flip-flops
- p21. a 4-bit synchronous binary counter
  - p21.a serial gating for serial counter 
  - p21.b parallel gating for parallel counter
- p22. a 4-bit synchronous binary counter with parallel load
  - only three operations are provided: 
    - Load (10), Count (01), and Hold (00)
  - for (11), a load occurs
    - This is sometimes described as `Load overriding Count`
  - can be converted into a BCD counter p23
    - counts from 0000 through 1001, followed by 0000


Up-down binary counter
---
- A down binary counter goes through 1111 to 0000 and back to 1111 to repeat the count
- A up binary counter goes through 0000 to 1111 and back to 0000 to repeat the count
- they can be combined into a up-down binary counter by 
  - contracting an adder–subtractor into an incrementer–decrementer


Other counters
---
- Counters can be designed to generate any desired number of states in sequence
- A `divide-by-N counter` (or `modulo-N counter`)
  - goes through a repeated sequence of N states following
    - the binary count or any other arbitrary sequence



💡 Design a BCD counter directly
---
- count from 0000 through 1001, followed by 0000
- p24. state table and flip-flop inputs for BCD counter
  - the unused states for minterms 1010 through 1111 are used as don't-care conditions
- simplified input equations for the BCD counter
  - D₁=Q₁'
  - D₂=Q₂⨁Q₁Q₈'
  - D₄=Q₄⨁Q₁Q₂
  - D₈=Q₈⨁(Q₁Q₈+Q₁Q₂Q₄)
  - CO=Q₁Q₈


💡 Design an arbitrary counter
---
- repeat a sequence of six states specified in p25
  - flip-flops B and C repeat the binary count 00, 01, 10
  - flip-flop A alternates between 0 and 1 every three counts
  - state 011 and 111 are not included in the count
    - can be used as don't-care conditions
- simplified input equations
  - DA = A⨁B
  - DB = C
  - DC = B'C'
- p26.a logic diagram
  - p26.b state diagram
    - if the circuit ever goes to one of the unused states, 
    - the next count pulse transfers it to one of the valid states