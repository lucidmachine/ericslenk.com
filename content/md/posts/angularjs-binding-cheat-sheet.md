{:title "AngularJS Binding Cheat Sheet", :date "2019-01-13", :tags ["AngularJS" "binding" "isolate scope" "cheat sheet"], :description "A quick guide for AngularJS isolate scope binding syntax."}

| Syntax     | Value                          | Direction  | Evaluated | Aliased? | Optional? |
|------------|--------------------------------|------------|-----------|----------|-----------|
| foo: @     | Value of DOM attribute         | Out  -> In | Out       | No       | No        |
| foo: @?    | Value of DOM attribute         | Out  -> In | Out       | No       | Yes       |
| bar: @foo  | Value of DOM attribute         | Out  -> In | Out       | Yes      | No        |
| bar: @?foo | Value of DOM attribute         | Out  -> In | Out       | Yes      | Yes       |
| foo: =     | Expression passed by attribute | Out <-> In | In        | No       | No        |
| foo: =?    | Expression passed by attribute | Out <-> In | In        | No       | Yes       |
| bar: =foo  | Expression passed by attribute | Out <-> In | In        | Yes      | No        |
| bar: =?foo | Expression passed by attribute | Out <-> In | In        | Yes      | Yes       |
| foo: <     | Expression passed by attribute | Out  -> In | In        | No       | No        |
| foo: <?    | Expression passed by attribute | Out  -> In | In        | No       | Yes       |
| bar: <foo  | Expression passed by attribute | Out  -> In | In        | Yes      | No        |
| bar: <?foo | Expression passed by attribute | Out  -> In | In        | Yes      | Yes       |
| foo: &     | Value passed by attribute      | Out <-  In | Out       | No       | No        |
| foo: &?    | Value passed by attribute      | Out <-  In | Out       | No       | Yes       |
| bar: &foo  | Value passed by attribute      | Out <-  In | Out       | Yes      | No        |
| bar: &?foo | Value passed by attribute      | Out <-  In | Out       | Yes      | Yes       |