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

You can also run it as a batch file which will reduce the processing fee in half however turnaround time could range up to 24 hours.

Code line 60-62:

		 messages=[
            {"role": "user", "content": f"Summarize the findings from the following abstract in 2 sentences: {abstract} Thanks!"}
        ]

This line of code includes the message that is being sent to the model with the f"Question to model". This can be changed to fit the need of your review. There were multiple phrases that were tested and this was the most consistent coherent output from the model.






EXTRAS/FUTURE ADD-ONS

In the future, a nice addition to this tool would be to add an export to CSV function where the collected summarized abstracts can then be exported as a .csv file to allow for easy sharing of the information using the PRE teams 365/teams functions(csv will need to be converted to excel formatting for this to work). To add a function like this I would follow the relative format I have been using starting with the usula functions. I would keep the action and function names consistent too (something like "export" and '/export')

		@app.route('/export', methods=['GET'])
  
Make sure that you update your HTML file to add a button something along this should work:

		<h1>Export Data</h1>
		<form method="GET" action="/export">
  		  	<button type="submit">Export to CSV</button>
		</form>

Then make a function "export" (def export():) with the following code  

	papers = Paper.query.all()
    data = [{
    	##All the data you will want to export##
        } for paper in papers]

    df = pd.DataFrame(data)
    csv_data = df.to_csv(index=False)

    return Response(
        csv_data,
        mimetype='text/csv',
        headers={'Content-Disposition': 'attachment;filename=##future file name##'}

There are two parts to this that need to be immediately changed for this to work and are indicated with ##enclosed message##. 
##All the data you will want to export##
You will need to add the data you want to export in this data frame (ex if you want author you will need to add 'Author': paper.author)
##future file name##
Just the name of your future file will replace this, if you save more than one on the same desktop it will just add filename.csv --> filename(2).csv 

One other addition could be instead of adding a csv button you add an Excel button, I am not sure of the exact way to code this up but you would likely need to use to_excel alongside the BytesIO package to complete this.















