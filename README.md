## Database Adapter

### API

Add student:
**POST /student**

`> Body:`
```
{
    username: "joedoe",
    course_name: "Analiza Matematica"
}
```

`> Response:`

*  `200 OK`
*  `400 BAD REQUEST`


Add course: **POST /course**

`> Body:`
```
{
    course_name: "Analiza Matematica",
    weekday: "Monday",
    start_hour: "10:00",
    end_hour: "12",
    location: "EC105",
    max_students: "120"
}
```

`> Response:`

*  `200 OK`
*  `400 BAD REQUEST`

Add grade: **POST /student/grades**

`> Body:`
```
{
    username: "joedoe",
    course_name: "Analiza Matematica",
    grade: 10
}
```
`> Response:`

*  `200 OK`
*  `400 BAD REQUEST`

Add course material: **POST /course/materials**

`> Body:`
```
{
    course_name: "Analiza Matematica",
    data: "Lorem Ipsum..."
}
```

`> Response:`

*  `200 OK`
*  `400 BAD REQUEST`


View grades: **GET /student/grades**

```
{
    username: "joedoe",
    course_name: "Analiza Matematica"
}
```
`> Response:`
* `200 OK`
```
{
    grade: 10
}
```
*  `400 BAD REQUEST`

View student's courses: **GET /student/courses**

`> Body:`
```
{
    username: "joedoe",
}
```
`> Response:`
* `200 OK`
```
{
    courses: [
        "Analiza Matematica",
        "Algebra Liniara",
        "Programare 1"
    ]
}
```
*  `400 BAD REQUEST`
