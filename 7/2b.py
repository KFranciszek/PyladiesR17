import requests

save_result = requests.post(
    'http://localhost:5000/user/aa/set-password',
    json={'passwd': '12345'}
)
print(save_result.text)

login = requests.post(
    'http://localhost:5000/user/aaa/login',
    json={'passwd': '12345'}
)
print(login.text)
