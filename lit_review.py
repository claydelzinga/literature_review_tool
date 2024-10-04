from flask import Flask, render_template, request, redirect, url_for, Response
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import openai

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///literature.db'
db = SQLAlchemy(app)

openai.api_key = "YOUR_API_KEY_HERE"

class Paper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    abstract = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text)

@app.route('/', methods=['GET', 'POST'])
def index():
    papers = Paper.query.all()
    return render_template('index.html', papers=papers)

@app.route('/upload', methods=['POST'])
def upload():
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
    return redirect(url_for('index'))

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    papers = Paper.query.filter(
        (Paper.author.like(f'%{keyword}%')) |
        (Paper.title.like(f'%{keyword}%')) |
        (Paper.abstract.like(f'%{keyword}%')) |
        (Paper.summary.like(f'%{keyword}%'))
    ).all()
    return render_template('index.html', papers=papers, keyword=keyword)

@app.route('/clear_search', methods=['POST'])
def clear_search():
    return redirect(url_for('index'))

def summarize_abstract(abstract):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"Summarize the findings from the following abstract in 2 sentences: {abstract} Thanks!"}
        ]
    )
    # Correctly access the content using dot notation
    summary = response.choices[0].message.content
    return summary.strip()

@app.route('/clear', methods=['POST'])
def clear():
    Paper.query.delete()
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/export', methods=['GET'])
def export():
    papers = Paper.query.all()
    data = [{
        'Author': paper.author,
        'Title': paper.title,
        'Year Published': paper.year,
        'Abstract': paper.abstract,
        'Summary': paper.summary
    } for paper in papers]

    df = pd.DataFrame(data)
    csv_data = df.to_csv(index=False)

    return Response(
        csv_data,
        mimetype='text/csv',
        headers={'Content-Disposition': 'attachment;filename=literature_summary.csv'}
    )

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)




