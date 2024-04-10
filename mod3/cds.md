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



Single-cycle hardwired control
---



Multiple-cycle hardwired control
---

