__Memory Basics__
_lcdf5 chapter 7_


Memory definitions
---
- memory is a collection of `cells` capable of storing binary information
  - integrated electronic circuits for `storing and retrieving` the information
    - storing is by `memory write` operations
    - retrieving is by `memory read` operations
- two types
  - random-access memory (RAM) stores data `temporarily`
  - read-only memory (ROM) stores data `permanently`


Random-Access Memory
---
- Binary information is stored in memory in `groups of bits` called `words`
  - an entity of bits that moves in and out of memory as a unit
- Most computer memories use words that are `multiples of eight bits` in length
   - an `8-bit` word is called a `byte`
   - a `16-bit` word contains `2 bytes`, and a `32-bit` word is made up of `4 bytes`
- The `capacity of a memory` is the `total number of bytes` that it can store
  - specified in binary prefix
  - K (kilo) = 2¹⁰, M (mega) = 2²⁰, or G (giga) = 2³⁰
- (p1) A block diagram of a memory shows signals of
  - n data input and output lines determine
    - word length in bits = number of data lines
  - k address selection lines determine 
    - address range [0, 2ᵏ-1] and number of words 2ᵏ
    - each word in memory is assigned an location called `address`
  - and control lines that specify the direction of transfer of information
- (p2) Contents of a 1024 × 16 Memory


Write and Read Operations
---
- A `write` is a transfer `into` memory of a new word to be stored
- A `read` is a transfer of a copy of a stored word `out` of memory
- (p3) Control inputs to a memory Chip for read/write'


Timing Waveforms
---
- (p4) The operation of the memory is often controlled by a CPU
- The `access time` of a memory `read` operation is 
  - the maximum time from the application of the address to the appearance of the data at the Data Output
  - the `write cycle time` is the maximum time from the application of the address to the completion of all internal memory operations required to store a word


Properties of Memory
---
- Integrated-circuit RAM may be either `static or dynamic`
  - `Static RAM (SRAM)` consists of internal latches that store the binary information. the stored information remains valid as long as power is applied to the RAM. 
  - `Dynamic RAM (DRAM)` stores the binary information in the form of electric charges on capacitors
    - the capacitors must be periodically recharged by `refreshing` the DRAM
- Memory that lose stored information when power is turned off are said to be `volatile`
  - such as RAMs, both static and dynamic
- `nonvolatile memory` maintain the stored information even power is off
  - such as ROM, CD/DVD, magnetic disk, etc.


Sram Integrated Circuits
---
- a RAM chip of `m words` with `n bits per word` consists of 
  - an array of `mn binary storage cells` and associated circuitry
  - (p5) the logic model of the RAM cell by an SR latch
- (p6) a RAM `bit slice` contains all of the circuitry associated with a single bit position of a set of RAM words
  - (p7) The symbol and block diagram for a 16 × 1 RAM chip
- a `coincident selection` scheme uses two k/2-input decoders instead of one k-input decoder
  - One decoder controls the word select lines and the other controls the bit select lines
  - The result is a two-dimensional matrix selection scheme (p8) with
    - `Row Select` and `Column Select`
  - (p9) Block Diagram of an `8 × 2` RAM Using a 4 × 4 RAM Cell Array


Array Of Sram ICs
---
- (p10) Symbol for a 64K × 8 RAM Chip
- (p11) construct a 256K × 8 RAM with four 64K × 8 RAM chips
- (p12) Block diagram of a 64K * 16 RAM


DRAM ICs
---
- dominates the `high-capacity` memory applications
- (p13) The dynamic RAM cell circuit
- (p14) DRAM bit slice
- (p15) Block diagram of a DRAM including refresh logic
- (p16) Timing for DRAM write and read operations


DRAM refreshing
---
The standard ways in which a refresh cycle can be triggered and the corresponding refresh types are as follows:
- Ras-only refresh
- CAS-before-RAS refresh
- Hidden refresh


DRAM types
---
- (p17-18)
- Synchronous DRAM (SDRAM)
  - (p19) Block diagram of a 16 MB SDRAM
  - (p20) Timing diagram for an SDRAM
- Double-data-rate SDRAM (DDR SDRAM)
  - provides two bytes of data per clock period by using both the positive and negative clock edges
  - eight bytes can be transferred in the same read cycle time ${t_{RC}}$
- RAMBUS DRAM (RDRAM) (p21)