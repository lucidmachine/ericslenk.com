# Setup
In order to set up the Pelican environment, use pip to install the Pelican package and optional dependency packages Markdown, py_w3c, and yuicompressor.

```
sudo pip3 install Pelican Markdown HTMLParser markup
```

# Composition
Site content is stored in the ```content/``` directory. The directory ```content/blog/``` contains blog articles in Markdown. The directory ```content/pages/``` contains static pages in Markdown. The directory ```content/images/``` contains static images.

# Development
## Development Server
While developing the site's templates and assets it is useful to run a development server which re-compiles the site as files are modified. The development server can be started with the following command.
```
make devserver
```
When you are finished developing, stop the server with the following command.
```
make stopserver
```

# Compilation
In order to generate the site contents based on your composed content and developed files and templates run the following command.
```
make html
```

# Publication
In order to generate and rsync the site to your website run the following command.
```
make rsync_upload
```
