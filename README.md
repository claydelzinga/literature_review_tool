Hello, this is a literature review tool that can be used with a .csv file with the contents of authors, title, year published and abstract in the file. 
All of this content can be downloaded in csv formatting using the tool Scopus which allows for search queries of papers using keywords and other filters.






Some notes about this file for the PRE team:

This tool requires an API key from OpenAI which you can use to call the GPT model. The cost of this, if you are using the GPT 4-o mini, is so small you can run 100+ papers for <0.01 USD (The GPT 4 model is a bit more expensive than this). On average the application takes 3 minutes 30 seconds/100 papers (Average speed per 100 papers abstracts).

SETUP FILES

The first thing you will need to do is create a new directory, in this directory you will have a folder named "instance" and the "instance" folder will contain your SQL database named "literature.db". This holds and stores any data from the summaries (the literature summaries will be saved on your machine if you close the application).
Next, you will create a folder named templates which will include an .html file named "index.html". The index.html will contain the structure of the application and if parts are deleted, it will alter the visual appearance of the application
Finally, create your literature review file that will end in .py (ex "lit_review_trial.py")
The file structure should follow:

Project_Name

-instance

---litreature.db

-templates

---index.html

-lit_review_trial.py

Code line 10:
		open.api_key = "YOUR_API_KEY"
This line should include your API key inside the quotations 




