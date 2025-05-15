**Ternary Search Tree Autocomplete Project** :sparkles:

:rocket: **Overview**

Welcome to the Ternary Search Tree (TST) Autocomplete Project! This repository showcases an implementation of a TST using nested Python dictionaries, designed to power an efficient autocomplete algorithm. Integrated with a fun "Word Akinator" guessing game, it allows users to manage a dictionary, play interactive word games, and explore word frequency data—all powered by a word list from a CSV file.

:hammer_and_wrench: **Features**

Insert Words: Seamlessly add new words to the TST with recursive insertion.
Traverse Tree: Explore and list all words stored in the TST.
Check Existence: Quickly verify if a word is part of the dictionary.
Delete Words: Remove words from the TST with ease.
Autocomplete: Get smart word suggestions based on any prefix.
Word Guessing Game: Engage in a thrilling game where the program guesses your word using frequency insights.
Frequency Tracking: Leverage a frequency dictionary to prioritize commonly guessed words.

:file_folder: **File Structure**

python_project_dsa_1.py: The heart of the project, containing TST logic and the Word Akinator game.
4000-most-common-english-words-csv.csv: A CSV file with common English words to initialize the TST (not included; provide your own).

:gear: **Requirements**

Python 3.x
A CSV file with a list of words (e.g., 4000-most-common-english-words-csv.csv)—first line is a header and skipped.

:computer: **Usage**

:arrow_forward: **Getting Started**

Prepare the Word List:
Obtain a CSV file with one word per line and a header row.


Run the Program:
Launch the script:python python_project_dsa_1.py


The TST will load words from the CSV and launch the Word Akinator interface.



:game_die: **Interacting with Word Akinator**

Choice 1: Play a Guessing Game - Think of a word, enter a prefix, and let the program guess it based on frequency. Confirm or correct the guess.
Choice 2: Insert a Word - Add a new word (e.g., "zebra") to the TST.
Choice 3: Delete a Word - Remove an existing word (e.g., "zebra").
Choice 4: Print All Words - View the entire word list.
Choice 5: Check Existence - Confirm if a word exists.
After each action, choose yes to continue or no to exit.

:bulb: **Example**

Loading Words: The program reads from 4000-most-common-english-words-csv.csv to build the TST.
Guessing Game: Enter prefix "app" to get suggestions like ["apple", "application", "approve"]. The program picks the highest-frequency match.
Inserting: Add "zebra" via Choice 2.
Deleting: Remove "zebra" via Choice 3 if it exists.
Checking: Verify "apple" exists with Choice 5.

:warning: **Notes
**
The TST uses nested dictionaries with root, left, mid, right, and end_of_word nodes.
Autocomplete navigates to the prefix subtree and traverses for suggestions.
Frequency data enhances game accuracy.

:construction: **Limitations**

Assumes a well-formed CSV input.
File I/O may not work in browser-based environments.
Deletion might leave empty nodes.

:chart_with_upwards_trend: **Future Improvements**

Add robust error handling for file operations.
Optimize deletion to remove empty nodes.
Enable saving TST and frequency data.
Limit autocomplete suggestions.

:scroll: **License**
For educational use only, no specific license applied. Feel free to use and modify for non-commercial purposes.

