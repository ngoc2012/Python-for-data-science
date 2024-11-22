# https://github.com/pypa/packaging-problems/issues/606
#
all:
	@echo "=============== Test with whl ==============="
	@make clean
	@make build
	@make install
	@make test
	@echo "=============== Test with tar ==============="
	@make clean
	@make build
	@make install2
	@make test

build:
	@echo "=============== Building ft_package ==============="
	python3 -m build

test:
	@echo "=============== Checking ft_package ==============="
	pip show -v ft_package
	@echo "=============== Testing ft_package ==============="
	@cd tests && python3 tester.py

install:
	@echo "=============== Installing ft_package with whl ==============="
	pip install dist/ft_package-0.0.1-py3-none-any.whl

install2:
	@echo "=============== Installing ft_package with tar ==============="
	pip install dist/ft_package-0.0.1.tar.gz

re:
	@echo "=============== Reinstalling ft_package with whl ==============="
	pip install --force-reinstall dist/ft_package-0.0.1-py3-none-any.whl

fclean: clean

clean:
	rm -rf dist
	rm -rf build
	rm -rf ft_package.egg-info
	@echo "=============== Uninstalling ft_package ==============="
	pip uninstall -y ft_package
	
.PHONY: all clean fclean re tests build
