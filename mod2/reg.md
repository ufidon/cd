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
- (p1.a*) 4-bit register with asynchronous clear'
  - (p1.b) symbol
  - (p1.c) apply load' control: C inputs = load' + clock
    - this technique is called `clock gating`
- (p2). 4-bit register with parallel load


Register transfers
---
- (p3). digital system design can be partitioned into two types of modules
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
    - (p5). hardware implementation


Basic symbols for register transfers
---
- (p6). 
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
- (p8).  add, subtract, increment, decrement, and complement
- (p9). Implementation of Add and Subtract Microoperations
  - X'K₁: R1 ← R1 + R2 (S=0)
    - X'K₁ = 1 when X'=0 and K₁ = 1
  - XK₁: R1 ← R1 + (R2' + 1) (S=1)
    - XK₁ = 1 when X=1 and K₁ = 1
  - K₁ = 0, inhibits the operations
  - together can be simplified
    - X'K₁+XK₁ = (X'+X)K₁ = K₁
    - K₁ loads the result into R1
    - X selects the operation


Logic microoperations
---
- (p10)


🍎 Example
---
❶ The meaning of a symbol depends on its context:
- (K1 + K2 ): R1 ← R2 + R3, R4 ← R5 ∨ R6
  - K1 + K2 means K1 OR K2
  - R2 + R3 means the sum of R2 and R3
  - R5 ∨ R6 means R5 or R6

❷ Implementation of logic microoperations
- The NOT of a register of n bits is obtained with n NOT gates in parallel
- The AND microoperation is obtained using a group of n AND gates
  - each receiving a pair of corresponding inputs from the two source registers
  - The outputs of the AND gates are applied to the corresponding inputs of the destination register
- The OR and exclusive-OR (XOR) microoperations require a similar arrangement of gates

❸ The logic microoperations can `change` bit values such as
- The `AND` microoperation can be used for `clearing` one or more bits in a register to 0
  - `clear` a group of bits:  `X ⋅ 0 = 0 and X ⋅ 1 = X`
- The `OR` microoperation is used to `set` one or more bits in a register
  - `set` a group of bits: `X + 1 = 1 and X + 0 = X`
- The `XOR` (exclusive-OR) microoperation can be used to `complement or negate` one or more bits in a register
  - `complement` a group of bits in a register: `X ⊕ 1 = X' and X ⊕ 0 = X`
- ➀ clear the most significant 8 bits of R1
  - (data) R1 = `11001010` 01011101 
  - (mask) R2 = `00000000` 11111111
  - after R1 ← R1 ∧ R2: R1 = `00000000` 01011101
- ➁ set the most significant 8 bits of R1
  - (data) R1 = `11001010` 01011101 
  - (mask) R2 = `11111111` 00000000
  - after R1 ← R1 ∨ R2: R1 = `11111111` 01011101
- ➂ complement the most significant 8 bits of R1
  - (data) R1 = `11001010` 01011101 
  - (mask) R2 = `11111111` 00000000
  - after R1 ← R1 ⊕ R2: R1 = `00110101` 01011101


Shift microoperations
---
- (p11) many applications
  - lateral movement of data
  - serial transfer of data
  -  manipulating the contents of registers in arithmetic, logical, and control operations
- The contents of a source register can be shifted either right or left
- The destination register for a shift microoperation may be 
  - the same as or different from the source register
  - A `left` shift is toward the `most` significant bit 
  - A `right` shift is toward the `least` significant bit
- The `incoming bit` is 
  - the `rightmost` bit of the `destination` register for a `left`-shift microoperation
  - the `leftmost` bit of the `destination` register for a `right`-shift microoperation
- The incoming bit may have different values depending upon the type of shift microoperation
  - here it is assumed to be 0 for both sr and sl
- The `outgoing` bit is 
  - the `leftmost` bit of the `source` register for the `left`-shift operation
  - the `rightmost` bit of the `source` register for the `right`-shift operation
  - here the outgoing bit value is simply `discarded`


🍎 Example
---
if R0 = `1010 0101`, R2 = `1101 1010`, find the new value of R0, R1 and R2 after the following shifts:
- a `one-bit shift to the right` of the contents of register R0
  - R0 ← sr R0
- a transfer of the contents of R2 shifted `one bit to the left` into register R1
  - R1 ← sl R2
  - The contents of R2 are not changed by this shift


Microoperations on a single register
---
- microoperations are implemented with combinational logic
  - the logic may be `dedicated` to a single register or
  - shared by a set of destination registers
- (p12) the source of multiple registers can be selected with multiplexer, e.x.
  - if (K₁=1) then (R0←R1) else if (K₂=1) then (R0←R2)
  - which can be implemented as: K₁:R0←R1, K₁'K₂:R0←R2
- (p13) generalization: n sources to 1 destination
  - these sources could to be register outputs or combinational logic implementing microoperations
    - the first k sources are dedicated logic 
    - the last n - k sources are either registers or shared logic
  - The control signals that select a given source are either a single control variable or the OR of all control signals corresponding to the microoperations associated with the source
    - To force R0 to load for a microoperation, these control signals are ORed together to form the Load signal
      - Since it is assumed that only one of the control signals is 1 at any time
    - these signals must be encoded to provide the selection codes for the multiplexer


Shift registers
---
- A `shift` register can shift its stored bits laterally in `one or both directions`
  - consists of a chain of flip-flops
    - with the output of one flip-flop connected to the input of the next flip-flop
    - share a common clock-pulse input that activates the shift
- (p14). `unidirectional shift register` can shift its stored bits laterally in  one direction
  - if the current bit values in the flip-flops are `1011`,
  - ❓ what are their values after 1, 2, 3, 4, ⋯, n clocks if 
    - SI = 0? (`zero extension`)
    - SI = 1? (`one extension`)
- (p15). shift register with parallel load
  - used for converting incoming `parallel` data to outgoing `serial` data and vice versa
  - shift: Q←sl Q
  - shift'⋅load: Q←D
  - (p16). function table
- (p17). `bidirectional shift register` with parallel load
  - can shift in both directions
  - (p17.a) each stage consists of a D flip-flop and a 4–to–1-line multiplexer
    - S1'S0: Q←sl Q (Qᵢ ← Qᵢ₋₁)
    - S1S0': Q←sr Q (Qᵢ → Qᵢ₋₁)
    - S1S0 : Q← Q
  - (p18). function table
- Behavioral Verilog description of 4-bit left shift register with direct reset
```verilog
module srg_4_r_v (CLK, RESET, SI, Q,SO);
  input CLK, RESET, SI;
  output [3:0] Q;
  output SO;

  reg [3:0] Q;
  assign SO = Q[3];
  always @(posedge CLK or posedge RESET)
  begin
    if (RESET)
      Q <= 4'b0000;
    else
      Q <= {Q[2:0], SI};
  end
endmodule
```
- Behavioral VHDL description of 4-bit left shift register with direct reset
```vhdl
architecture behavioral of srg_4_r is
signal shift : std_logic_vector(3 downto 0);
begin
process (RESET, CLK)
begin
  if (RESET = '1') then
    shift <= "0000";
  elsif (CLK’event and (CLK = '1')) then
    shift <= shift(2 downto 0) & SI;
  end if;
end process;
  Q <= shift;
  SO <= shift(3);
end behavioral;
```



Ripple counter
---
- A `counter` goes through a prescribed sequence of distinct states
  - upon the application of a sequence of `input pulses`
  - may be clock pulses or other pulses that may occur at `regular or irregular `intervals of time
- A `binary counter` follows the binary number sequence
  - An n-bit binary counter consists of n flip-flops and can count in binary 
    - from 0 through 2ⁿ-1
- two types of counters
  - ripple counters: the flip-flop output transitions serve as the sources for triggering the changes in other flip-flops
    - i.e. the C inputs of some of the flip-flops are triggered not by the common clock pulse, but rather by the transitions that occur on other flip-flop outputs
    - (p19). a 4-bit ripple counter
      - this is an `upward` counter
      - the application of a positive edge to the C input of each flip-flop causes the flip-flop to complement its state
      - The complemented output of each flip-flop is connected to the C input of the next most significant flip-flop
      - The flip-flop holding the least significant bit receives the incoming clock pulses. 
      - Positive-edge triggering makes each flip-flop complement its value when the signal on its C input goes through a positive transition. 
      - The positive transition occurs when the complemented output of the previous flip-flop, to which C is connected, goes from 0 to 1.
      - A 1-level signal on Reset driving the R inputs clears the register to all zeros asynchronously.
      - The count starts at binary 0 and increments by one with each count pulse. After the count of 15, the counter goes back to 0 to repeat the count.
    - (p20). counting sequence, 💡show 0011 to 0100
      - 0011 → 0010 → 0000 → 0100
        - The flip-flops `change one at a time in quick succession` as the signal propagates through the counter in a `ripple fashion` from one stage to the next
      - `Downward` counting can be accomplished by connecting the `true output` of each flip-flop to the C input of the next flip-flop
    - advantages
      - simple hardware
    - disadvantages
      - there are delay dependence and unreliable operation as asynchronous circuits  with added logic
      - particularly true for logic that provides feedback paths from counter outputs back to counter inputs
      - due to the length of time required for the `ripple` to finish, `large ripple` counters can be `slow` circuits.
  - synchronous counters
    - the C inputs of all flip-flops receive the common clock pulse, and the change of state is determined from the present state of the counter


Synchronous binary counters
---
- a `common clock` applied to the C inputs of all flip-flops
  - its pulse triggers all flip-flops simultaneously rather than one at a time as in a ripple counter
- (p21). a 4-bit synchronous binary counter
  - The polarity of the clock is not essential here as it was for the ripple counter
  - The synchronous counter can be designed to trigger with either the positive or the negative clock transition
- (p21).a `serial gating` for serial counter
  - used a chain of 2-input AND gates to provide information to each stage about the state of the prior stages in the counter
  - analogous to the carry logic in the `ripple carry adder`
- (p21).b `parallel gating` for parallel counter
  - with counter logic analogous to the `carry lookahead adder`
  - replaces the dashed blue box in (p21).a with (p21).b
  - advantage:
    - in going from state 1111 to state 0000, only one AND-gate delay occurs instead of the four AND-gate delays that occur for the serial counter
    - This reduction in delay allows the counter to operate much faster
  - An 8-bit serial-parallel counter can be created by connecting two 4-bit parallel counters together by connecting the CO output of one to the EN input of the other
    - The idea can be extended to counters of any length
    - parallel gating logic can be used to replace the serial connections between the 4-bit segments to construct large, fast counters
- (p22). a 4-bit synchronous binary counter with parallel load
  - controlled by two inputs `Load` and `Count` of four combinations
  - only three operations are provided: 
    - Load (10), Count (01), and Hold (00)
  - for (11), a load occurs
    - This is sometimes described as `Load overriding Count`
  - The implementation uses an `incrementer` plus `2n + 1 ENABLEs`, `a NOT gate`, and `n 2-input OR gates`
    - The `first n ENABLEs` with enable input Load are used to enable and disable the parallel load of input data D
    - The `second n ENABLEs` with enable input Load on the incrementer outputs are used to disable both the count and hold operations when Load = 1
    - When Load = 0, both count and hold are enabled
    - Without the additional ENABLE, Count = 1, causes counting, and Count = 0, the hold operation occurs
    - Counting is disabled by the Load' signal and loading is enabled by Load
  - can be converted into a BCD counter (p23)
    - starts with an all-zero output
    - the count input is always active
    - counts from 0000 through 1001, followed by 0000
- Behavioral Verilog description of 4-bit binary counter with direct reset
```verilog
module count_4_r_v (CLK, RESET, EN, Q, CO);
  input CLK, RESET, EN;
  output [3:0] Q;
  output CO;

  reg [3:0] Q;
  assign CO = (count == 4'b1111 && EN == 1’b1) ? 1 : 0;
  
  always @(posedge CLK or posedge RESET)
  begin
    if (RESET)
      Q <= 4'b0000;
    else if (EN)
      Q <= Q + 4'b0001;
  end
endmodule
```
- Behavioral VHDL description of 4-bit binary counter with direct reset
```vhdl
architecture behavioral of count_4_r is
signal count : std_logic_vector(3 downto 0);
begin
process (RESET, CLK)
begin
  if (RESET = '1') then
    count <= "0000";
  elsif (CLK'event and (CLK = '1') and (EN = '1')) then
    count <= count + "0001";
  end if;
end process;
  Q <= count;
  CO <= '1' when count = "1111" and EN = '1' else '0';
end behavioral;
```


Up-down binary counter
---
- A down binary counter goes through 1111 to 0000 and back to 1111 to repeat the count
- A up binary counter goes through 0000 to 1111 and back to 0000 to repeat the count
- they can be combined into a up-down binary counter by 
  - contracting an adder–subtractor into an incrementer–decrementer
- can be designed directly from counter behavior with the following flip-flop [input equations](https://www.boolean-algebra.com/kmap/):
  - D<sub>A0</sub> = Q₀ ⊕ EN
  - D<sub>A1</sub> = Q₁ ⊕ ((Q₀S' + Q₀'S)EN)
  - D<sub>A2</sub> = Q₂ ⊕ ((Q₀Q₁S' + Q₀'Q₁'S)EN)
  - D<sub>A3</sub> = Q₃ ⊕ ((Q₀Q₁Q₂S' + Q₀'Q₁'Q₂'S)EN)
  - S = 0 for up-counting and S = 1 for down-counting
  - EN = 1 for normal up- or down-counting and EN = 0 for disabling both counts


Other counters
---
- Counters can be designed to generate any desired number of states in sequence
- A `divide-by-N counter` (or `modulo-N counter`)
  - goes through a repeated sequence of N states following
    - the binary count or any other arbitrary sequence
  - needs `⌈log₂N⌉` flip-flops
- designed with the methods for synchronous sequential circuits



💡 Design a BCD counter directly
---
- count from `0000(0)` through `1001(9)`, followed by 0000
  - a `module-10` counter needs `⌈log₂10⌉ = 4` flip-flops
- (p24). state table and flip-flop inputs for BCD counter
  - the unused states for minterms 1010 through 1111 are used as don't-care conditions
- simplified [input equations](https://www.boolean-algebra.com/kmap/) for the BCD counter
  - D₁=Q₁'
  - D₂=Q₂⨁Q₁Q₈'
  - D₄=Q₄⨁Q₁Q₂
  - D₈=Q₈⨁(Q₁Q₈+Q₁Q₂Q₄)
  - CO=Q₁Q₈


💡 Design an arbitrary counter
---
- repeat a sequence of six states specified in (p25)
  - it needs `⌈log₂6⌉ = 3` flip-flops
  - flip-flops B and C repeat the binary count 00, 01, 10
  - flip-flop A alternates between 0 and 1 every three counts
  - state 011 and 111 are not included in the count
    - can be used as don't-care conditions
- simplified [input equations](https://www.boolean-algebra.com/kmap/)
  - D<sub>A</sub> = A⨁B
  - D<sub>B</sub> = C
  - D<sub>C</sub> = B'C'
- (p26.a) logic diagram
  - (p26.b) state diagram
    - if the circuit ever goes to one of the unused states, 
    - the next count pulse transfers it to one of the valid states
    - 🏃 verify them on the circuit diagram
- 🏃 reimplement this counter with a 4-bit binary counter