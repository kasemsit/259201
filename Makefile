buildall:
	jupyter-book build --all ./
build:
	jupyter-book build ./	
clean:
	rm -rf _build/
	jupyter-book clean ./ --all
deploy:
	ghp-import -n -p -f _build/html