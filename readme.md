# cookie, a fortune-style random quote generator

A simple Python command-line tool to display random quotes from text files.

## FEATURES
- Random Quote Display: Prints a random quote from the selected quote file.
- Multiple Quote Files: Supports using multiple quote files stored in a designated “quotes” directory.
- Configurable Default: Set a default quote file using the provided command-line options.

## INSTALLATION

1.	Clone the repository:
```bash
git clone https://github.com/dkrashen/cookie.git
```
2.	Ensure Python 3 is installed:


## USAGE

Run the script from the command line:

Display a Random Quote (Using the Default Quote File):
```bash
python3 cookie.py
```

List Available Quote Files:
```bash
python3 cookie.py –-list
```
This will display all quote files found in the “quotes” directory.

Set a Default Quote File:
```bash
python3 cookie.py -–set-default filename
```

Specify a Quote File for a Single Run:
```bash
python3 cookie.py -–file filename
```
This option overrides the default quote file for that run.

Add a Quote File:
```bash
python3 cookie.py -–add filename
```
or
```bash
python3 cookie.py -a filename
```
The file should be formatted as below. If the file already exists, the user will be prompted to overwrite. 

Add a Quote File (force overwrite):
```bash
python3 cookie.py -–add --force filename
```
or
```bash
python3 cookie.py -af filename
```

## QUOTE FILE FORMAT

Use a line containing only the “%” character (ignoring surrounding whitespace) as a delimiter.

Example:


Quote 1: Life is what happens when you’re busy making other plans.
%
Quote 2: To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.
%
Quote 3: The only limit to our realization of tomorrow is our doubts of today.


Each section between “%” lines is treated as an individual quote.


## CONTRIBUTING

Contributions are welcome! Please open issues or submit pull requests if you have suggestions or improvements.

## LICENSE

This project was written by Danny Krashen with help by ChatGPT and Claude. It is licensed under the Creative Commons Attribution License (CC BY). See the LICENSE file for details.

