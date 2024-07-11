## 0x10-python-network_0
This repository contains Bash scripts for working with cURL. The scripts perform various tasks such as:

- Displaying the size of the body of a response
- Displaying the body of a response
- Sending DELETE requests
- Displaying accepted HTTP methods
- Sending GET requests with headers
- Sending POST requests with parameters

### Files
- `0-body_size.sh`: Displays the size of the body of a response in bytes
- `1-body.sh`: Displays the body of a response
- `2-delete.sh`: Sends a DELETE request to a URL
- `3-methods.sh`: Displays accepted HTTP methods
- `4-header.sh`: Sends a GET request with a header variable
- `5-post_params.sh`: Sends a POST request with email and subject parameters

### Usage
Run each script followed by the URL and any required parameters. For example:

```
./0-body_size.sh 0.0.0.0:5000
./1-body.sh 0.0.0.0:5000/route_1
./2-delete.sh 0.0.0.0:5000/route_3
./3-methods.sh 0.0.0.0:5000/route_4
./4-header.sh 0.0.0.0:5000/route_5
./5-post_params.sh 0.0.0.0:5000/route_6
```

### Note
Please test the scripts in the sandbox provided, using the web server running on port 5000.