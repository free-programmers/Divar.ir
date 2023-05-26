# api doc



## Json only views 
#### the routes that required json request always return
   - {'error': 'Only JSON requests are accepted'} 
#### with status code 400


---
## Login view
### /auth/login/
#### content type json
#### params: 
    {
        "username":"user's username",
        "password": "user's password",
    }
#### return answer
- if username and password correct:
    

    {
        "accessToken":"access token",
        "refreshToken":"refresh token"
    } 
    status code: 200

- else :
    

    {
        "error": "invalid credential"
    }
    status code: 401

---