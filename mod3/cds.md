# Computer Design Basics
_lcdf5 chapter 8_


A simple computer
---
- a programmable system (PS) consists of 
  - a generic datapath
  - a control unit described by control words
  - memory
- specified by instruction set architecture (ISA)
  - implemented as a CPU (central processing unit)
- two different types
  - type ❶ has two memory
    - one for instructions and one for data
    - performs all of its operations in a `single clock cycle`
  - type ❷ has a single memory for both instructions and data
    - performs its operations in `multiple clock cycles`


Introduction
---
- ISA present a `programming interface` to the programmer
- The implementation hardware is formulated by a high-level description `computer architecture` divided into a `datapath` and a `control unit`
  - The `datapath` is defined by `three` basic components:
    - a set of `registers`
    - the `microoperations` performed on data stored in the registers
    - the control interface
  - The `control unit` controls
    - the microoperations
    - its own operations
    - other components of the system such as memories
-  Different ISAs can be implemented by combining the `datapath` with `different control units`


Datapaths
---
- employ a number of `storage registers` with a shared combinational operation unit called an `arithmetic/logic unit (ALU)`
- perform 3 consecutive operations during `one clock cycle`
  - the entire register `transfer` operation from the `source` registers 
  - through the ALU for `microoperations`
  - and transfer the result onto the inputs of the `destination` register
- perform shift operations in a separate unit or within the ALU
- (p1) shows a simple bus-based datapath with four registers, an ALU, and a shifter
  - to perform `R1 ← R2 + R3`, the control unit must provide the following signals
    - `A select`, to place the contents of R2 onto A data and, hence, Bus A
    - `B select`, to place the contents of R3 onto the 0 input of MUX B
      - and `MB select`, to put the 0 input of MUX B onto Bus B
    - `G select`, to provide the arithmetic operation A + B
    - `MF select`, to place the ALU output on the MUX F output
    - `MD select`, to place the MUX F output onto Bus D
    - `Destination select`, to select R1 as the destination of the data on Bus D
    - `Load enable`, to enable a register—in this case, R1—to be loaded
  - the result is loaded into the destination register R1 when the next positive clock edge arrives


The ALU
---
- performs a set of basic `arithmetic and logic  microoperations` by a `combinational` circuit consists of `arithmetic circuit` and `logic circuit`
- (p2) The `arithmetic circuit` has the basic component a `parallel adder`
  - (p3) possible to perform different types of arithmetic operations
    - `G=X+Y+Cᵢₙ`, here `+` is arithmetic addition
  - (p4) the operation type is selected by S₁ and S₀
    - the B input logic can be implemented with a n-bit 4-to-1 multiplexer
    - or with gates directly for each `stage i`
      - (p5) ${ Y_i = B_iS_0 + \bar{B}_iS_1 }$
      - the selection circuit is shown in (p6)
  - (p6) shows the parallel adder implemented with full-adders
  - (p7) shows the `eight arithmetic operations` for the circuit as a function of `S₁, S₀, and Cᵢₙ`
- The `logic circuit` supports four commonly used logic operations—AND, OR, XOR, and NOT
  - (p8) shows one stage of the logic circuit
- (p9) The logic circuit can be combined with the arithmetic circuit to produce an ALU



The shifter
---
- (p10) a combinational shifter is preferred
  - the signals propagate through the gates without the need for a clock pulse
  - ∴ the `only clock `needed for a shift in the datapath is for loading the data from Bus H into the selected destination register
  - S=00, B passes through the shifter `unchanged`
  - S=01, a right-shift operation
    - fills the position on the left with the value on serial input Iᵣ
  - S=10, a left-shift operation
    - fills the position on the right with the value on serial input Iₗ
  - Serial outputs are available from serial output R and serial output L for right and left shift respectively
  - to shift an operand by m > 1 bit positions, this shifter must perform a series of m 1-bit position shifts, taking m clock cycles


Barrel shifter
---
- can shift or `rotate` the input data bits by the number of bit positions specified by a binary value on a set of selection lines in a `single clock cycle`
- (p11) shows a `4-bit version` of this kind of barrel shifter
  - (p12) the input data will be `shifted to the left S₁S₀ positions` by rotation
  - S₁S₀ = 0, no rotation occurs, Y[3:0]=D[3:0]
  - S₁S₀ = 1, rotates 1 position, Y[3:1,0]=D[2:0,3]
  - S₁S₀ = 2, rotates 2 position, Y[3:2,1:0]=D[1:0,3:2]
  - S₁S₀ = 3, rotates 3 position, Y[3,2:0]=D[0,3:1]
- All desired right rotations can be generated using this 4-bit left-rotation barrel shifter
  - a left rotation by 3 positions is the same as a right rotation by 1 position
- In a `2ⁿ`-bit barrel shifter, `i` positions of `left` rotation are the same as `2ⁿ - i` bits of `right` rotation
- A barrel shifter with `2ⁿ input and output lines` requires `2ⁿ multiplexers`
  - each having 2ⁿ data inputs and n selection inputs
  - The number of positions for the data to be rotated is specified by the selection variables and can be from `0 to 2ⁿ − 1 positions`


Datapath representation
---
- (p13) a `hierarchical` structure can reduce the `apparent complexity` of the datapath
  - allows one implementation of a module to be replaced with another
  - A `register file` is a set of registers having common microoperations performed on them
- (p14) FS defines all of the codes for MF select, G select, and H select in (p1)
  - MF = F₃F₂,  G[3:0]=F[3:0], H[1:0]=F[1:0]



The control word
---
- (p15) control variables select the microoperations for the datapath
  - there are 8 registers, R0 through R7
  - the function unit generate the binary data for the four status bits:
    - V (overflow), C (carry), N (sign), and Z (zero)
- The combined values of the 16 binary control inputs specify a `control word` which
  - consists of 7 fields each designated by 2 letters
- The 3 register fields are 3 bits each
  - The 3 bits of `DA` select one of 8 `destination` registers for the result of the microoperation
  - The 3 bits of `AA` select one of 8 `source` registers for the `Bus A` input to the ALU
  - The 3 bits of `BA` select a `source` register for the 0 input of the `MUX B`
- The remaining fields have one or four bits
  - The 1 `MB` bit determines whether Bus B carries the contents of the selected source register or a constant value
  - The 4-bit `FS` field controls the `operation` of the function unit
  - The 1 bit of `MD` selects the function unit output or the data on Data in as the input to Bus D
  - The 1 bit `RW` determines whether a register is written or not
- (p16) Each control word specifies a particular `microoperation`
  - R1 ← R2 + R3' + 1

| Field | DA | AA | BA | MB | FS | MD | RW |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Symbolic | R1 | R2 | R3 | Register | F = A+B'+1 | Function | Write |
| Binary | 001 | 010 | 011 | 0 | 0101 | 0 | 1 |

- (p17) examples of microoperations for the Datapath using symbolic notation
- (p18) examples of microoperations for the (p17) using binary notation
  - X's are unspecified values
- (p19: optional) simulation of the microoperation sequence in (p18)
  - the initial content of each register is its number in decimal
  - changes in registers as a result of a particular microoperation appear in the clock cycle after that in which the microoperation is speciied
  - the values on the Status bits, Address out, and Data out appear in the same clock cycle as the microoperation controlling them
    - they are not always meaningful


A simple computer architecture
---
- A `programmable` system reads, decodes, and executes `sequences of instructions` called `programs`
  - from memory such as RAM or ROM
- Each instruction specifies an `operation` the system is to perform
  - which `operands` to use for the operation
  - `where to place the results` of the operation
  - and/or, in some cases, `which instruction to execute next`
- The `program counter (PC)` register generates `addresses in memory of the instructions` to be executed
  - the PC can `change the sequence` of operations based on `status` information by parallel load


Instruction Set Architecture (ISA)
---
- A computer's `instruction set` is the collection of instructions 
- Its `instruction set architecture (ISA)` describes the instruction set thoroughly by three major components: 
  - (p20) storage resources
  - instruction formats
  - instruction specifications


Instruction Formats
---
- (p21) the general `layout of the bit fields` of instructions
  - `opcode (operation code)` specifies an `operation` such as add, subtract, shift, or complement
    - to be performed through `a sequence of control words` applied to the datapath
      - these control words are generated by the control unit
    - N distinct operations needs `⌈log₂N⌉` bits
  - `operands` are the data manipulated by operations
    - stored in registers or memory
    - `specified explicitly` by special bits in the instructions for their locations
      - such as `(p21.a) Register`: 
        - ADD: DR ← SA + SB
        - STORE: M[SA] ← SB   'M[SA] is the memory location with address in SA
    - `defined implicitly` as a part of the definition of the opcode
      - such as an Increment Register operation
        - one of the operands is implicitly +1
- `(p21.b) Immediate`: DR ← SA opcode OP
  - The 3-bit `Operand (OP)` is a constant called an `immediate operand`
    - immediately available in the instruction
    - to become a 16-bit operand, the remaining 13 bits must be `zero-filled or sign-extended`
- `(p21.c) Jump and branch`:
  - affects the order in which the instructions are fetched from memory without changing any register file or memory contents
  - `Branch` provides branch addresses within a small range below and above the PC
value
    - condition(SA): PC ← PC + AD[8:6,2:0] in `signed 2s complement`
      - range: -2⁵=-32 to 2⁵-1=31
    - AD[8:6,2:0] is called the `address offset`. It is extended to be 16 bits offset A before addition. A[4:0]=AD[7:6,2:0] and
      - if AD[8]=1, A[15:5]=1 (sign extension) for negative numbers
      - if AD[8]=0, A[15:5]=0 (zero fill) for positive numbers
  - `Jump` provides a broader range of addresses by using the unsigned contents of a 16-bit register as the jump target
    - range: 0 to 2¹⁶-1=65535



Instruction Specifications
---
- (p22-23) symbolically describe `each of the distinct instructions` 
  - `mnemonic` for the opcode
  - other symbols for all other fields
- This `symbolic representation` is called `assembly language`
  - converted into `binary representation` by a program called `assembler`
- (p24) shows a piece of memory containing instructions and data
  - Suppose 
    - R4 contains 70 and R5 contains 80
    - the addition to the PC content occurs before the PC has been incremented
  - 🏃 decode each line


Single-cycle hardwired control
---
- (p25.l) fetches and executes an instruction in a single clock cycle
- has a `load/store` architecture since it has dedicated `load and store instructions`
- The PC is updated in each clock cycle
  - determined by the opcode and status flags such as N and Z
  - incremented by 1 by default
  - or jump or branch to a new address = PC + offset



Instruction Decoder
---
- (p26) a combinational circuit that provides `control words`(p15) for the datapath
  - based on the contents of the `instruction`
- Some fields of the control word can be obtained directly from the instruction
  - (DA,AA,BA) = (DR, SA, SB)
  - BC that selects branch condition status bit = Opcode[9]
  - datapath and data memory control bits MB, MD, RW, and MW
  - PL and JB control PC 
    - `PL = 1` loads the PC if there is to be a jump or branch
    - `PL = 0` increments PC
    - `PL = 1, JB = 1` calls for a jump
    - `JB = 0` calls for a conditional branch
- the logic circuit in (p26) is derived from truth table (p27)
  - optimized with those don’t-care (X) entries


💡 Demo
---
- ❶ Run the sample instructions in (p28) on (p25)
- ❷ An example assembly program 
  - calculates: 
    - 83 - (2 + 3) ;represented in signed 2s complement
  - given
    - M[R3] = 2; R3=248
    - M[249] = 83
    - M[250] saves result
```nasm
LD    R1,R3     ;Load R1 with contents of location 248 in memory (R1 = 2)
ADI   R1, R1,3  ;Add 3 to R1 (R1 = 5)
NOT   R1, R1    ;Complement R1
INC   R1, R1    ;Increment R1 (R1 = - 5)
INC   R3, R3    ;Increment the contents of R3 (R3 = 249)
LD    R2, R3    ;Load R2 with contents of location 249 in memory (R2 = 83)
ADD   R2, R2,   ;R1 Add contents of R1 to contents of R2 (R2 = 78)
INC   R3, R3    ;Increment the contents of R3 (R3 = 250)
ST    R3, R2    ;Store R2 in memory location 250 (M[250] = 78)
```

Single-Cycle Computer (SCC) Issues
---
- Many complex operations can't be done in one clock cycle
  - such as the division of float point numbers
- Accessing instruction and data from the same memory needs two clock cycles
  - the single-cycle computer above has two distinct 16-bit memories 
    - one for instructions and one for data
- The SCC has a lower limit on the clock period based on a long `worst-case delay` path
  - (p29) has a total delay along the path of 9.8 ns
    - limits the clock frequency to about 102 MHz
  - can be relieved by reducing the number of components in the longest combinational delay path through `pipeline`


Multiple-cycle hardwired control
---
- (p30) uses a `single memory` for both data and instructions
- implements more complex instructions by saving the instruction in the `instruction register IR` across `multiple clock cycles`
- added `temporary storage registers 8 through 15` used only during instruction execution
  - `R8-15` are not part of the storage resources visible to the user
- divides the `control word` into two parts
  - `Sequence control` determines the `next state` of the overall control unit 
  - `Datapath control` controls the `microoperations` executed by the Datapath and Memory M


Multiple-Cycle Computer (MCC) control word
---
- shown in (p31)
  - the fields DX, AX, and BX control the register selection
    - DA ← 0 ∥ DR if msb(DX) = 0 else DX
    - AA ← 0 ∥ SA if msb(AX) = 0 else AX
    - BA ← 0 ∥ SB if msb(BX) = 0 else BX
- fields for 
  - datapath defined in (p32)
  - sequence control in (p33)
    - `NS` provides the `next state` for the Control State Register (CSR)
    - `PS` controls the program counter PC
      - `00` holds PC
      - `01` increments PC by 1
      - `10` conditionally loads PC plus sign-extended AD
      - `11` unconditionally loads the contents of R[SA]
    - `IL` controls IR loading
      - a `new` instruction is `loaded` when `IL = 1`
      - the instruction remains `unchanged` when `IL = 0`


Sequential Control Design
---
- separate the cycles into two processing steps:
  - instruction `fetch` and instruction `execution`
- the `partial state diagram` for the two-cycle instructions is given in (p34)
  - the instruction fetch occurs in state `INF`
  - in state `EX0`, the instruction is `decoded` and the microoperations executing `all or part` of the instruction appear in Mealy-type outputs
    - If additional states are required for instruction execution, the next state is `EX1` (p35) or more (p36)
  - unused opcodes will be don’t-care inputs (p37-38)
    - or cause an exception that signals their presence
