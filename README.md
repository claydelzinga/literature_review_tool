Hello, this is a literature review tool that can be used with a .csv file with the contents of authors, title, year published and abstract in the file. 
All of this content can be downloaded in csv formatting using the tool Scopus which allows for search queries of papers using keywords and other filters.






Some notes about this application for the PRE team:

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

Code line 4:

	import openai

When installing openai package in your virtual environment or your project use openai <0.99. For my project I used openai 0.27.0

Code line 10:

		open.api_key = "YOUR_API_KEY"
  
This line should include your API key inside the quotations. (Don't share/upload your API key as it can be used by others)

Code line 23:

		def index():
    papers = Paper.query.all()
    return render_template('index.html', papers=papers)

The html formatting of the site can have a different file name however you will need to change it in line 23 from 'index.html' to your new html file name. 

Code line 59:

		model="gpt-4o-mini",

This line of code will tell the API which model to use, as stated before the gpt 4-o mini is the cheapest and quickest current model. Other models include;
gpt-4o ($5.00 / 1M input tokens $15.00 / 1M output tokens),
gpt-4o-mini ($0.150 / 1M input tokens $0.600 / 1M output tokens),
gpt-4-turbo ($10.00 / 1M tokens $30.00 / 1M tokens)

You can also run as a batch file that will reduce proces in half however turnaround time could range up to 24 hours.

Code line 60-62:

		 messages=[
            {"role": "user", "content": f"Summarize the findings from the following abstract in 2 sentences: {abstract} Thanks!"}
        ]

This line of code includes the message that is being sent to the model with the f"Question to model". This can be changed to fit the need of your review. There were multiple phrases that were tested and this was the most consistent coherent output from the model.






