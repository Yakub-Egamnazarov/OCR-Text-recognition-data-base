def img_to_text(input_dir, output_dir):
    img_names = os.listdir(input_dir)
    img_names.sort()

    count = 0
    for img in img_names:
        img_path = os.path.join(input_dir, img)
        
        # Read the image from which text needs to be extracted
        img_obj = cv2.imread(img_path)
        
        # Preprocessing the image
        # 1. Convert the image to gray scale
        gray_img = cv2.cvtColor(img_obj, cv2.COLOR_BGR2GRAY)
        
        # 2. Performing OTSU Threshold
        ret, thresh1 = cv2.threshold(gray_img, 0, 255, 
                            cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
        
        # Specify structure shape and kernel size 
        # Kernel size increases or decreases the area 
        # of the rectangle to be detected. 
        # A smaller value like (10, 10) will detect 
        # each word instead of a sentence. 
        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, 
                                                (50, 20))
        
        # applying dilation on the threshold image
        dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
        
        # Finding contours
        contours, hierarchy = cv2.findContours(dilation, 
                                               cv2.RETR_EXTERNAL, 
                                               cv2.CHAIN_APPROX_NONE)
        
        # creating a copy of the image 
        img_obj_2 = img_obj.copy()
        
        # a text file created for the image 
        
        # Looping through the identified contours 
        # Then Rectangular part i scropped and passed
        # on to pytesseract for extracting text from it 
        # Extracted text is then written in to the file 
        text_all= ''
        for cnt in contours: 
            x, y, w, h = cv2.boundingRect(cnt)
            
            # Drawing a rectangle on copied image 
            rect = cv2.rectangle(img_obj_2, 
                                 (x, y), 
                                 (x + w, y + h), 
                                 (0, 255, 0), 
                                 2)
            
            # cropping the text block for giving input to ocr 
            cropped = img_obj_2[y: y + h, x: x + w]
            text = pytesseract.image_to_string(cropped)
            text_all += text.strip() + '\n'

        
        file_path = os.path.join(output_dir, 
                                 img.split('-')[0] + '-raw.txt')
        file = open(file_path, 'w')
        file.write(text_all)
        file.close()
        
        cv2.imwrite(os.path.join(os.getcwd(), 
                                 'img_boxed', 
                                 img.split('-')[0] + '-boxed.jpg'), 
                    img_obj_2)
        count += 1
        print ('done ocr: ', count)
        
        




