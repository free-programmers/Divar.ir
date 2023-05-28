# api doc



## Json only views 
#### the routes that required json request always return
   - {'error': 'Only JSON requests are accepted'} 
#### with status code 400


---
## Register view
### /auth/api/Register/
#### content type json
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