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


Datapath representation
---


The control word
---


A simple computer architecture
---


Single-cycle hardwired control
---


Multiple-cycle hardwired control
---

