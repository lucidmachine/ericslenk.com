Title: TypeScript on an Arduino with Johnny-Five
Date: 2019-04-22
Category:
Tags: johnny-five, arduino, typescript
Summary: 
Status: published

Are you proficient in [TypeScript](http://typescriptlang.org/) and want to dip your toes in microcontrollers? Missing your favorite IDE? Want a REPL for your robot? Let's get some TypeScript running on your [Arduino](https://www.arduino.cc/) with [Johnny-Five](http://johnny-five.io/)!

# TypeScript Toolchain
First thing's first, let's set up our TypeScript toolchain.

```javascript
// package.json
{
  .
  .
  .
  "main": "build/main/index.js",
  "typings": "build/main/index.d.ts",
  "scripts": {
    "build": "run-s clean && run-p build:*",
    "build:main": "tsc -p tsconfig.json",
    "clean": "trash build test"
  },
  "engines": {
    "node": ">=10.15.0"
  },
  "devDependencies": {
    "npm-run-all": "^4.1.5",
    "trash-cli": "^1.4.0",
    "typescript": "^3.4.2"
  }
```

In `package.json` we'll require the TypeScript compiler and a couple scripting utilities, define our build and clean scripts, declare our entry point as `build/main/index.js`, and specify a target Node.js version.

```javascript
// tsconfig.json
{
  "compilerOptions": {
    "target": "es2017",
    "outDir": "build/main",
    "rootDir": "src",
    "moduleResolution": "node",
    "module": "commonjs",
    "lib": ["es2017"],
    "types": ["node"],
    "typeRoots": ["node_modules/@types", "src/types"]
  },
  "include": ["src/**/*.ts"],
  "exclude": ["node_modules/**"]
}
```

In `tsconfig.json` we'll tell the TypeScript compiler that our source code is in the `src/` directory and that it should be transpiled to ES2017 and output in the directory `build/main`.

Now let's get that all installed.

```
> npm install
```

# Johnny Five
Now we need to install the Johnny Five package and its TypeScript types.

```
> npm install johnny-five @types/johnny-five
```

Pretty easy.

# Hello, World!
Now let's set up a simple test. We're going to translate [the Johnny Five Hello World example](http://johnny-five.io/examples/#hello-world-see-more-) to TypeScript. First, let's set up the hardware. Plug a single LED into your board with the anode (long end, positive) in I/O pin 13 and the cathode (short end, negative) in the GROUND pin. Now open up the file `src/index.ts` and write the following:

```typescript
// src/index.ts
#!/usr/bin/env node

import { Board, Led } from 'johnny-five';


const board = new Board();

board.on('ready', () => {
    const led = new Led(13);
    led.blink(500);
});
```

With the Johnny Five types package we're able to import the `Board` and `Led` types as expected in TypeScript, no muss, no fuss. Then we simply instantiate a Board and write an anonymous function to handle its 'ready' event. We define an Led on I/O pin 13 and instruct that LED to blink every 500ms. Let's build this sucker!

```
> npm run build
> tree build
build
└── main
    └── index.js
```

Oooooo we've got something! Now connect the board to your computer and run that program!

```
node build/main/index.js
```

![LIIIIIIIIIIIFE!](https://rachaelcorbin.files.wordpress.com/2017/04/636206370165002514-707932019_gif-4.gif?w=820)


# REPL
Okay, so you can flash a TypeScript program to your board now and that's pretty neat but what if you had a Read Evaluate Print Loop (REPL), too?! Like you could just send commands to the board or read info from the board at *runtime*?!?!

```typescript
// src/index.ts
#!/usr/bin/env node

import { Board, Led } from 'johnny-five';


const board = new Board();

board.on('ready', () => {
    const led = new Led(13);

    board.repl.inject({
        led: led
    });
});
```

```
> npm run build
> node build/main/index.js
1555900146160 Available /dev/ttyACM0
1555900146178 Connected /dev/ttyACM0
1555900149946 Repl Initialized
>> 
```

Well you heckin' **CAN**! That code up there set up a REPL and passed your LED in to that REPL, so you can read debug information about your LED.

```
>> led
Led {
  board:
   Board {...},
  io:
   Board {...},
  id: '2253A374-ED4C-4D11-83B0-88C3BCA66C18',
  custom: {},
  pin: 13 }
```

And you can turn your LED on.

```
>> led.on();
```

Or turn it back off.

```
>> led.off();
```

Or set it to strobe!

```
>> led.strobe(1000);
```

Even strobier!!

```
>> led.strobe(500);
```

** DONE.**
