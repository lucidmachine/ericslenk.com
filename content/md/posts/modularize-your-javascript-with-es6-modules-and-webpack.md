{:title "Modularize Your JavaScript with ES6 Modules and Webpack", :date "2019-01-28", :tags ["es6" "modules" "webpack" "bitclock" "javascript" "js"], :description "Do you have a bunch of old JavaScript code that's harder to look at than Ted Cruz's face? Try ES6 Modules today!"}

Do you have a bunch of old JavaScript code that's [harder to look at than Ted Cruz's face](https://www.psychologytoday.com/us/blog/the-fallible-mind/201601/why-ted-cruz-s-facial-expression-makes-me-uneasy)? Or maybe you're looking for some way to keep your shiny new project from devolving into the utter chaos to which your last project succumbed? Friend, have I got a miracle cure for you! Try ES6 Modules today! 

# Why Modules?
Modules are just little self-contained chunks of your program. Small, self-contained code is easier to reason about and simpler to maintain, debug, and write. You can read a single module much more quickly than an entire code base, and if its boundaries have been set in juuuust the right places you might not have to read anything from outside of that module in order to understand what it's doing. Self-contained modules also lend themselves to reuse and composition into higher-level applications.

# Determining Module Boundaries
Now that you're convinced that modules will solve all of your problems forever you may wonder, "just how *do* I modularize my code?" Excellent question. Nobody knows! But these guidelines might help:

* Do as **few things** as possible. If you can get the number down to 1 you're doing really well, and if you get the number down to 0 you can just delete the module and you win at Programming.
* Talk with as **few other modules** as possible. Modules are hermits.
* **Combine** modules which **always talk to each other** to get anything done. That'll shut 'em up.
* **Do not look inside** of another module. That's just rude.

# Writing ES6 Modules
These days modules are a standard part of vanilla JavaScript. You can go read the [ES6 specification for modules](https://www.ecma-international.org/ecma-262/6.0/#sec-modules) if you're curious, but don't. To get started you just need to learn to use a couple of statements in your JS files.

## export
Use the `export` statement at the end of a module file to say which parts of your code the rest of the world may use. There are an awful lot of ways you can write this (see the [the MDN article on export](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export#Syntax) for details), but `export { name1, name2, …, nameN };` will usually suffice. In Bitclock the backend module looks like this:

```javascript
// bitclock-backend.js

// ...
const placeValues = [8, 4, 2, 1];

const isBitActive = (placeValue, digit) =>
    (placeValue & digit) > 0;

const bitDigit = digit =>
    placeValues
        .map(placeValue =>
            isBitActive(placeValue, digit) ?
                1 :
                0);

const bitTime = date =>
    timeAsDigits(date)
        .map(digit =>
            bitDigit(digit));

const getCurrentBitTime = () =>
    bitTime(new Date());

export { bitDigit, bitTime, getCurrentBitTime };
```

The rest of the world is allowed to use just 3 of the many functions defined in our backend module. Any code which imports this can create a BitDigit from a given digit, create a BitTime from a given time, or get a BitTime for the current time.

## import
Use the `import` statement at the beginning of a module file to say which parts of which other modules your module may use. Import statements will often look like `import { export1 , export2 } from "module-name";`. Like the export statement, there are also a boatlod of ways to write an import statement outlined in the [MDN article on import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import). In Bitclock our top-level module looks like this:

```javascript
// index.js

import { getCurrentBitTime } from "./js/bitclock-backend";
import { updateClockDivs } from "./js/bitclock-frontend-dom";
// ...

const update = () => {
    const currentBitTime = getCurrentBitTime();

    updateClockDivs(currentBitTime);
    // ...
};
// ...
```

Here the top-level code has imported just 1 of the 3 functions exported from the backend module and a function from the DOM rendering frontend module and combined those functions into a function which updates the DOM rendering frontend with the current BitTime retrieved from the backend.

# Using your Modules with Webpack
Splitting your code up into a bunch of little JS files which import each other is only, like, half the battle, and the other half isn't "knowing." You must now **somehow** get all of those modules into an appication to **do** something. At the time of writing [less than 80% of browsers support loading JS modules via the script tag](https://caniuse.com/#feat=es6-module), so I'd avoid doing so for now. Plus, you'll have to contend with [CORS policies regarding local files](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS/Errors/CORSRequestNotHttp?utm_source=devtools&utm_medium=firefox-cors-errors&utm_campaign=default) if you do, and that's a bummer. Instead, let's install an assload of tools and restructure our project! We're going to use [Webpack](https://webpack.js.org/) to bundle our modularized application. Webpack neatly circumvents those problems and [gets rid of unnecessary code](https://webpack.js.org/guides/tree-shaking/) to boot. Much better!

## Installing NPM via NVM
In order to use Webpack we're going to need NPM. If you have a current version of NPM, move on. Otherwise, install Node Version Manager (NVM) and then use it to install the latest stable version of Node.js and NPM.

```
$ curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash
$ nvm install node
$ nvm use node
```

## Restructuring Your Project
From here on out we'll be building our application distribution from source using Webpack, so we should structure our project's directories and files to reflect that and to minimize the amount of Webpack configuration we'll have to do later.

### src/ and dist/
If your source files weren't in their own directory before, make it so. Create the directory `src/` and move your JS and anything else that will need to be built by Webpack in here. The JS file which will serve as your entry point should be moved in here as well. Webpack expects `src/index.js` by default, so let's use that.

```
src/
├── index.js
└── js
    ├── bitclock-backend.js
    ├── bitclock-frontend-canvas.js
    ├── bitclock-frontend-dom.js
    └── bitclock-frontend-favicon.js

```

Now let's make our distribution directory, `dist/`, and place in it anything that will be distributed to end users without being built first. Things like CSS stylesheets or static image assets belong in here. This should also contain your HTML entry point. We'll place it at `dist/index.html`.

```
dist/
├── css
│   └── clock.css
└── index.html

```

### package.json
Now we'll need to create or update your project's package specification. Use NPM's init wizard in your project's top-level directory to bootstrap your `package.json` file if you don't already have one.

```
$ npm init
```

New open up `package.json` and add a few utility scripts for later.

```json
  "scripts": {
    "build": "webpack",
    "clean": "rm -rf node_modules && rm dist/main.js",
    "reinstall": "npm run clean && npm install",
    "rebuild": "npm run clean && npm install && npm run build"
  },
```

### index.html
Finally, you'll need to modify your HTML entry point to pull in the bundle which Webpack will build.

```html
<!-- index.html -->

<!-- ... -->
  <script src="main.js"></script>
</body>
<!-- ... -->
```

## Webpack
Now that you've prepared your project for Webpack it's time to get installing! So exciting! Run the following to add Webpack and its CLI as development dependencies to your project.

```
$ npm install --save-dev webpack webpack-cli
```

Hot damn that's a lot of Webpack! Now let's finally *do* something with it. The build script that we added to our `package.json` file will use Webpack's CLI to run Webpack against our `src/` directory and compile our modularized JavaScript into the big old JS file, `dist/main.js`, which `dist/index.html` is expecting.

```
$ npm run-script build

> bitclock@1.0.0 build /home/lucidmachine/src/bitclock
> webpack

Hash: b1f1afb47ea5ff1a1965
Version: webpack 4.29.0
Time: 173ms
Built at: 01/28/2019 8:46:58 PM
  Asset      Size  Chunks             Chunk Names
main.js  1.96 KiB       0  [emitted]  main
Entrypoint main = main.js
[0] ./src/index.js + 4 modules 3.42 KiB {0} [built]
    | ./src/index.js 453 bytes [built]
    | ./src/js/bitclock-backend.js 797 bytes [built]
    | ./src/js/bitclock-frontend-dom.js 572 bytes [built]
    | ./src/js/bitclock-frontend-canvas.js 1.34 KiB [built]
    | ./src/js/bitclock-frontend-favicon.js 302 bytes [built]
```

Ooooooo something happened!

```
.
├── dist
│   ├── css
│   │   └── clock.css
│   ├── index.html
│   └── main.js
├── package.json
├── package-lock.json
└── src
    ├── index.js
    └── js
        ├── bitclock-backend.js
        ├── bitclock-frontend-canvas.js
        ├── bitclock-frontend-dom.js
        └── bitclock-frontend-favicon.js
```
![OH YEAH!!!](https://media.giphy.com/media/VRa3YCyi3JSWk/giphy.gif)


**DONE.**