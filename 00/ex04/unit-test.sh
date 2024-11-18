echo "================================= ex04 ================================="
command1="\
python3 whatis.py 14 && \
python3 whatis.py -5 && \
python3 whatis.py && \
python3 whatis.py 0 && \
python3 whatis.py Hi! && \
python3 whatis.py 13 5 \
"
echo "Command: $command1"
output=$(eval $command1)
echo -e "Actual Output:\n$output"
output_file=$(mktemp)
echo "$output" > "$output_file"
if diff -q "output" "$output_file" > /dev/null; then
    echo "Output matches the expected value."
else
    echo "Output does not match the expected value."
    diff "output" "$output_file"
fi
rm "$output_file"

commands=(\
"python3 whatis.py 108435803487987979874798797987979879879879874" \
"python3 whatis.py -59999999999999999999999999999999999999999999999999999999999" \
"python3 whatis.py 0.0000000000000000000000000000000000000000000000000000000001" \
"python3 whatis.py -0.0000000000000000000000000000000000000000000000000000000001" \
"python3 whatis.py 1e100" \
"python3 whatis.py -1e100" \
)

for cmd in "${commands[@]}"; do
	echo "Executing: $cmd"
	output=$(eval $cmd)
	echo -e "$output" | cat -e
	echo
done
