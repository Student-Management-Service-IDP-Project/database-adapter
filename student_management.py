from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient(host='mongodb',
                     port=27017,
                     username='school',
                     password='schoolpassword',
                     authSource='school')
db = client['school']

# Route for teachers to add students to a course
@app.route('/teacher/add_student', methods=['POST'])
def add_student_to_course():
    data = request.json
    db.students.insert_one(data)
    return jsonify({"message": "Student added successfully"})


# Route for teachers to add courses
@app.route('/teacher/add_course', methods=['POST'])
def add_course():
    data = request.json
    db.courses.insert_one(data)
    return jsonify({"message": "Course added successfully"})


# Route for teachers to add grades to students
@app.route('/teacher/add_grade', methods=['POST'])
def add_grade():
    data = request.json
    db.grades.insert_one(data)
    return jsonify({"message": "Grade added successfully"})


# Route for teachers to upload materials for a course
@app.route('/teacher/upload_material', methods=['POST'])
def upload_material():
    data = request.json
    db.materials.insert_one(data)
    return jsonify({"message": "Material uploaded successfully"})


# Route for students to view grades
@app.route('/student/grades', methods=['GET'])
def view_grades():
    data = request.json
    username = data.get('username')
    course_name = data.get('course_name')
    grade = db.grades.find_one({"username": username, "course_name": course_name})
    if grade:
        return jsonify({"grade": grade["grade"]})
    else:
        return jsonify({"message": "Grade not found"}), 404


# Route for students to view their courses
@app.route('/student/courses', methods=['GET'])
def view_courses():
    data = request.json
    username = data.get('username')
    
    # Find all students with the specified username
    students = db.students.find({"username": username})
    
    # Initialize an empty list to store course names
    course_list = []
    
    # Iterate over the students and add their course names to the list
    for student in students:
        course_list.append(student.get("course_name"))
    
    if course_list:
        return jsonify({"courses": course_list})
    else:
        return jsonify({"message": "No courses found for the student"}), 404
    
@app.route('/student/materials', methods=['GET'])
def view_materials():
    data = request.json
    course_name = data.get('course_name')
    
    # Find all courses with the specified course name
    courses = db.materials.find({"course_name": course_name})
    
    # Initialize an empty list to store materials
    material_list = []
    
    # Iterate over the courses and add their materials to the list
    for course in courses:
        material_list.append(course.get("data"))
        
    if material_list:
        return jsonify({"materials": material_list})
    else:
        return jsonify({"message": "No materials found for the course"}), 404


@app.route('/student/course_details', methods=['GET'])
def view_course_details():
    data = request.json
    course_name = data.get('course_name')
    
    
    # Find the course with the specified course name
    course = db.courses.find_one({"course_name": course_name})
    
    if course:
        return jsonify({"course_name": course.get("course_name"), "weekday": course.get("weekday"),"start hour": course.get("start_hour"), "end hour": course.get("end_hour"), "location": course.get("location"), "max students": course.get("max_students")})
    else:
        return jsonify({"message": "Course not found"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
