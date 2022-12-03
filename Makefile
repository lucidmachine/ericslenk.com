.PHONY: all serve serve-fast lint-scss build

all: build

serve:
	clojure -X:serve

serve-fast:
	clojure -X:serve-fast

lint-scss:
	fd '.scss' | xargs npx stylelint

build:
	clojure -M:build
