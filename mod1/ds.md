__Digital Systems__
_lcdf5 chapter 1_


Digital systems and information
---
- ![it](./img/it.gif)
- information is represented as data
- data is encoded as number
- digital computer p2
- embedded systems p5



Signal flow diagram
---
```mermaid
flowchart 
pq(physical quantities<br>analog signal)
qd(quantized data<br>digital signal)
pq --->|ADC<br>analog-to-digital converter|qd
gs(generated signal)
qd --->|DAC<br>digital-to-analog converter|gs
```

Signal flow illustration
---
p3
- ![adda](https://upload.wikimedia.org/wikipedia/commons/5/5a/Conversion_AD_DA.png)


Quantization
---
p4
| 2-bit resolution | 3-bit resolution |
| --- | --- |
| <img src="https://upload.wikimedia.org/wikipedia/commons/b/b1/2-bit_resolution_analog_comparison.png" alt="2b" style="width:400px;"> | <img src="https://upload.wikimedia.org/wikipedia/commons/b/b7/3-bit_resolution_analog_comparison.png" alt="3b" style="width:400px;">


[Logic signal voltage levels](https://www.allaboutcircuits.com/textbook/digital/chpt-3/logic-signal-voltage-levels/)
---
- <img src="https://www.allaboutcircuits.com/uploads/articles/voltage-tolerance-of-ttl-gate-inputs.jpg" alt="2b" style="width:600px;">

p1

| level\truth | Positive logic | Negative logic |
| --- | --- | --- |
| high | true (1) | false (0) |
| low | false (0) | true (1) |


[Units of information](https://en.wikipedia.org/wiki/Units_of_information)
---
p7
| Unit | # of bits |  # of values representable | number ranges |
| --- | --- | --- | --- |
| bit | 1 | $2^1=2$ | 0, 1 |
| nibble | 4 | $2^4=16$ | 0, 1, 2, ..., 15 |
| byte | 8 | $2^8=256$ | 0, 1, 2, ..., 255 |
| word | 16 | $2^{16} = 65536$ | 0, 1, 2, ..., 65535 |
| dword | 32 | $2^{32} = 4294967296$ | 0, 1, 2, ...,  4294967295 |
| qword | 64 | $2^{64} = 18446744073709551616$ | 0, 1, 2, ..., 18446744073709551615 |


A vertical profile of a computer
---
p6
| layer | name |
| --- | --- |
| S | Applications |
| S | Programming languages and libraries |
| S | Operating systems |
| SH | Instruction set architecture (ISA) | 
| SH | Micro-architecture |
| `H` | `Register transfers` |
| `H` | `Logic gates` |
| P | Transistor circuits |

- S: software; SH: abstract layer between software and hardware
- H: hardware; P: physical entities 


# References
- [Analog-to-digital converter](https://en.wikipedia.org/wiki/Analog-to-digital_converter)
- [Quantization (signal processing)](https://en.wikipedia.org/wiki/Quantization_(signal_processing))
