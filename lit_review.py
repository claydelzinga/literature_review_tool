from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import openai

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///literature.db'
db = SQLAlchemy(app)

openai.api_key = "YOUR_OPENAI_API_KEY"

class Paper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    abstract = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file.filename.endswith('.csv'):
                df = pd.read_csv(file)
                for _, row in df.iterrows():
                    author = row['Author']
                    title = row['Title']
                    year = row['Year Published']
                    abstract = row['Abstract']
                    summary = summarize_abstract(abstract)
                    new_paper = Paper(author=author, title=title, year=year, abstract=abstract, summary=summary)
                    db.session.add(new_paper)
                db.session.commit()
        else:
            author = request.form['author']
            title = request.form['title']
            year = request.form['year']
            abstract = request.form['abstract']
            summary = summarize_abstract(abstract)
            new_paper = Paper(author=author, title=title, year=year, abstract=abstract, summary=summary)
            db.session.add(new_paper)
            db.session.commit()

    papers = Paper.query.all()
    return render_template('index.html', papers=papers)
def summarize_abstract(abstract):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"Summarize the findings from the following abstract in 2 sentences: {abstract} Thanks!"}
        ]
    )
    summary = response.choices[0]['message']['content']
    return summary.strip()

@app.route('/clear', methods=['POST'])
def clear():
    Paper.query.delete()
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
