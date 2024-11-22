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
	make build
	make install
	make test
build:
	python3 setup.py sdist bdist_wheel
test:
	cd tests && python3 tester.py
install:
	pip install dist/ft_package-0.0.1-py3-none-any.whl

install2:
	pip install dist/ft_package-0.0.1.tar.gz
re:
	pip install --force-reinstall dist/ft_package-0.0.1-py3-none-any.whl

fclean: clean

clean:
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	
.PHONY: all clean fclean re tests build
