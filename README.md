# Google Script Search Tool

A simple Python script that opens Google searches in your browser with site-specific filters for popular developer and tech websites.

## Features

- Searches Google with automatic site filters
- Opens results in Brave browser
- Filters results to specific trusted websites:
  - Reddit
  - Medium
  - Google
  - Stack Overflow

## Requirements

- Python 3.x
- Brave browser installed at `/usr/bin/brave-browser`

## Installation

Make the script executable:

```bash
chmod +x main.py
```

Optionally, you can create a symlink or add the script to your PATH to use it as a system command:

```bash
# Option 1: Create a symlink in /usr/local/bin (requires sudo)
sudo ln -s $(pwd)/main.py /usr/local/bin/googlesearch

# Option 2: Add to PATH by adding this to your ~/.bashrc or ~/.zshrc
export PATH="$PATH:/path/to/goooglescript"
```

## Usage

### As a Command

If you've added it to your PATH or created a symlink:

```bash
googlesearch your search query here
```

Or run directly:

```bash
./main.py your search query here
```

### Example

```bash
googlesearch python list comprehension
# or
./main.py python list comprehension
```

This will open a Google search for "python list comprehension" filtered to the specified websites in your Brave browser.

## How It Works

The script:
1. Takes command-line arguments as your search query
2. Constructs a Google search URL with site filters
3. Opens the search results in Brave browser

## Notes

- If no search query is provided, the script will display an error message
- The script is configured to use Brave browser by default
- You can modify the `valid_websites` list in `main.py` to add or remove site filters

