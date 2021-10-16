{:title "Converting to TypeScript: Toolchain"
 :date "2019-02-04"
 :tags ["typescript" "toolchain" "webpack" "javascript" "bitclock"]
 :description "Upgrade your project's toolchain to build TypeScript alongside JavaScript."}

This article assumes that your project is already built using Webpack and structured in a standard
way. If your project doesn't use Webpack yet check out [Modularize Your JavaScript with ES6 and
Webpack](/posts/modularize-your-javascript-with-es6-modules-and-webpack).

# Install TypeScript Toolchain
To get started get yourself the TypeScript compiler, the TypeScript loader for Webpack, and a
TypeScript linter plugin for ESLint.

```text
$ npm install --save-dev typescript ts-loader tslint @typescript-eslint/eslint-plugin-tslint
```

# Configure TypeScript Compiler
Next you need to tell the TypeScript compiler how to do its job. Computers sure are dumb. Create the
file `tsconfig.json` in your project's top-level directory and add the following.

```javascript
// tsconfig.json

{
  "compilerOptions": {
    "outDir": "./dist/",
    "sourceMap": true,
    "noImplicitAny": true,
    "module": "es6",
    "allowJs": true,
    "moduleResolution": "node"
  }
}
```

This tells the TypeScript compiler take your TypeScript and JavaScript files as input and output ES5
JavaScript with [source
maps](https://developer.mozilla.org/en-US/docs/Tools/Debugger/How_to/Use_a_source_map) so that your
browser will run the equivalent ES5 code but let you debug the corresponding TypeScript source.

The last line tells the compiler to look for modules in the same way that Node.js does. This isn't
strictly necessary, but some development tools which analyze your code and assume this resolution
strategy might benefit here. See the [TypeScript documentation on module resolution
strategies](https://www.typescriptlang.org/docs/handbook/module-resolution.html#classic) for
details.

# Reconfigure Webpack
Now you need to configure Webpack to run the TypeScript compiler when building your project. If you
don't already have a file `webpack.config.js` in your project's top-level directory, create it and
add the following.

```javascript
// webpack.config.js

const path = require('path');

module.exports = {
    entry: './src/index.ts',
    devtool: 'inline-source-map',
    module: {
        rules: [
            {
                test: /\.ts$/,
                use: 'ts-loader',
                include: /src/,
                exclude: /node_modules/
            }
        ]
    },
    resolve: {
        extensions: ['.ts', '.js']
    },
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname, 'dist')
    }
};
```

This tells Webpack to build your project starting with the entry point `src/index.ts` and output the
result at `dist/main.js`. Any files with extensions '.ts' or '.js' will be picked up. That module
rule tells Webpack that any file in the `src/` directory with a '.ts' extension should be built
using ts-loader, which runs the TypeScript compiler against those files.


# index.ts
Now to convert your entry point, `index.js`, to TypeScript. This is the easy part. Rename the file
to `index.ts`. That's it! Build your project and see for yourself!

```text
$ npm run rebuild

...

Version: webpack 4.29.0
Time: 1663ms
Built at: 02/03/2019 1:16:46 PM
  Asset      Size  Chunks             Chunk Names
main.js  15.8 KiB       0  [emitted]  main
Entrypoint main = main.js
[0] ./src/index.ts + 4 modules 3.42 KiB {0} [built]
    | ./src/index.ts 452 bytes [built]
    | ./src/js/bitclock-backend.js 797 bytes [built]
    | ./src/js/bitclock-frontend-dom.js 572 bytes [built]
    | ./src/js/bitclock-frontend-canvas.js 1.34 KiB [built]
    | ./src/js/bitclock-frontend-favicon.js 302 bytes [built]
```

**DONE.**
