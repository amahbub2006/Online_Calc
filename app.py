from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    """
    Renders the calculator page and handles form submission.

    Handles both GET and POST requests. On GET requests, it renders the
    calculator page. On POST requests, it performs the calculation based
    on the user input and returns the result.
    """
    result = None
    if request.method == "POST":
        try:
            # Retrieve numbers and operation from form data
            num1 = float(request.form.get("num1", 0))
            num2 = float(request.form.get("num2", 0))
            operation = request.form.get("operation")

            # Perform the selected operation
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Division by zero"
            else:
                result = "Invalid operation"
        except ValueError:
            result = "Invalid input"

    # Render the calculator template with the result
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
