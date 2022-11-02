import requests
import json

def get_something():
    request = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print("get something: ")
    print("status code response: ", request.status_code)
    print("content response: ", request.content)
    all_fields = json.loads(request.content)
    print(all_fields)

def get_all():
    request = requests.get("https://jsonplaceholder.typicode.com/todos")
    print("get all: ")
    print("status code response: ", request.status_code)
    print("content response: ", request.content)
    all_fields = json.loads(request.content)
    print(all_fields)

def delete_something():
    request = requests.delete("https://jsonplaceholder.typicode.com/todos/1")
    print("delete something: ")
    print("status code response: ", request.status_code)

def post_something():
    json = {
        'title':'foo',
        'body': 'test',
        'userId': 1
    }
    request = requests.post("https://jsonplaceholder.typicode.com/todos", json)
    print("post something: ")
    print("status code response: ", request.status_code)
    print("content response: ", request.content)

def update_something():
    json = {
        'title':'foo',
        'body': 'test 2',
        'userId': 1
    }
    request = requests.put("https://jsonplaceholder.typicode.com/todos/1", json)
    print("update something: ")
    print("status code response: ", request.status_code)
    print("content response: ", request.content)

    json = {
        'title':'foo',
        'body': 'test 2',
    }
    request = requests.patch("https://jsonplaceholder.typicode.com/todos/1", json)
    print("patching something: ")
    print("status code response: ", request.status_code)
    print("content response: ", request.content)

def nested_resource():
    request = requests.get("https://jsonplaceholder.typicode.com/todos/1/comments")
    print("nested resource: ")
    print("status code response: ", request.status_code)
    print("content response: ", request.content)
    all_fields = json.loads(request.content)
    print(all_fields)

def filter_something():
    request = requests.get("https://jsonplaceholder.typicode.com/posts?userId=1")
    print("filter something: ")
    print("status code response: ", request.status_code)
    print("content response: ", request.content)
    all_fields = json.loads(request.content)
    print(all_fields)

if __name__ == '__main__':
    get_something()
    get_all()
    delete_something()
    post_something()
    update_something()
    nested_resource()
    filter_something()


