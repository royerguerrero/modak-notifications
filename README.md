<center>
    <h1>📬 Modak Notification</h1>
    <small>Solution for Modak technical exercise backend developer</small>
</center>

## Setup

Requirements
- Python3.7 or higher
- Pip

1. Install dependencies
   ```
   pip install -r dev-requirements.txt
   ```


You can run the tests just using `pytest`


This project use a DDD architecture. I only implemented the domain layer 🙃 the time play me dirty. I would like to have implemented other layers like infra and application for show the consumption from the application layer obviously you can see the use of the notification aggregate. anyway I implemented unit of work partially (only the port) to later link it to a redis or memory repository 