"""
Page segmentation modes:

0   Orientation and script detection(OSD) only
1   Automatic page segmentation with OSD
2   Automatic page segmentation, but no OSD, or OCR
3   Fully automatic page segmentation, but no OSD . (default)
4   Assume a single column of text of variable sizes
5   Assume a single uniform block of vertcially aligned text
6   Assume a single uniform block of text
7   Treat the image as a single text line 
8   Treat the image as a single word
9   Treat the image as single word in a circle 
10  Trear the image as single character
11  Sparse text. Find as much text as possible in no particular order
12  sparse text with OSD 
13  Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific


"""

"""
OCR Engine Mode

0 Legacy engine only
1 Neural nets LSTM engine only
2 Legacy + LSTM engines
3 Default, based on what is available 

"""