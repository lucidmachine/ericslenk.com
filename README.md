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
make serve
```


# Compilation

In order to compile the site contents from the `contents` and `themes` subdirectories to the `public`
subdirectory run the following command:

```
make build
```


# Publication

In order to publish the compiled site contents from the `public` subdirectory to a remote host via
rsync run the following commands:

```bash
LOCAL_SRC_DIR=public/
REMOTE_HOST=ssh.phx.nearlyfreespeech.net
REMOTE_PORT=22
REMOTE_USER=lucidmachine_ericslenk
REMOTE_TARGET_DIR=/home/public
rsync \
  --checksum \
  --compress \
  --delete \
  --partial \
  --progress \
  --recursive \
  --rsh="ssh -p ${REMOTE_PORT}" \
  --verbose \
  "${LOCAL_SRC_DIR}" \
  "${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_TARGET_DIR}"
```
