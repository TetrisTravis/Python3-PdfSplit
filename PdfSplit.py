#! python3

# Makes a separate folder for each pdf file and splits the pdf file in that folder
# PdfSplit "<Path>" <-- place path between commas 

import os, PyPDF2, sys, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

#Get path where we want to launch the script and set as current working directory
path = sys.argv[1]
logging.debug('The path is ' + path)

os.chdir(path)
logging.debug('Current working directory: ' + os.getcwd())


# Loop through all files in a folder (subfolders NOT included)
logging.debug("Directory list: " + str(os.listdir(path)))
              
for file in os.listdir(path):
    
    # Verify is file is pdf
    if file.endswith('.pdf'):
        # Create folder for .pdf file and name folder accordingly
        try:
            os.makedirs(r'.\%s' % file[:-4])
        except:
            print(r'The folder .\%s already exists' % file[:-4])
            continue
        
        #TODO: Split .pdf file
        pdfFile = open(file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        

        for pageNum in range(pdfReader.numPages):
            pdfWriter = PyPDF2.PdfFileWriter()
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
            #TODO: Save .pdf files in folder
            pdfOutputFile = open(r'.\%s\Page%s.pdf' % (file[:-4], str(pageNum)), 'wb')
            pdfWriter.write(pdfOutputFile)
            pdfOutputFile.close()

        pdfFile.close()
        
        
        

