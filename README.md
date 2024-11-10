__Binary Number:__ has only 1s and 0s
- Rightmost bit (binary digit) is 2^0, and the power raises for every digit, just like in decimal system

How Binary Works:
- _Example (Least Significant Bit to Most Significant Bit):_
- 110001010
- 0x2^0 + 1x2^1 + 0x2^2 + 1x2^3 + 0x2^4 + 0x2^5 + 0x2^6 + 1x2^7 + 1x2^8 = 2 + 8 + 128 + 256 = 394

__Decimal to Binary:__ Divide the number to two. Take note of the remainder for each. Keep going until answer becomes zero. (Most Significant Bit to Least Significant Bit)
- _Example:_
- 394/2 = 197r0; 197/2 = 98r1; 98/2 = 49r0; 49/2 = 24r1; 24/2 = 12r0; 12/2 = 6r0; 6/2 = 3r0; 3/2 = 1r1; 1/2 = 0r1; 110001010
