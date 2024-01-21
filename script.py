#!/usr/bin/env python3

def prompt_yes_no_question(question):
    prompt = f"{question} (y/n): "
    user_input = input(prompt).lower()
    return user_input == "y"

def generate_shell_script(script_name):
    # Prompt the user for a yes or no question
    answer = prompt_yes_no_question("Do you only want paru or paru with pacman key fix")

    # Generate the shell script
    script = """#!/bin/sh

# Add your desired custom command here
sudo steamos-readonly disable
echo "keyserver hkps://keyserver.ubuntu.com" >> /etc/pacman.d/gnupg/gpg.conf
sudo pacman-key --init
sudo pacman-key --populate
sudo pacman-key --refresh-keys
"""

    if answer:
        # Add additional command to the script
        script += """
# Add your desired custom command here
sudo pacman -S base-devel
sudo pacman -S openssl
rm -rf paru
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
cd ..
rm -rf paru
"""
    
    script += """
echo "Hello, Arch Linux!"
# Add more commands here if needed
"""

    # Write the shell script to a file
    with open(script_name, "w") as f:
        f.write(script)
    
    print(f"Shell script '{script_name}' generated successfully.")

if __name__ == "__main__":
    script_name = "arch_start.sh"
    generate_shell_script(script_name)
