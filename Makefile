.PHONY: all serve serve-fast lint-clj lint-scss build

all: build

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
