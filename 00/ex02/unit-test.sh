echo "================================= ex01 ================================="
command1="python3 tester.py | cat -e"
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

command1="python3 find_ft_type.py | cat -e"
echo "Command: $command1"
output=$(eval $command1)
echo -e "$output" | cat -e
