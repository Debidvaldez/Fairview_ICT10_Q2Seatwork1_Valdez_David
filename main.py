from pyscript import document, display

def gwa_calculation(e):
    document.getElementById('student_info').innerHTML = "student_info";
    document.getElementById('grade_summary').innerHTML = "grade_summary";
    document.getElementById('GWA').innerHTML = "GWA";

    firstname = document.getElementById('1stname').value
    lastname = document.getElementById('lastname').value

    subjects = ['science', 'math', 'english', 'filipino', 'ict', 'pe']

    science = float(document.getElementById('science').value)
    math = float(document.getElementById('math').value)
    english = float(document.getElementById('english').value)
    filipino = float(document.getElementById('filipino').value)
    ict = float(document.getElementById('ict').value)
    pe = float(document.getElementById('pe').value)

    subject_weights = (5, 3, 2, 1)
    total_score = (science * subject_weights[0] + math * subject_weights[0] + english * subject_weights[0] + filipino * subject_weights[1] +ict * subject_weights[2] + pe * subject_weights[3])

    summary = f""" {subjects[0]}: {science}
    {subjects[1]}: {math}
    {subjects[2]}: {english}
    {subjects[3]}: {filipino}
    {subjects[4]}: {ict}
    {subjects[5]}: {pe} """

    document.getElementById('student_info').innerHTML = f"Name: {firstname} {lastname}"
    document.getElementById('grade_summary').innerHTML = summary
    document.getElementById('GWA').innerHTML = f"Your General Weighted Average (GWA) is: {total_score:.2f}"