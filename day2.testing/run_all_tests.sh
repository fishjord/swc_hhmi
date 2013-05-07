#!/bin/bash

for test_file in `ls test_*.txt`
do
	echo "Current test file is $test_file"
	./mean.py $test_file
done
