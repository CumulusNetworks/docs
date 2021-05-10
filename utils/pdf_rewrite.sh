#!/usr/bin/env bash

find ./public -name "index.html" | grep pdf | while read -r line ; do
    echo "Rewriting $line"
    sed -i 's/<div class=\"expand-content\" style=\"display: none;\">/<div class=\"expand-content\" style=\"\">/g' $line
done