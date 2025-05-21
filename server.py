# Import the Flask class from the flask module
from flask import Flask, make_response
from flask import make_response
from flask import request
from data import data

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return "hello world"

@app.route("/no_content")
def no_content(): 
    """return 'No content found' with a status of 204

    Returns:
        string: No content found
        status code: 204
    """
    return ({"message": "No content found"}, 204)

@app.route("/exp")
def index_explicit():
    """return 'Hello World' message with a status code of 200
    Returns:
        string: Hello World
        status code: 200
    """

    resp = make_response({"Message":"Hello Germany"})
    resp.status_code = 200
    return resp


@app.route("/data")
def get_data():
    try:
        # Check if 'data' exists and has a length greater than 0
        if data and len(data) > 0:
            # Return a JSON response with a message indicating the length of the data
            return {"message": f"Data of length {len(data)} found"}
        else:
            # If 'data' is empty, return a JSON response with a 500 Internal Server Error status code
            return {"message": "Data is empty"}, 500
    except NameError:
        # Handle the case where 'data' is not defined
        # Return a JSON response with a 404 Not Found status code
        return {"message": "Data not found"}, 404

@app.route("/name_search") 
def name_search():
    """Find a person in the database.
    Returns:
        json: Person if found, with status of 200
        404: If not found
        400: If argument 'q' is missing
        422: If argument 'q' is present but invalid
    """


    # Get the argument 'q' from the query parameters of the request
    query = request.args.get("q")

    # Check if the query parameter 'q' is missing
    if query is None:
        return {"message": "Query parameter 'q' is missing"}, 400

    # Check if the query parameter is present but invalid (e.g., empty or numeric)
    if query.strip() == "" or query.isdigit():
        return {"message": "Invalid input parameter"}, 422

    # Iterate through the 'data' list to look for the person whose first name matches the query
    for person in data:
        if query.lower() in person["first_name"].lower():
            # If a match is found, return the person as a JSON response with a 200 OK status code
            return person, 200

    # If no match is found, return a JSON response with a message indicating the person was not found and a 404 Not Found status code
    return{"Message": "Person not found"}, 400               

@app.route("/count")
def count():
    try:
        # Attempt to return a JSON response with the count of items in 'data'
        # Replace {insert code to find length of data} with len(data) to get the length of the 'data' collection
        return {"data count": len(data)}, 200
    except NameError:
        # If 'data' is not defined and raises a NameError
        # Return a JSON response with a message and a 500 Internal Server Error status code
        return {"Message": "data is not defined"}, 500        

@app.route("/person/<var_name>")
def find_by_uuid(var_name):
    # Iterate through the 'data' list to search for a person with a matching ID
    for person in data:
      # Check if the 'id' field of the person matches the 'var_name' parameter
      if person["id"] == str(var_name):
        # Return the person as a JSON response if a match is found
        return person
    # Return a JSON response with a message and a 404 Not Found status code if no matching person is found
    return {"Message": "Person is not found"}, 404    


@app.route("/person/<var_name>", methods=["DELETE"])
def delete_by_uuid(var_name):
    for person in data:
        if person["id"] == str(var_name):
            # Remove the person from the data list
            data.remove(person)
            # Return a JSON response with a message and HTTP status code 200 (OK)
            return {"Message": "Person with desired Id is deleted"}, 200
    # If no person with the given ID is found, return a JSON response with a message and HTTP status code 404 (Not Found)
    return {"Message": "person is not found"}, 404        


@app.route("/person", methods = ["POST"])
def create_person():
   # Get the JSON data from the incoming request 
   new_person = request.get_json()
   # Check if the JSON data is empty or None
   if not new_person:
        return {"Message":"Data is invalid"}, 422
    # Proceed with further processing of 'new_person', such as adding it to a database
    # or validating its contents before saving it
   try:
        data.append(new_person)
   except NameError:
         return{"message":"Data is not defined"}, 500       
   # Assuming the processing is successful, return a success message with status code 200 (Created)
   return{"Message":"New person is being added"}, 200     

    
@app.errorhandler(404)
def api_not_found(error):
    # This function is a custom error handler for 404 Not Found errors
    # It is triggered whenever a 404 error occurs within the Flask application
    return {"Message":"Api has not found"}, 404
