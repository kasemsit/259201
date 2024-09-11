# 259201

Convert ipynb to myst 
```console
 jupytext <file.ipynb> --to myst
```

Build the book
```
jupyter-book build --all .
```

Update the book's website
```
ghp-import -n -p -f _build/html
```