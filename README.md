# Python3-PdfSplit
Works for Windows and makes use of PyPDF2.

Takes a directory, finds all pdf files (subfolders not included), creates a new folder for each pdf file, splits pdf file in the respective folder

PdfSplit requires a PdfSplit.bat file in a folder that is added to the computer's system path, with the following contents:

@py.exe <path of PdfSplit.py> %*
  
  
To call the application:
1. open a run window
2. input: PdfSplit "<path where you want to unleash PdfSplit>" <---the "" are important, please do not forget them.
3. profit
