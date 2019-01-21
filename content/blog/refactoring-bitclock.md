Title: Refactoring Bitclock
Date: 2019-01-21
Category: 
Tags: bitclock, refactoring, javascript, projects 
Summary: Half a decade ago I made a humble little widget named bitclock to practice reading binary. I've rearchitected bitclock to begin porting it to meatspace.
Status: published

<iframe src="https://lucidmachine.github.io/bitclock/" style="border: none; height: 150px"></iframe>

# What is Bitclock?
Half a decade ago I made a humble little widget named [bitclock](https://lucidmachine.github.io/bitclock/) to practice reading binary integers (bits). It's embedded above for demonstration, or you can view it on [its Github Pages site](https://lucidmachine.github.io/bitclock/). You can check out its code at [the project's Github repository](https://github.com/lucidmachine/bitclock). Bitclock's original implementation was a 4x4 grid of bits in which each column represented a digit of the current time, and each row represented a place value in the digit. It renders on a webpage and dynamically updates that page's favicon.

![Interpretation of Bitclock](https://lucidmachine.github.io/bitclock/img/interpretation.png)

# Why refactor Bitclock?
While I still enjoy it an awful lot I've begun to wish it existed in more places. I'd love to build a hardware version, and might like to port it to mobile platforms, a command-line interface, etc. Plus, I've always wanted to add more display features e.g. configurable colors and sizes, optional second or microsecond precision, timezones, multiple clocks on a page, etc. It should also be useful as a reference problem to compare technology stacks. One could make an implementation in AngularJS and an implementation in Angular 7 to compare and contrast functionality between the two stacks.

# How has it been refactored?
Today I finally wrote a proper README for bitclock which formalizes its data structures. I've also defined a frontend/backend architecture for it. Loosely, a backend is anything which spits out a BitTime, and a frontend is anything that can turn a BitTime into user-interpretable output. The reference code itself has been rewritten to those specifications and split up by transformation stage. 

# What's next?
The very next step is refactoring to use more modern JS conventions such as modularization and maybe some build tools. Once the application is properly modularized it will be ported to the Raspberry Pi Zero with GPIO using Node.js and to an Angular 7 based webapp.

