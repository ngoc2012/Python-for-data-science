echo "================================= ex07 ================================="
command1="python3 tester.py"

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
"python3 tester1.py"\
"python3 tester1.py"\
)

for cmd in "${commands[@]}"; do
	echo "Executing: $cmd"
	output=$(eval $cmd)
	echo -e "$output" | cat -e
	echo
done
