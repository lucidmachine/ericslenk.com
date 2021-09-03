# Composition

Site content is laid out like so in the `content` subdirectory:

```
content
|-- config.edn    Cryogen configuration
|-- css           Custom CSS
|-- img           Images
|-- md
|   |-- pages     Pages defined in Markdown
|   `-- posts     Posts defined in Markdown
`-- static        Other static assets to be copied directly to the public directory
```

While developing the site's content it is useful to run a development server which re-compiles the
site as files are modified. The development server can be started with the following command:

```
clojure -X:serve
```


# Compilation

In order to compile the site contents from the `contents` and `themes` subdirectories to the `public`
subdirectory run the following command:

```
clojure -M:build
```
