#!/bin/bash

echo "Enter the name of the script file to copy:"
read script_name

echo "Enter the number of copies to make:"
read num_copies

echo "Enter the prefix for the copied files:"
read prefix

for ((i=1; i<=num_copies; i++))
do
  cp "$script_name" "${prefix}${i}.sh"
done

echo "Done!"
