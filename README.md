# schedule_api
Scheduling system with Django Rest Framework (DRF).

This application uses Python3 (3.6.4) and requires:

* Django==2.0.1
* djangorestframework==3.7.7
* model-mommy==1.5.1
* pip==9.0.1
* pytz==2017.3

This project was created on macOS High Sierra (10.13.3) and Tested on same mac and a distro Debian (9.3.0).

Need to run migrations!

### API Interaction
I decided to use generic class-based Views, as it is so much simpler. For testing porpouses, there is no authentication, so any access is anonimously. The implementation have support for just 1 doctor, so all schedules are based in one "calendar".

Tests are implemented in the folder `/scheduler/tests/`.

All the expected and required HTTP methods (GET, POST, PUT, DELETE) can be accessed with curl as seen above:

|EndPoint         |HTTP Method  |CRUD Method  |Result                   |
|:----------------|:------------|:------------|:------------------------|
|patients/        | GET         | READ        | Get all patients        |
|patient/id       | GET         | READ        | Get a single patient    |
|patients/        | POST        | CREATE      | Add a single patient    |
|patient/id       | PUT         | UPDATE      | Update a single patient |
|patient/id       | DELETE      | DELETE      | Delete a single patient |

If there is no patient in the DB, you can create one:

`curl -X POST http://localhost:8000/patients/ -H 'content-type:application/json' -d '{"id_number": 1, "name": "Leonardo", "age": 35}'`

The patient previously entered can now be retrieved with:

`curl -X GET http://localhost:8000/patient/1/ -H 'Aceppt:application/json'`

where `/patient/1/` is the first patient, and all patients stored can be retrieved with:

`curl -X GET http://localhost:8000/patients/ -H 'Aceppt:application/json'`

Now, appointments can be used!

|EndPoint         |HTTP Method  |CRUD Method  |Result                      |
|:----------------|:------------|:------------|:---------------------------|
|appointments/    | GET         | READ        | Get all appointments       |
|appointments/id  | GET         | READ        | Get a single appointment   |
|appointments/    | POST        | CREATE      | Add a single appointment   |
|appointments/id  | PUT         | UPDATE      | Update a single appointment|
|appointments/id  | DELETE      | DELETE      | Delete a single appointment|

##### Scheduling lists, containing all schedules with all Patients that has schedules
`curl -X GET http://localhost:8000/appointments/ -H 'Aceppt:application/json`

##### Scheduling detais, containing all the information of a patient's appointment
`curl -X GET http://localhost:8000/appointment/1/ -H 'Aceppt:application/json'`

##### Scheduling storage, where it is possible to insert new appointments
`curl -X POST http://127.0.0.1:8000/appointments/ -H 'content-type:application/json' -d '{"date": "01/03/2018", "start_time": "08:00", "end_time": "09:00", "procedure": "Consulta", "patient": 2}'`

##### Scheduling updates, if any updates should be done
`curl -X PUT http://127.0.0.1:8000/appointment/1/ -H 'content-type:application/json' -d '{"date": "01/03/2018", "start_time": "08:10", "end_time": "09:00", "procedure": "Consulta", "patient": 2}'`

##### Scheduling deletes
`curl -X DELETE http://127.0.0.1:8000/appointment/1/`

and of course if it is needed, any patient can be updated too:

`curl -X PUT http://localhost:8000/patient/3/ -H 'content-type:application/json' -d '{"id_number": 3, "name": "Sérgio", "age": 24}`

