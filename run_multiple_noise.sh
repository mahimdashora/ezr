#!/bin/bash

# Define the input file and output file paths
#input_file=/workspaces/ezr/data/optimize/config/SS-A.csv  #"/workspaces/ezr/data/optimize/misc/auto93.csv"     #"/workspaces/ezr/data/optimize/config/SS-A.csv"   #"/workspaces/ezr/data/optimize/misc/auto93.csv"
input_files=(
    "/workspaces/ezr/data/optimize/process/coc1000.csv"
)

output_file="/workspaces/ezr/accuracy.txt"

# Clear previous output
> $output_file

# Define an array of noise values to test
noise_values=(0 0.05 0.1 0.15 0.2 0.4)

# Loop through each noise value, execute the command, and append the output
# for noise in "${noise_values[@]}"; do
#     echo "Running with noise=$noise" >> $output_file
#     python3 -B extend_mahim.py $input_file $noise >> $output_file
#     echo -e "\n" >> $output_file
# done

for input_file in "${input_files[@]}"; do
    echo "Processing file: $input_file" >> $output_file
    # Loop through each noise value, execute the command, and append the output
    for noise in "${noise_values[@]}"; do
        echo "Running with noise=$noise" >> $output_file
        python3 -B extend_mahim.py $input_file $noise >> $output_file
        echo -e "\n" >> $output_file
    done
    echo -e "Finished processing $input_file\n" >> $output_file
done

echo "All commands executed. Output saved to $output_file."
