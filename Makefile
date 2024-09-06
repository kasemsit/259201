buildall:
	jupytext --to notebook modules/module02.md modules/module02.ipynb
	jupyter-book build --all ./
build:
	jupyter-book build ./	
clean:
	rm -rf _build/
	jupyter-book clean ./ --all
deploy:
	ghp-import -n -p -f _build/html