# api doc



## Json only views 
#### the routes that required json request always return
   - {'error': 'Only JSON requests are accepted'} 
#### with status code 400


---
## Register view
### /auth/api/Register/
#### content type json / POST
#### params: 
    {
        "phonenumber" : "user's phone number",
    }

#### return response
- if phone number is already have account:

    
    {
        "error": "Account already Exists"
    }
    status code: 409

else:

        at this point user added to db and a sms with a verify code send 
        to user phone number the  code is valid for 5 minute 

        {
            "message": "User Created Successfully",
            "phone": "user phone number",
            "token": "eb3ed707-f72e-4271-930a-a6e5c89f0ca0"
        }
        status code :200

---


## Verify user account
### /auth/api/verify/
#### content type json / POST
params :
        
        {
            "code":code that user type in,
            "token":token that user get when created an account,
            "phone":user phone number
        }

return response:

    if is any params missing it always return error
    
    otherwise if code or token is in valid it return an error with 400

if everything is ok verified user account and return 

    {
	"message": "User verify Successfully!"
    }   
    status code : 200


---

## Login to account
### /auth/api/login/
#### content type json / POST

params:
        
        {
            "phone":"users phone number"
        }

if phone number is not belong to any user

response: 
        
        {
            "error": "User does not exist"
        }, status_code:404

if user exists and every thins goes ok

response:
        
        {
            "expire_time": "300",
            "message": "Code Send to user",
            "user_id": "587c0bae-5a92-4c75-a2a8-ce1e164bcaf5" # user unique public key
        }, 200
user_id is user unique publicKey for verify login code this token should send as well


if user one time enter its phone number for login
and try again shortly after then server response will be (when user enter its phone number for getting login code, user should wait 5 minute till user can request for code agian)

response:
    
    {
        "message": "User already have a request for login"
    }, 429


---
## Resend Login Code

### for this simply after 5 minute time for user, just simply call login view again

---

## Verify Login Code
### /auth/api/login/verify/
#### content type json / POST


params:

    {
        "code":"code that sends to user phone",
        "user_id": "user_id that recived from login view",
    }

if users that belong to  user_id is not requesting login code:

        {
            "error": "login first"
        }, 400
        

if code is ok and valid :

        {
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4OTAxMDgwOCwianRpIjoiZDY3Nzk2MDctMDc2Ni00Yzk0LTg5ZTAtYzFlNGU3Nzg5NjIwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjU4N2MwYmFlLTVhOTItNGM3NS1hMmE4LWNlMWUxNjRiY2FmNSIsIm5iZiI6MTY4OTAxMDgwOCwiZXhwIjoxNjkwMzA2ODA4fQ.Kj7Fq4Hea4AnpKWoHFvbSUqR41gtkyLqWJzXBE8O1lk",
            "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4OTAxMDgwOCwianRpIjoiMWVhM2MxNzctYjk2Yy00ZTc1LThhZjEtZjdjYTA3NTU1MTBjIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiI1ODdjMGJhZS01YTkyLTRjNzUtYTJhOC1jZTFlMTY0YmNhZjUiLCJuYmYiOjE2ODkwMTA4MDgsImV4cCI6MTY5MDM5MzIwOH0.FCt1VPOEUVcqwZHrhXvV7D3tcNWBjn2cFxUmlZ1szLo"
        }, 200





