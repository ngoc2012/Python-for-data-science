FILES :=\
	ex00/Hello.py \
	ex01/format_ft_time.py \
	ex02/find_ft_type.py \
	ex03/NULL_not_found.py \
	ex04/whatis.py \
	ex05/building.py \
	ex06/ft_filter.py \
	ex06/filterstring.py \
	ex07/sos.py \
	ex08/Loading.py \
	ex09/LICENSE \
	ex09/pyproject.toml \
	ex09/README.md \
	ex09/ft_package/__init__.py \
	ex09/ft_package/ft_package.py

all:
	@make norm
	@make git
git:
	git add $(FILES)

bat:
	batcat $(FILES)

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
