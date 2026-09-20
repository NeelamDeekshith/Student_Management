from flask import Flask,render_template,request
import sqlite3

# ----------------------------db_conection-----------------------------------

db = sqlite3.connect('Student_database_file.db', check_same_thread=False)

db.execute('''create table if not exists student(
            id int primary key,
            name varchar(50),
            age int,
            course varchar(10));''')

app = Flask(__name__)

# -------------------------root_page--------------------------------------

@app.route('/', methods=['POST', 'GET'])

def mainf():
    return render_template('base.html')

# ----------------------------add_student-----------------------------------

@app.route('/add_student', methods=['POST', 'GET'])

def add_student():
    msg = None
    if request.method == 'POST':
        
        student_id = request.form['id']
        name = request.form['name']
        age = request.form['age']
        course = request.form['course']
        
        try:

            if student_id and name and age and course:
                
                age = int(age)
                query = f"insert into student(id, name, age, course) values (?,?,?,?)"
                db.execute(query,(student_id,name,age,course))
                db.commit() 
                
                msg = "Student added successfully!"
                
        except sqlite3.IntegrityError:
            msg = "Student with this ID already exists."

        except Exception as e:
            msg = f"Error: {e}"
            
    return render_template('add_student.html',msg = msg)

# ---------------------------search_student---------------------------------------------

@app.route("/search_student", methods=["GET", "POST"])
def search_student():
    students = []
    msg = ''

    if request.method == 'POST':
        if 'search' in request.form:
            search_by = request.form["choice"]
            search_value = request.form["value"]

            if search_by and search_value:
                try:
                    if search_by == "id" or search_by == "age":
                        search_value = int(search_value)

                    query = f"SELECT * FROM student WHERE {search_by} = ?;"
                    students = db.execute(query, (search_value,)).fetchall()

                    if not students:
                        msg = "No student found!"
                except Exception as e:
                    msg = f"Error: {e}"
            else:
                msg = "Please fill input field."

        elif 'show_all' in request.form:
            try:
                students = db.execute("SELECT * FROM student").fetchall()
            except Exception as e:
                msg = f"Error: {e}"

    return render_template("search_student.html", students=students, msg=msg)


# ------------------------------update_student---------------------------------

@app.route("/update_student",methods=["GET", "POST"])
def update_student():
    msg = ''
    if request.method == 'POST':
        try:
            choice = request.form["choice"]
            id = request.form["id"]
            value = request.form["value"]

            if id and choice and value:   
                if choice == "age":
                    value = int(value)

                if choice == "id":
                    id = int(id)
                    
                exists = db.execute("SELECT 1 FROM student WHERE id = ?", (id,)).fetchone()
                
                if exists:
                    query = f'update student set {choice} = ? where id = ?;'
                    db.execute(query,(value,id))
                    db.commit()
                    msg = f"Student {choice} with {value} updated successfully!"

                else:
                    msg = f"No student found with ID {id}."
        except Exception as e:
            msg = f"Error: {e}"

    return render_template("update_student.html",msg = msg)

# ---------------------------delete_student------------------------------------

@app.route("/delete_student", methods=["GET", "POST"])
def delete_student():
    msg = ''
    if request.method == 'POST':
        id = request.form["id"]

        try:
            
            query_check = "select count(*) from student where id = ?"
            count = db.execute(query_check, (id,)).fetchone()[0]

            if count > 0:
                
                query_delete = "DELETE FROM student WHERE id = ?"
                db.execute(query_delete, (id,))
                db.commit()
                msg = f"Student with ID {id} deleted successfully!"
            else:
                msg = f"Student with ID {id} not found!"

        except Exception as e:
            msg = f"Error deleting student: {e}"

    return render_template("delete_student.html", msg=msg)

# ---------------------------Entry_point------------------------------------

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
    db.close()
    
# ----------------------------END-----------------------------------
