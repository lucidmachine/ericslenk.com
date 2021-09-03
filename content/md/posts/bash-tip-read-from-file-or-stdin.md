{:title "Bash Tip: Read From File or STDIN", :date "2020-07-18", :tags ["bash" "file" "stdin"], :description "A quick bash snippet to read from a given file or else STDIN."}

```bash
# Usage:
#   script.sh foo.txt > foo_but_better.txt
#   cat bar.txt | tr '[:lower:]' '[:upper:]' | script.sh > BAR_BUT_BETTER.txt
  
cat ${1:--} \
  | sed -e 's/pipe/line/g'
```

Sometimes I write a bash script that needs to play nicely in the middle of a pipeline, but it would also be nice to use it at the front of the pipeline or on its own. This snippet says, "cat whatever the first parameter is, or if there's no first parameter, then cat the content of STDIN".

**DONE.**