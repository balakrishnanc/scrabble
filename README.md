# About

Simple utility to guess valid words that could formed from a given list of letters.


## Usage

```
» usage: search.py [-h] [--min-len min_len] [--dict dict_file] letters

Retrieve proper words from the given letters

positional arguments:
  letters               Letters (without any space in between them)

optional arguments:
  -h, --help            show this help message and exit
  --min-len min_len, -m min_len
                        Minimum length of words
  --dict dict_file, -d dict_file
                        Compressed dictionary
```

## Example

 ```
» ./search.py -d ../word-list/word-list.txt.gz -m 4 trotgo
tort
toot
root
grotto
goot
grot
otto
trot
```
