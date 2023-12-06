from flask import Flask , render_template
import sqlite3
import pathlib


Titan = Flask(__name__)


base_path = pathlib.Path().cwd()
db_name = "Titanic.db"
File_path = base_path / db_name

@Titan.route("/")
def index():
    return render_template("index.html")
    
@Titan.route("/about")
def about():
    return render_template("about.html")        
    
@Titan.route("/data")
def data():
    con = sqlite3.connect(File_path)
    cursor = con.cursor()
    Name = cursor.execute("SELECT * FROM Name").fetchall()
    con.close()
    return render_template("data_table_fillin.html", Name = Name)    
    
    
if __name__=="__main__":
    Titan.run(debug = True)   