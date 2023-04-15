# ***Project Scraping***

- ## **What is this?**
    ### This repo contains my scraping project.
    #
    ### There are 3 folders:
    - ### img:
        - ### contains the images used by the app and a folder named "scraped" destined to save the scraped image.
    - ### scheme:
        - ### contains a horrible png with an scheme of the app.
    - ### scraping app:
        - ### contains all the files of the app.
            ### v (( NOT NEEDED BECAUSE OCR HAS BEEN BYPASSED )) v
            + ### if you want to save the scraped image you'll need to change the path on:
                + ### scraping.py
                + ### line 6 - class do_scraping():
                    + ### line 27 - def step2_download(img_url):
                        + ### line 29 - directorio = "WRITE YOUR PATH"
            ### ^ (( NOT NEEDED BECAUSE OCR HAS BEEN BYPASSED )) ^

#
- ## **What was the goal?**
    1. ### ) First I wanted to apply OCR on an scraped image to take the information on a pandas.DataFrame, but this was not successful due to a malfunction of the library used (pytesseract), not taking all the information in a legible way.
    2. ### ) Because of this and the lack of development time I decided to make the scraping of the image with the information and then putting manually the information on a pandas.DataFrame.
    3. ### ) The final goal was to show the information inside a little app build with tkinter.

#
- ## **The tools I used are:**
    - ### tkinter (GUI - Graphical User Interface)
    - ### ctypes (C related data types and funtions)
    - ### time (time related functions)
    - ### threading (multiple threads)
    - ### PIL (image)
    - ### requests (web requests)
    - ### BeautifulSoup (web data)
    - ### pandas (DataFrames)
    - ### pytesseract (OCR - Optical Character Recognition)

# 
- ## **The conclusions of this project are:**
    - ### *Personal:*
        - #### Simplify your task. Try to use familiar tools when working under deadlines.
        - #### Limit yourself to developing what is necessary and do not get over-involved in a task, do it in a separate project of your own in which you have time and freedom.
            #### (I spent most of my time developing an app that wasn't necessary to meet any requirements just because it was stimulant. Big mistake I'd make again in pursuit of stimuli.)
        - #### ChatGPT is your best friend. Not because he can spit out large amounts of code that you don't even understand, but because he is capable of explaining every step if you ask him to be very specific, he understands errors (both those raised by libraries and yours as a programmer) and can help you out of your stagnant situations.
    - ### *Professional:*
        - #### OCR can be a powerful multi-scope tool if you know how to use it. In this case, machine learning and neural networks are used to create the learning models of the tool, so venturing into using it without knowing these can greatly limit your integration capabilities.
        - #### Threading is an incredibly important topic to be ignored.
        - #### This application simulates data collection by web request, but steps and checks are omitted, such as:
            - #### Save that data in a document locally.
                - #### It would make sense if it was obtained by the good functioning of OCR with the automation of the data retrieval.
                - #### It does not make sense in this case since the information is inserted manually after obtaining the image, through scraping, which provides it.
            - #### Check if the document with the required data already exists before executing a redundant action. Implement a button with the function of updating the data, executing scraping, in case it is pressed.
            - #### Re-build the only loading bar that appears when scraping (it's a sample simulation that doesn't represent a real load of the process) so that it returns useful information that can serve as a debug in case an error is raised.