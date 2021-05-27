# Importing modules
import cv2
import pytesseract
from pytesseract import Output
from pprint import pprint

# STEP-1: reading the image using OpenCV
img_obj = cv2.imread('pytesseract_test/IMG_6823-cropped.jpeg')
# cv2.imshow('Original Image', img_obj)
# cv2.waitKey(0)

# STEP-2: converting the image into the gray scale
img_obj_gray = cv2.cvtColor(img_obj, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray Scale Image', img_obj)
# cv2.waitKey(0)

# STEP-3: converting the image into binary image by thresholding
img_obj_threshold = cv2.threshold(img_obj_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# cv2.imshow('Thresholded Image', img_obj)
# cv2.waitKey(0)

# STEP-4: configuring the parameters for tesseract
custom_config = r'--oem 3 --psm 6'

# STEP-5: feeding image to pytesseract
details = pytesseract.image_to_data(img_obj_threshold, output_type=Output.DICT, config=custom_config, lang='eng')

# STEP-6: Drawign the bounding boxes for the image 
total_boxes = len(details['text'])

for seq_num in range(total_boxes):
    if int(details['conf'][seq_num]) > 20:
        (x, y, w, h) = (details['left'][seq_num], details['top'][seq_num], details['width'][seq_num], details['height'][seq_num])
        img_obj_threshold = cv2.rectangle(img_obj_threshold, (x, y), (x + w, y + h), (0, 252, 0), 1)
    
#displaying the image 
cv2.imshow('Captured text', img_obj_threshold)
cv2.waitKey(0)

# STEP-7: Parsing the text 
parse_txt, word_list, last_word = [], [], ''
for word in details['text']:
    if word != '':
        word_list.append(word)
        last_word = word
    
    if (last_word != '' and word == '') or (word == details['text'][-1]):
        parse_txt.append(word_list)
        word_list = []

pprint(parse_txt)
pprint(word_list)

print('done')