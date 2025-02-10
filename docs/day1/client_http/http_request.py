import requests

result = requests.get('http://example.com/index.html')
print(result.text)
print(result.status_code)
print('headers', result.headers, end='\n\n') 
print("content" , result.content)


# pode se utilizar o httpx mais moderno e mais rapido que o requests
