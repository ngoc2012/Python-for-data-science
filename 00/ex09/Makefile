# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcyprien <dcyprien@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/28 10:56:09 by minh-ngu          #+#    #+#              #
#    Updated: 2024/04/15 13:09:28 by dcyprien         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
	#python3 setup.py sdist bdist_wheel

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
	rm -rf *.egg-info
	@echo "=============== Uninstalling ft_package ==============="
	pip uninstall -y ft_package
	
.PHONY: all clean fclean re tests build
