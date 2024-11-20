echo "================================= ex07 ================================="
command1="\
python3 sos.py 'sos' | cat -e && \
python3 sos.py 'h\$llo' \
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

#commands=(\
#"python3 filterstring.py 0 0" \
#"python3 filterstring.py 0 0.0001" \
#"python3 filterstring.py '' 0" \
#"python3 filterstring.py '' 1" \
#"python3 filterstring.py '' 99999999999999999999999999999999999999999999999" \
#)
#
#for cmd in "${commands[@]}"; do
#	echo "Executing: $cmd"
#	output=$(eval $cmd)
#	echo -e "$output" | cat -e
#	echo
#done
