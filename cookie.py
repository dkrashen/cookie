#!/usr/bin/env python3

import os
import random
import json
import argparse
import shutil  # For copying files

class Quotes:
    def __init__(self):
        self.quotes = []

    def make_quotes_from_file(self, filename):
        with open(filename, "r") as f:
            s = f.read()
        self.quotes = parse_quotes(s)

    def random(self):
        return random.choice(self.quotes)

def parse_quotes(text):
    r"""
    Split a multi-section text on lines containing only the '%' character.
    
    This function divides text into sections where each section is separated by
    a line containing only '%' (possibly with surrounding whitespace). The separator
    lines themselves are not included in the returned sections.
    
    Args:
        text (str): The input text to be split into sections.
        
    Returns:
        list: A list of strings, where each string is a section of the original text.
              Empty sections are not included in the result.
    
    Example:
        >>> text = "Section 1\n%\nSection 2"
        >>> parse_quotes(text)
        ['Section 1', 'Section 2']
    """
    lines = text.split('\n')
    sections = []
    current_section = []
    
    for line in lines:
        if line.strip() == '%':
            if current_section:
                sections.append('\n'.join(current_section))
                current_section = []
        else:
            current_section.append(line)
    
    if current_section:
        sections.append('\n'.join(current_section))
    
    return sections

def load_config(config_path):
    if not os.path.exists(config_path):
        default_config = {"default_quotes": ""}
        save_config(default_config, config_path)
        return default_config
    with open(config_path, 'r') as f:
        return json.load(f)

def save_config(config, config_path):
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)

def list_quote_files(quotes_dir):
    """Return a list of files in the quotes directory."""
    if not os.path.isdir(quotes_dir):
        return []
    return [f for f in os.listdir(quotes_dir)
            if os.path.isfile(os.path.join(quotes_dir, f))]

def main():
    # Determine the directory where the script is located (resolving symbolic links)
    script_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(script_dir, 'config.json')
    quotes_dir = os.path.join(script_dir, 'quotes')

    parser = argparse.ArgumentParser(description="Random Quote Generator")
    parser.add_argument('--list', action='store_true',
                        help="List available quote files")
    parser.add_argument('--set-default', metavar='FILE',
                        help="Set default quote file")
    parser.add_argument('--file', metavar='FILE',
                        help="Use a specific quote file for this run")
    parser.add_argument('-a', '--add', metavar='FILE',
                        help="Copy a quote file to the quotes directory")
    parser.add_argument('-f', '--force', action='store_true',
                        help="Force overwrite when adding a file if the file already exists in the quotes directory")
    args = parser.parse_args()

    # List available quote files
    if args.list:
        files = list_quote_files(quotes_dir)
        if not files:
            print("No quote files found in", quotes_dir)
        else:
            print("Available quote files:")
            for file in files:
                print(" -", file)
        return

    # Set default quote file
    if args.set_default:
        available_files = list_quote_files(quotes_dir)
        if args.set_default not in available_files:
            print(f"Error: '{args.set_default}' is not in the quotes directory.")
            return
        config = load_config(config_path)
        config["default_quotes"] = args.set_default
        save_config(config, config_path)
        print(f"Default quote file set to '{args.set_default}'")
        return

    # Save a new quote file into the quotes directory
    if args.add:
        source_file = os.path.abspath(args.add)
        if not os.path.exists(source_file):
            print(f"Error: Source file '{source_file}' not found.")
            return

        # Destination is inside the quotes directory with the same base name
        dest_file = os.path.join(quotes_dir, os.path.basename(source_file))
        if os.path.exists(dest_file) and not args.force:
            response = input(f"File '{dest_file}' already exists. Overwrite? [y/N]: ")
            if response.lower() != 'y':
                print("File not overwritten.")
                return

        try:
            shutil.copy(source_file, dest_file)
            print(f"File '{source_file}' successfully copied to quotes directory as '{os.path.basename(source_file)}'.")
        except Exception as e:
            print(f"Error copying file: {e}")
        return

    # Determine which quote file to use: command-line override or default.
    if args.file:
        quote_file = args.file
    else:
        config = load_config(config_path)
        quote_file = config.get("default_quotes")
        if not quote_file:
            print("No default quote file set. Use --set-default to set one.")
            return

    quote_file_path = os.path.join(quotes_dir, quote_file)
    if not os.path.exists(quote_file_path):
        print(f"Error: Quote file '{quote_file}' not found in {quotes_dir}.")
        return

    quotes = Quotes()
    quotes.make_quotes_from_file(quote_file_path)
    print(quotes.random())

if __name__ == "__main__":
    main()