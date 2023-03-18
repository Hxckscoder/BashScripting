#!/bin/bash

# Define colors for terminal output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Define functions
function greeting {
    echo "Hello there! My name is $0"
}

function ask_name {
    read -rp "What is your name: " name
    if [[ -z "$name" ]]; then
        echo -e "${RED}Please enter your name.${NC}"
        ask_name
    elif [[ "$name" = "Abdul" ]]; then
        name="Boss"
    fi
    echo "Nice to meet you, $name."
}

function ask_question {
    read -rp "What do you do? " q1
    if [[ -z "$q1" ]]; then
        echo -e "${RED}Please enter a response.${NC}"
        ask_question
    fi
    echo "Wow! I hear some good things about $q1."
}

function farewell {
    echo -e "${GREEN}It's been a pleasure meeting you, $name.${NC}"
    echo "Goodbye!"
}

# Main script
greeting
ask_name
ask_question
farewell
