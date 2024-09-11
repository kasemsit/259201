JUPYTERBOOK = jupyter-book
JUPYTEXT = jupytext
MARKDOWN_DIR = md
NOTEBOOK_DIR = notebook

all: jupytext buildall

jupytext:
	mkdir -p $(NOTEBOOK_DIR)
	$(JUPYTEXT) --set-formats $(NOTEBOOK_DIR)//ipynb,$(MARKDOWN_DIR)//md --sync $(MARKDOWN_DIR)/*.md

buildall:
	$(JUPYTERBOOK) build --all ./

build:
	$(JUPYTERBOOK) build ./

clean:
	rm -rf _build/ notebook/
	$(JUPYTERBOOK) clean ./ --all

deploy:
	ghp-import -n -p -f _build/html