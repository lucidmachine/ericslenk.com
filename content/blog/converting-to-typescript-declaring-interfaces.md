Title: Converting to TypeScript: Declaring Interfaces
Date: 2019-02-18
Category: 
Tags: typescript, ts, definitions, interfaces, types, javascript, js, bitclock
Summary: Now that you're set up, start *using* TypeScript. With types and stuff!
Status: published

Hey nerds. Now that you've [modularized your project with ES6 and Webpack]({filename}/blog/modularize-your-javascript-with-es6-modules-and-webpack.md) and [set up a toolchain to transpile TypeScript to JavaScript]({filename}/blog/converting-to-typescript-toolchain.md) you should start *using* TypeScript. With types and stuff!

# The Declaration File
Your library's types should live in a declaration file, so let's make one and get cracking! Where do we put this thing? What do we call it? The [TypeScript docs on library structures](https://www.typescriptlang.org/docs/handbook/declaration-files/library-structures.html) have a lot of suggestions, but you'll probably be interested in one of three cases.

Suppose you're writing a really awesome module named "rad", and you import it like `const rad = require('rad');`.

* If your module will be called as a function like `rad('yeah');`, name it `rad/module-function.d.ts` and use [the module-function.d.ts template](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-function-d-ts.html).
* If your module will be constructed as a class using `new ` like `let woo = new rad('yeah');`, name it `rad/module-class.d.ts` and use [the module-function.d.ts template](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-function-d-ts.html)
* If neither of the above apply, name it `rad/module.d.ts` and use [the module.d.ts template](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-d-ts.html)

# Interfaces
What exactly goes in that declaration file? Interfaces! So. Many. Interfaces. From the docs:

> One of TypeScript’s core principles is that type-checking focuses on the shape that values have. ... In TypeScript, interfaces fill the role of naming these types, and are a powerful way of defining contracts within your code as well as contracts with code outside of your project.

TypeScript has a lot of kinds of interfaces and plenty of ways to define those interfaces, but to start we'll focus on two extremely versatile kinds of interfaces that get stuff done.

## Object Interfaces
An object interface is a description of the shape of an object. You can describe which properties should exist on an object which conforms to the interface, what the types of those properties are, and which of those properties are required or optional. For example, let's say we want to greet some chump. Among other things, chumps have names - usually a couple, sometimes more. We might start with a function that looks a bit like this.

```typescript
// index.ts
const rudeGreeting = (victim) =>
    `Get lost, ${victim.name}!`;

console.log(rudeGreeting({name: 'Steve'}));
// > "Get lost, Steve!"
```

That seems fine at first blush. The trouble is, we're assuming that `victim` *has* a `name`.

```typescript
// index.ts
const rudeGreeting = (victim) =>
    `Get lost, ${victim.name}!`;

console.log(rudeGreeting(false));
// > "Get lost, undefined!"
```

That's a bug. We could write some more code to check whether our `victim`'s got a `name`, and to specify how the function should behave if our `victim` *doesn't* have a `name`. Or we can lean on TypeScript's compiler to ensure that whatever makes it into our function definitely has a `name`. We'll define an interface for chumps and require that anything passed into our greeting function is an object which conforms to that chump interface.

```typescript
// module.d.ts
interface Chump {
    givenName: string;
    middleNames: string[];
    familyName: string;
    nickName?: string;
}

// index.ts
import {Chump} from 'rad';

const rudeGreeting = (victim: Chump) =>
    `Get lost, ${victim.nickName || victim.givenName}!`;

const steve = {
    givenName: "Steven",
    middleNames: [],
    familyName: "Chumpsworth",
    nickName: "Steve",
    isAwful: true
    
};

console.log(rudeGreeting(steve));
// > "Get lost, Steve!"

console.log(rudeGreeting(false));
// > Argument type boolean is not assignable to parameter type Chump
```

Heck yeah! When we gave it a properly formed victim everything worked out fine. And when we gave it some invalid crap, the compiler yelled at us! Much better!

## Function Interfaces
A function interface is a description of the shape of a function. You can describe what parameters a function should take and what type of data it should return by using a function interface. For example, let's write a second chump greeting function.


```typescript
// module.d.ts
interface Chump {
    givenName: string;
    middleNames: string[];
    familyName: string;
    nickName?: string;
}

interface GreetingFunc {
    (victim: Chump): string
}


// index.ts
import {Chump, GreetingFunc} from 'rad';


const rudeGreeting: GreetingFunc = (victim: Chump) =>
    `Get lost, ${victim.nickName || victim.givenName}!`;

const politeGreeting: GreetingFunc = (victim: Chump) => {
    const fullName = [
        victim.givenName, 
        ...victim.middleNames, 
        victim.familyName]
        .join(' ');
    return `Salutations, ${fullName}!`;
};

const metaGreeting = (victim: Chump & {isAwful: boolean}) =>
    victim.isAwful ?
        rudeGreeting(victim) :
        politeGreeting(victim);


const steve = {
    givenName: "Steven",
    middleNames: [],
    familyName: "Chumpsworth",
    nickName: "Steve",
    isAwful: true
};

const phyllis = {
    givenName: "Phyllis",
    middleNames: ["Rose", "Dandellion"],
    familyName: "Herpingderp",
    isAwful: false
};

console.log(metaGreeting(steve));
// > "Get lost, Steve!"

console.log(metaGreeting(phyllis));
// > "Salutations, Phyllis Rose Dandellion Herpingderp!"
```

You can see that both `rudeGreeting()` and `politeGreeting()` were defined as implementing our function interface, `GreetingFunc`. For a bit of bonus fun, we've defined a third function, `metaGreeting()`, which takes a objects which conform to the Chump interface *and also* have a boolean property named `isAwful` by using [Intersection Types](https://www.typescriptlang.org/docs/handbook/advanced-types.html#intersection-types). Read up on it, that's cool as heck.

**DONE.**