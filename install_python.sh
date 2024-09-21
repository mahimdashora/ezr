#!/bin/bash

# Update and upgrade system
sudo apt update -y
sudo apt upgrade -y

# Install software-properties-common
sudo apt install software-properties-common -y

# Add deadsnakes PPA repository
sudo add-apt-repository ppa:deadsnakes/ppa -y

# Update package list again
sudo apt update -y

# Install Python 3.13
sudo apt install python3.13 -y
