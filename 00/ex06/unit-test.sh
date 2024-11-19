echo "================================= ex06 ================================="
command1="\
python3 filterstring.py 'Hello the World' 4 && \
python3 filterstring.py 'Hello the World' 99 && \
python3 filterstring.py 3 'Hello the World' && \
python3 filterstring.py"
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
"python3 filterstring.py 'Hello the World' 4" \
"python3 filterstring.py 'Hello the World' 99" \
"python3 filterstring.py 3 'Hello the World'" \
"python3 filterstring.py" \
"python3 filterstring.py 0 0" \
"python3 filterstring.py 0 0.0001" \
)

for cmd in "${commands[@]}"; do
	echo "Executing: $cmd"
	output=$(eval $cmd)
	echo -e "$output" | cat -e
	echo
done
