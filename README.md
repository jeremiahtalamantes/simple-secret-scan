# simple-secret-scan
A small Python script that uses a very simple approach to finding hardcoded secrets in code. 

## Usage
- Save this script as `search_secrets.py`.
- Run it from the command line, providing the directory to search as an argument:

    `python search_secrets.py <directory>`

## Description
This Python script will search a given directory for hardcoded secrets in code, such as API keys or passwords, using regular expressions (regex). Please note that this script will not catch all secrets, and you should always use proper secret management tools for better security. That said, short of using any tool whatsoever, this small script could be Step 0 toward a better secret management tool.

This regular expression looks for base64-encoded strings. Base64 is a common encoding format for representing binary data in an ASCII string format. It consists of characters from the sets A-Z, a-z, 0-9, '+', and '/'. In base64, every 4 characters represent 3 bytes of binary data. The last group of characters may be followed by one or two padding '=' characters. This pattern may match API keys, tokens, or other secrets encoded in base64.

    re.compile(r'((?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?)'):

This regular expression searches for strings that are exactly 32 characters long and consist of alphanumeric characters (A-Z, a-z, 0-9). This pattern can match MD5 hashes, which are commonly used for storing passwords, unique identifiers, or other sensitive data.

    re.compile(r'([A-Za-z0-9]{32})'):

This regular expression looks for strings that are exactly 40 characters long and consist of alphanumeric characters (A-Z, a-z, 0-9). This pattern can match SHA-1 hashes, which are often used for storing passwords or other sensitive data.

    re.compile(r'([A-Za-z0-9]{40})'):

This regular expression searches for strings that are exactly 64 characters long and consist of alphanumeric characters, hyphens (-), and underscores (_). This pattern may match API keys, tokens, or other secrets that follow this specific format.

    re.compile(r'([A-Za-z0-9-_]{64})'):


## Disclaimer
It's important to note that these regular expressions will produce false positives or fail to catch certain secrets. They are intended to provide a **simple** approach for identifying potential hardcoded secrets in code. For optimal security, always use proper secret management tools and best practices.