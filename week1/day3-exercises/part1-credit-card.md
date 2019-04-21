## Bank Part 1 - Credit Card

#### The assignment

* We will be using the [Luhn Algorithm](http://en.wikipedia.org/wiki/Luhn_algorithm) to verify credit card numbers.

* The assignment is to prompt for a credit card number and determine the validity and type of the card.

* * Here is a test value: 347650202246884. It is a valid Amex. There are more online.

* The second part of the assignment is to devise a scheme to generate new valid values.

### The algorithm

#### Card type and length

* Visa must start with 4

* Mastercard must start with 51, 52, 53, 54 or 55

* AMEX must start with 34 or 37

* Discover must start with 6011

* Visa, MC and Discover have 16 digits

* AMEX has 15 digits

* * You already know a card is invalid if it is the wrong length or isn't any type. You can go ahead and say so and use quit() to exit the program without the rest of the test.

#### The Luhn Algorithm

* From the right most digit, double the value of every second digit. For example:

`4 4 8 5 0 4 0 9 9 3 2 8 7 6 1 6`

becomes

`8 4 16 5 0 4 0 9 18 3 4 8 14 6 2 6`

* Now, sum all the individual digits together. That is to say, split any numbers with two digits into their individual digits and add them. Like so:

`8 + 4 + 1 + 6 + 5 + 0 + 4 + 0 + 9 + 1 + 8 + 3 + 4 + 8 + 1 + 4 + 6 + 2 + 6`

* Now take the sum of those numbers and modulo 10.

* 80 % 10

* If the result is 0, the credit card number is valid.

