# TeleMedicine API

[![TeleMedicine](https://circleci.com/gh/remiljw/telemedicine.svg?style=svg)](https://circleci.com/gh/remiljw/telemedicine)
[![TeleMedicine](https://github.com/remiljw/telemedicine/workflows/Django%20CI/badge.svg)](https://github.com/remiljw/telemedicine/actions)

API built with DRF for a telemedicine app to book hospital appointments.

## Endpoints

### `patientsignup/`
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
 ### `signin/`
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
 
 ### `add-doctor/`
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
 
 ### `doc-calendar/`
 - Only doctors have access to this endpoint, they create their availability here. Token is needed for authentication, which is gotten from the `signin/` endpoint.
 ```
 payload = {
              'date': '2020-01-30' #date must be in 'YYYY-MM-DD' format.
              }
 ```
 
 ### `appointment/`
 - Can be accessed by all patients, to book appointments based on their doctor of choice availability. Date and Doctor fields accepts only integers which are the id of the doctor and the available date.
```
payload = {
      'doctor' : 'doctor_id',
      'date' : 'date_id',
      'reason_for_visit' : Sore Throat'
      'time' :  '' 
      }
```
      
## Authentication
- All end points need authentication to access except `signin/` and `patient-signup/`.
- Get your token from the `signin/` endpoint and add it to the request headers.
```
    (AUTHORIZATION='Bearer ' + yourtoken)
```
- You are good to go. 👍🏾
