
# Resume PDF Generator

This Python script generates a customizable resume in PDF format using the FPDF library. Users can specify font size, font color, and background color via command-line arguments.

## Pre requisites Needed

1) Python 3.6+ version

2) FPDF library

Install fpdf library using this command
```bash
  pip install fpdf
```
3) DejaVuSans Font File
        
- Place the DejaVuSansCondensed.ttf font file in the same directory as the script.
    
## Arguments

--font_size: Font size for the text (e.g., 10, 12, 14).

--font_color: Font color in hex code format. (e.g., #FF5733).

--background_color: Background color in hex code format (e.g., #FFFFFF).


## Deployment

1) Open a terminal or command prompt.

2) Navigate to the directory where the script is located.

3) Run the script with the following arguments:

```bash
    python PDF_Generator.py --font_size <font_size> --font_color <font_color> --background_color <background_color>
```
4) Example Command:
```bash
    python PDF_Generator.py --font_size 12 --font_color "#FF5733" --background_color "#FFFFFF"
```
5) The PDF is saved as My_Resume.pdf in the script's directory.
## Features

1) Customizable font size, font color, and background color.
2) Predefined sections for:
    - Contact Details
    - Education
    - Skills
    - Project Experience
3) Automatically generates a PDF named My_Resume.pdf.


## Acknowledgements

I would like to express my gratitude to the developers and maintainers of the FPDF Python Library, whose documentation provided a comprehensive guide to creating and customizing PDFs. 

I am also thankful for the Python argparse documentation, which helped me implement command-line argument parsing effectively.

I extend my appreciation to the creator of the YouTube playlist, which clarified many concepts.

Lastly, I am grateful to Pragament Tech Solutions for giving me this opportunity to learn a new library.

- [FPDF Documentation](https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html)  
- [Python argparse Documentation](https://docs.python.org/3/howto/argparse.html)  
- [YouTube Playlist](https://www.youtube.com/playlist?list=PLjNQtX45f0dR9K2sMJ5ad9wVjqslNBIC0)


"# Python-PDF-Maker" 
"# Python-PDF-Maker" 
