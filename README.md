## Database Adapter

### API

#### What teachers can do:


Add a student:
**POST /teacher/add_student**

`> Body:`
```
{
    username: "Maria Garcia",
    course_name: "Chemestry"
}
```

`> Response:`

*  `200 OK`
```
{
    "message": "Student added successfully"
}
```
*  `400 BAD REQUEST`


Add a course: 
**POST /teacher/add_course**

`> Body:`
```
{
    course_name: "Computer Science",
    weekday: "Friday",
    start_hour: "15:00",
    end_hour: "17:00",
    location: "CS104",
    max_students: "70"
}
```

`> Response:`

*  `200 OK`
```
{
    "message": "Course added successfully"
}
```
*  `400 BAD REQUEST`

Add a grade:
**POST /teacher/add_grade**

`> Body:`
```
{
    username: "Maria Garcia",
    course_name: "Chemestry",
    grade: 8
}
```
`> Response:`

*  `200 OK`
```
{
    "message": "Grade added successfully"
}
```
*  `400 BAD REQUEST`

Add a course material:
**POST /teacher/upload_material**

`> Body:`
```
{
    course_name: "Chemestry",
    data: "Atomic Structure Chapter 2"
}
```

`> Response:`

*  `200 OK`
```
{
    "message": "Material uploaded successfully"
}
```
*  `400 BAD REQUEST`

#### What students can do:
View grades: 
**GET /student/grades**

```
{
    "username": "Emil Johnson",
    "course_name": "Physics"
}
```

`> Response:`

* `200 OK`
```
{
    grade: 9
}
```
*  `400 BAD REQUEST`
```
{
    "message": "Grade not found"
}
```

View student's courses:
**GET /student/courses**

`> Body:`
```
{
    username: "Maria Garcia",
}
```

`> Response:`

* `200 OK`
```
{
    "courses": [
        "Chemestry"
    ]
}
```
*  `400 BAD REQUEST`
```
{
    "message": "No courses found for the student"
}
```

View course materials:
**GET /student/materials**

`> Body:`
```
{
    course_name: "Chemestry",
}
```

`> Response:`

* `200 OK`
```
{
    "materials": [
        "Chemical Reactions Chapter 1",
        "Atomic Structure Chapter 2"
    ]
}
```
*  `400 BAD REQUEST`
```
{
    "message": "No materials found for the course"
}
```

View course details:
**GET /student/course_details**

`> Body:`
```
{
    course_name: "Chemestry",
}
```

`> Response:`

* `200 OK`
```
{
    "course": {
        "weekday": "Monday",
        "start_hour": "10:00",
        "end_hour": "12:00",
        "location": "CS101",
        "max_students": "50"
    }
}
```
*  `400 BAD REQUEST`
```
{
    "message": "Course not found"
}
```
