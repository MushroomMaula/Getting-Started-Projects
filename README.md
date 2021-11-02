# About

This project contains various little tasks and projects I usually find helpful when learning a new programming language.

# Tasks

## Beginner
<details>
    <summary>Hello World</summary>

Display the string ` "Hello World!" `.
</details>
<details>
    <summary> Fizz Buzz </summary>

Write a function that takes a number `n` and displays every number up to this n.
If the number is divisible by 3 display `Fizz` instead, if the number is divisible by `5` display `Buzz`.
Example output for `n=10`:

```
1
2
Fizz
3
4
Buzz
Fizz
7
8
Fizz
Buzz
```
</details>

<details>
    <summary> Reverse a String </summary>

Write a functions that takes a string `s` and returns the reversed string
Example output for `s=abcd`:
```
dcba
```

</details>
<details>
    <summary> Check if a string is palindrome </summary>

Write a function that returns `1` if a given string is palindrome and `0` otherwise.
A string is palindrome iff reads the same backwards as forwards.
Lower-/uppercase should be ignored.
Example outputs for multiple inputs:
```
> otto
1
> Anna
1
> abcde
0
```

</details>
<details>
    <summary> Swap variable </summary>

Write a program that swaps the value of to integer variables.
For example let `a=3` and `b=6` before the function, then after calling the following should be true `a=6` and `b=3`.
```
a=3
b=6
swap(a, b)  # This is the exercise
assert a == 6 and b == 3
```


</details>
<details>
    <summary> Fibonacci Sequence </summary>

Write a program that outputs the `n`th fibonacci number.
The Fibonacci sequence is defined as follows:
```
Fib(0) = 1
Fib(1) = 1
Fib(n) = Fib(n-1) + Fib(n+1)      for n>1
```
Example output for `n=10`:


More [Information](https://oeis.org/A000045).

</details>
<details>
    <summary> Prime numbers to given n </summary>

Display all prime numbers up to a given number `n`.
A number is prime iff it is only divisible by and 1 and itself.
A simple algorithm is the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode).
Sample output for `n=20`:
```
2 3 5 7 11 13 17 19
```
</details>

<details>
    <summary> Switch string case </summary>
    
Write a programm that switches the case of a given string.
Example output for `s=Example String!`:
```
eXAMPLE sTRING!
```
Helpful information: [ascii table](https://www.lookuptables.com/text/ascii-table)

</details>


<details>
    <summary> Natural square root </summary>
    
For a given `n` find the last square of two [natural numbers](https://en.wikipedia.org/wiki/Natural_number) that is less than `n`.
For example for `n=10` the program should output `9`.
</details>

## Intermediate
<details>
    <summary> Square root </summary>
    
For a given `n` approximate the square root of the number using [newton's method](https://en.wikipedia.org/wiki/Newton%27s_method).
Observe that newton's method is used to find the roots of a function. Therefore we need a function `f` that is zero at the square root of `n`. This relationship can be explained by `f(x) = x^2-n`.
```
function squareroot(n, steps):
    x = n  # We start at n other starting points can also be used
    for i=1 to steps do:
        x = x - (x^2  - n) / 2*x

    return x
```

</details>

<details>
    <summary>IO-something</summary>
</details>
<details>
    <summary>Bubble sort</summary>
</details>
<details>
    <summary>Queue</summary>
</details>
<details>
    <summary>Tree</summary>
</details>
<details>
    <summary>Tic Tac Toe</summary>
</details>
<details>
    <summary>Karatsuba-Ofman Algorithm for multiplying two numbers</summary>
</details>
<details>
    <summary>A* Algorithm / Path finding algorithm</summary>
</details>
<details>
    <summary>IO-something</summary>
</details>
<details>
    <summary>Conways game of life</summary>
</details>


## Advanced
<details>
    <summary>Finite State Machine</summary>
</details>
<details>
    <summary>Tokenizer/Lexer Interpreter</summary>
</details>