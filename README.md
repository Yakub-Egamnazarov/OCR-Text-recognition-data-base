This project is created to extract company informataion from pictures and place the text data to excel DataBase

It implements the power of python with support of some third party libraries:

    1. pytesseract | for python library for tesseract OCR - google
    2. 0penCV | python computer vision library 
    3. pyheif | for converting the pictures from IOS based to general jpg format, at the same time cropping in the part of onterest
    4. openpyxl | for manipulating excel file with python
    5. re | Regular expression library for python - for parsing the data 

Program logic:
1. All the images placed in the img_heic 
2. all the programming logic is placed in pytesseract/main.py folder.
3. when run it automatically 
    - scans the img_heic folder for raw images (.heac)
    - converts it into jpg format through pyheif library 
    - saves all the pictures files into the img_cropped folder
    - scans all the cropped pictures with pytesseract and OpenCV 
    - extracts the data and draws boxes and saves pictures in the folder img_boxed
    - all extracted data is saved in csv file format in output-txt folder
    - scans output-txt folder for text files (.csv) and parses it for certain setup data units 
    - all the data saved in one dictionary and saved in excel file in output_data/customer_list-0.xlsx 

4. delete.py file deletes all the created files and erases data from the final excel file. 
