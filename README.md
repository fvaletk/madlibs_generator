# MadLibs Generator

## Overview

This Python-based MadLibs generator allows users to create fun and personalized stories. By leveraging a template from `story.txt`, the program prompts users to input words that replace placeholders within the story, creating a customized narrative.

## How It Works

 1. The script reads a story template with placeholders marked by `<` and `>`.
 2. It identifies all placeholders and asks the user to input words corresponding to each placeholder's description.
 3. The user's inputs are then inserted into the story, replacing the original placeholders.

## Getting Started

### Prerequisites
 - Python 3.x

### Running the Program

 1. Clone this repository.
 2. Add your `story.txt` file to the project directory. Ensure that placeholders are correctly formatted within the story.
 3. Run the script:
	  ```bash
	python madlibs_generator.py
    ```

## Customizing Your Story
To create your story template, write any text and enclose placeholders within `<` and `>`. For example, `<adjective>`, `<noun>`. These placeholders will be recognized by the script as input prompts for the user.

## Contributions

Feel free to fork this project, make changes, and submit pull requests. We appreciate efforts to improve the script's efficiency or enhance its functionality.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.