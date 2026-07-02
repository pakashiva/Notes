from flask import Flask, render_template,request, redirect

app = Flask(__name__)

db = [] 

@app.route("/")
def home():
    return render_template("index.html", notes = db)

@app.route("/add" , methods = ['POST'])
def add_notes():
    title = request.form['title']
    content = request.form['content']

    note = {
        "id": len(db),
        "title": title,
        "content": content
    }

    db.append(note)

    return redirect("/")

@app.route("/edit/<int:index>" , methods = ['GET' , 'POST'])
def edit_note(index):
    if request.method == 'GET':
        return render_template("edit.html" , idx = index , note = db[index])
    
    new_title = request.form['title']
    new_content = request.form['content']

    db[index]["title"] = new_title
    db[index]["content"] = new_content

    return redirect("/")
    

@app.route("/delete/<int:index>" , methods = ['GET' , 'POST'])
def delete_note(index):
    if 0 <= index <= len(db):
        db.pop(index)

    return redirect("/")

if __name__ == "__main__": 
    app.run()