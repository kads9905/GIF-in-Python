# Python GIF Generator

A simple Python project that creates an animated GIF from a sequence of PNG images using the `imageio` library.

## Features

- Converts PNG images into an animated GIF
- Automatically reads all PNG files from the `shrek` folder
- Supports any number of images
- Adjustable animation speed

## Project Structure

```
GIF IN PYTHON/
├── create_gif.py
├── shrek/
│   ├── 1.png
│   ├── 2.png
│   └── ...
├── shrek.gif
└── README.md
```

## Requirements

- Python 3.x
- imageio

Install the required package:

```bash
pip install imageio
```

## Usage

1. Place your PNG images inside the `shrek` folder.
2. Run the script:

```bash
python create_gif.py
```

3. The generated GIF will be saved as `shrek.gif`.

> **Note:** The included `shrek` folder is just an example. You can use PNG frames extracted from **any GIF** by replacing the images in the folder (or updating the folder path in the script).

## Preview

![Shrek GIF](shrek.gif)