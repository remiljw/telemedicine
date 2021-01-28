# TeleMedicine API

[![TeleMedicine](https://circleci.com/gh/remiljw/telemedicine.svg?style=svg)](https://circleci.com/gh/remiljw/telemedicine)
[![TeleMedicine](https://github.com/remiljw/telemedicine/workflows/Django%20CI/badge.svg)](https://github.com/remiljw/telemedicine/actions)

API built with DRF for a telemedicine app to book hospital appointments.

## Endpoints

### https://telemed-api.herokuapp.com/api/patientsignup/
- Anyone can access this endpoint, it is meant to register new patients into the system.

```
   payload =  { 
      'email' : 'test@test.com' ,
      'password' : 'iamapatient',
      'patient' : {
              'first_name' : 'John'
              'last_name' : 'Doe'
              'date_of_birth' : '1999-01-24' #Date_of_birth must be in 'YYYY-MM-DD' format.
              'address': '17, Highway Street, Lagos.'
              }
       } 
 ```
 ### https://telemed-api.herokuapp.com/api/signin/
 - All users sign in here and get JWT tokens, which are used to access the remaining endpoints.
 ```
  payload = {
                'email' : 'test@test.com'
                'password' : 'iamapatient'
               }
  response = {
                'token' : 'JWT TOKEN'
        }
 ```
 
 ### https://telemed-api.herokuapp.com/api/add-doctor/
 - Only Admin Users have access to this endpoint. They add doctors to the system. Token is needed for authentication, which is gotten from the `signin/` endpoint.
 ```
   payload =  { 
      'email' : 'doctor@test.com' ,
      'password' : 'iamadoctor',
      'doctor' : {
              'first_name' : 'Doctor'
              'last_name' : 'Who'
              'date_of_birth' : '1999-01-24' #Date_of_birth must be in 'YYYY-MM-DD' format.
              'address': '17, Highway Street, Lagos.'
              }
       } 
 ```
 
 ### https://telemed-api.herokuapp.com/api/doc-calendar/
 - Only doctors have access to this endpoint, they create their availability here. Token is needed for authentication, which is gotten from the `signin/` endpoint.
 ```
 payload = {
              'date': '2020-01-30' #date must be in 'YYYY-MM-DD' format.
              }
 ```
 
 ### https://telemed-api.herokuapp.com/api/appointment/
 - Can be accessed by all patients, to book appointments based on their doctor of choice availability. Date and Doctor fields accepts only integers which are the id of the doctor and the available date.
```
payload = {
      'doctor' : 1, #doctor_id
      'date' : 1, #date_id
      'reason_for_visit' : Sore Throat'
      'time' :  1  # options ranges from 1 - 5 as they stand for key for the value of time. ('1', '09:00 – 10:00'),
                                                                                               #('2', '10:00 – 11:00'),
                                                                                              # ('3', '11:00 – 12:00'),
                                                                                               #('4', '12:00 – 13:00'),
                                                                                               #('5', '13:00 – 14:00'),
      }
```
      
## Authentication
- All end points need authentication to access except `signin/` and `patient-signup/`.
- Get your token from the `signin/` endpoint and add it to the request headers.
```
    (Authorization : 'Bearer ' + yourtoken)
```
- You are good to go. 👍🏾

## Credentials
- Here is the credential for the admin
```
   email : drno@med.com
   password: bond007
```
