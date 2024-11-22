all:
	@make norm
	@make git
git:
	git add ex00/Hello.py
	git add ex01/format_ft_time.py
	git add ex02/find_ft_type.py
	git add ex03/NULL_not_found.py
	git add ex04/whatis.py
	git add ex05/building.py
	git add ex06/ft_filter.py
	git add ex06/filterstring.py
	git add ex07/sos.py
	git add ex08/Loading.py
	git add ex09/LICENSE
	git add ex09/pyproject.toml
	git add ex09/README.md
	git add ex09/ft_package/__init__.py
	git add ex09/ft_package/ft_package.py

norm:
	flake8 ex00 ex01 ex02 ex03 ex04 ex05 ex06 ex07 ex08 ex09

test:
	cd ex00 && python3 Hello.py
	cd ex01 && python3 format_ft_time.py
	cd ex02 && python3 find_ft_type.py
	cd ex03 && python3 NULL_not_found.py
	cd ex04 && python3 whatis.py
	cd ex05 && python3 building.py	
	cd ex06 && python3 ft_filter.py
	cd ex07 && python3 sos.py
	cd ex08 && python3 tester.py
	cd ex09 && make

.PHONY: all clean fclean re
