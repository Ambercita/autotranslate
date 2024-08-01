# AutoTranslate

 AutoTranslate files on LibreTranslate server

## Installation

1. Clone or download libretranslate from [LibreTranslate Github](https://github.com/LibreTranslate/LibreTranslate).
2. Use `run.bat` or `run.sh` script to launch the local server.
3. Install python and pip libraries libretranslate and requests `pip install libretranslate requests`.
4. Now you're ready to use the provided scripts!

## Configuration

1. Configure HOST_URL to setup the url where the libretranslate server is hosted (default https://localhost:5000)
2. Configure INPUT_FOLDER for the folder where the files are going to be read from.
3. Configure OUTPUT_FOLDER for the folder where the files are going to be written to (it should be different than INPUT_FOLDER).
4. Configure INPUT_LANG for the language that the files are written in.
5. Configure OUTPUT_LANG for the language you want to translate the files to.

## Usage

You can execute the python script with `python3 ./autotranslate.py` or the jupyter notebook interactively.
