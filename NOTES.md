# Various notes during development

## Opens image using XDG
*Must* warn user about large rendering. How can I detect this? 
~~~sh
$ corg view stuff.json 
$ corg view stuff.json -o output.png
~~~

## Prints to terminal
Perhaps use the same output style as `tree`?
~~~sh
$ corg print stuff.json
$ corg table stuff.json #<-- col:operators row:res
~~~

## Filter by cluster operator name
~~~sh
$ corg print stuff.json -f authentication
~~~

## TODO Filter by resource
~~~sh
$ corg print stuff.json -f group=config.openshift.io
$ corg print stuff.json -f resource=namespaces,name=openshift-ingress
~~~