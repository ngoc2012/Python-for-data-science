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
	cd ex00 && bash unit-test.sh
	cd ex01 && bash unit-test.sh
	cd ex02 && bash unit-test.sh
	cd ex03 && bash unit-test.sh
	cd ex04 && bash unit-test.sh
	cd ex05 && bash unit-test.sh
	cd ex06 && bash unit-test.sh
	cd ex07 && bash unit-test.sh
	cd ex08 && python3 tester.py
	cd ex09 && make

.PHONY: all clean fclean re
