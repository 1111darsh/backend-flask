# backend-flask
This is a simple flask Application


    GET  tasks: Retrieves all tasks.
    GET  /tasks/<task_id>: Retrieves a specific task by its ID.
    POST  /tasks: Creates a new task.
    PUT  /tasks/<task_id>: Updates an existing task.
    PATCH  /tasks/<task_id>: Partially updates an existing task.
    DELETE  /tasks/<task_id>: Deletes an existing task.



flask app is running on the 5000 port 
### Docker 
```bash
docker run -d -p 5000:5000 --name backendflask  1111darsh/backend-flask:latest
```

Postman Collections [link](./backend-flask.postman_collection.json)