Title: Converting to TypeScript: Declaring Interfaces and Types
Date: 2019-02-12
Category: 
Tags: typescript, ts, definitions, types, interfaces, javascript, js, bitclock
Summary: []
Status: draft

Now that you're set up to write TypeScript you need to actually write some actual TypeScript. With types and stuff.

This article assumes that your project is modularized and compiles from TypeScript to JavaScript. If you're not quite there yet check out [Modularize Your JavaScript with ES6 and Webpack]({filename}/modularize-your-javascript-with-es6-and-webpack.md) and [Converting to TypeScript: Toolchain]({filename}/converting-to-typescript-toolchain.md).

# The Declaration File
So where do you even start? If you want to add types to your code, you want a declaration file. Declaration files contain the type declarations for a library. The [TypeScript docs on library structures](https://www.typescriptlang.org/docs/handbook/declaration-files/library-structures.html) have a lot of suggestions as to where this file goes and what you should call it, but you'll probably be interested in one of three things.

Suppose you're writing a really awesome module named "rad".

* If your module will be called like a function like `var rad = require('rad'); rad('yeah');`, name it `rad/module-function.d.ts` and use [the module-function.d.ts template](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-function-d-ts.html).
* If your module will be constructed as a class using `new ` like `var rad = require('rad'); var woo = new rad('yeah');`, name it `rad/module-class.d.ts` and use [the module-function.d.ts template](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-function-d-ts.html)
* If neither of the above apply, name it `rad/module.d.ts` and use [the module.d.ts template](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-d-ts.html)

# Interfaces
What goes in that declaration file? Interfaces! So. Many. Interfaces. From the docs:

> One of TypeScript’s core principles is that type-checking focuses on the shape that values have. ... In TypeScript, interfaces fill the role of naming these types, and are a powerful way of defining contracts within your code as well as contracts with code outside of your project.

There are many kinds of interfaces and ways to define those interfaces, but we'll focus on two extremely versatile interfaces for brevity.

## Object Interfaces
An object interface is a description of the shape of an object.

## Function Interfaces
A function interface is a description of the shape of a function.

# Types
