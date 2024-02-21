# Sequential Circuits
_lcdf5 chapter 4_


Topics
---
- circuits capable of storing information
  - synchronous sequential circuit synchronized with clock
    - flip-flops
  - asynchronous sequential circuits states changes are
    - triggered by the changes in inputs
    - latches
- describes sequential circuits in
  - State transition tables
  - state transition diagrams


Sequential Circuit Definitions
---
p1
- the output Y and next state S' of a sequential circuit depends on its current state S and input X:
  - $Y+S' = f(S, X)$


Logic Structures for Storing Information
---
p2 describes several primitive storage circuits
- $t_G$ is the gate delay in several to hundreds of nanoseconds
- a) input appears at the output after $t_G$
- 0 is stored forever in b), 1 in c), and X in d)

However, there is no way to override the storage without additional inputs. 
- Asynchronous storage circuits called latches are made from these storage circuits by replacing the inverters with NOR or NAND gates
- Synchronous circuits are built from latches together with a clock generator p3
  - their outputs can change their value only in the presence of clock pulses
  - those use clock pulses as inputs for storage elements are called `clocked sequential circuits`
  - the simplest form of clocked sequential circuits are called `flip-flops`
    - they store only one bit of information
    - and change state only in response to a clock pulse

SR latch
---
- p4 The SR latch is a circuit constructed from two cross-coupled NOR gates. 
- It has 
  - two inputs `set` S and `reset` R
  - two outputs $Q$ and $\bar{Q}$ are `normally` the complements of each other
- It is in one of the sates below at a time
  - `set state` when $(Q,\bar{Q})=(1,0)$
  - `reset state` when $(Q,\bar{Q})=(0,1)$
  - `undefined state` when $(Q,\bar{Q})=(0,0)$ and (S,R)=(1,1)
    - since it violates the requirement that the outputs be the complements of each other
    - It also results in an indeterminate or unpredictable next state when both inputs return to 0 simultaneously
- (S,R)=(0,0) is the `normal condition`
  - during normal operation, only one of S and R can be changed to 1 from 0
  - (S,R)=(1,0) transits the SR latch to `set state`
  - (S,R)=(0,1) transits the SR latch to `reset state`
- The behavior of the SR latch is illustrated in p5
  - sequence matters in sequential sequential circuits
  - a signal state is unknown when its level is 1/2 in p5
    - at the beginning, (S,R) and $Q, \bar{Q}$ are all unknown
    - (S, R)=(0, 1) → (Q,Q')=(0,1)
    - (S, R)=(0, 0) → (Q,Q')=(0,1)
    - (S, R)=(1, 0) → (Q,Q')=(1,0)
    - (S, R)=(0, 0) → (Q,Q')=(1,0)
    - (S, R)=(0, 1) → (Q,Q')=(0,1)
    - (S, R)=(0, 0) → (Q,Q')=(0,1)
    - (S, R)=(1, 1) → (Q,Q')=(1,1)
    - (S, R)=(0, 0) → (Q,Q')=(x,x)
  - In general, the latch state changes only in response to input changes and remains unchanged otherwise


$\bar{S}\bar{R}$ latch
---
- p6 The $\bar{S}\bar{R}$ latch with two cross-coupled NAND gates
  - has `set state` and `reset state` identical to SR latch
  - but has inputs and `undefined state` contrary to SR latch


SR Latch with Control Input
---
The operation of the basic NOR and NAND latches can be modiied by providing an additional control input that determines when the state of the latch can be changed.
- An SR latch with a control input is shown in p7


D Latch p8
---
- eliminates the `undefined state` in the SR latch 
  - by ensuring that S and R are never 1 at the same time
- receives its designation from its ability to hold data
  - When C=1, D → Q
  - When C=0, Q outputs old D
- it has an unreliable operation can be solved with `master–slave` flip-flop in p9
  - the left is the master and the right is the slave
- flip-flop state changes have two trigger schemes
  - `pulse-triggered` or `level-triggered` has two types
    - `positive-pulse triggered` or `high-level triggered` 
    - `negative-pulse triggered` or `low-level triggered`
  - `edge-triggered`, prevalent in contemporary design, also has two types
    - `negative-edge triggered` or `falling-edge triggered` p9
    - `positive-edge triggered` or `rising-edge triggered` p10
- The standard graphics symbols for the different types of latches and lip-lops are shown in p11


Direct Inputs
---
- Flip-flops can set and reset their storages asynchronously by
  - direct set or preset to 1
  - direct reset or clear to 0
- D Flip-Flop with Direct Set and Reset p12
