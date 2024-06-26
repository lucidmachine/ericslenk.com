.PHONY: all clean serve serve-fast lint-clj lint-scss lint build publish

all: build

clean:
	rm -rf public

serve:
	clojure -X:serve

serve-fast:
	clojure -X:serve-fast

lint-clj:
	clj-kondo --lint .

lint-scss:
	fd '.scss' | xargs npx stylelint

lint: lint-clj lint-scss

build:
	clojure -M:build

publish:
	rsync \
		--checksum \
		--compress \
		--delete \
		--partial \
		--progress \
		--recursive \
		--rsh='ssh -p 22' \
		--verbose \
		'public/' \
		'lucidmachine_ericslenk@ssh.nyc1.nearlyfreespeech.net:/home/public'
