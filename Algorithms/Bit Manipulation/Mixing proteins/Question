Some scientists are working on protein recombination, and during their research, they have found a remarkable fact: there are 4 proteins in the protein ring that mutate after every second according to a fixed pattern. For simplicity, proteins are called  (you know, protein names can be very complicated). A protein mutates into another one depending on itself and the protein right after it. Scientists determined that the mutation table goes like this:

    A   B   C   D
    _   _   _   _
A|  A   B   C   D
B|  B   A   D   C
C|  C   D   A   B
D|  D   C   B   A
Here rows denote the protein at current position, while columns denote the protein at the next position. And the corresponding value in the table denotes the new protein that will emerge. So for example, if protein i is A, and protein i + 1 is B, protein i will change to B. All mutations take place simultaneously. The protein ring is seen as a circular list, so last protein of the list mutates depending on the first protein.

Using this data, they have written a small simulation software to get mutations second by second. The problem is that the protein rings can be very long (up to 1 million proteins in a single ring) and they want to know the state of the ring after upto  seconds. Thus their software takes too long to report the results. They ask you for your help.

Input Format

Input contains 2 lines.
First line has 2 integers  and ,  being the length of the protein ring and  the desired number of seconds.
Second line contains a string of length  containing uppercase letters ,,  or  only, describing the ring.

Constraints



Output Format

Output a single line with a string of length , describing the state of the ring after  seconds.

Sample Input 0

5 15
AAAAD
Sample Output 0

DDDDA
Explanation 0

The complete sequence of mutations is:

AAADD
AADAD
ADDDD
DAAAD
DAADA
DADDD
DDAAA
ADAAD
DDADD
ADDAA
DADAA
DDDAD
AADDA
ADADA
DDDDA
