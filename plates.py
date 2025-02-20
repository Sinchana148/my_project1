from flask import Flask, render_template, request
app = Flask(__name__)
# Example helper function to generate a payment confirmation message
def get_custom_message():
    return "Your payment of $100 has been successfully processed!"
@app.route("/dashboard", methods=["GET", "POST"])
def home():
    amount = None
    message = None
    if request.method == "POST":
        try:
            # Get user input from the form
            input1 = int(request.form["plates"])  # Number of plates
            input2 = request.form["shape"].lower()  # Plate shape
            # Calculate amount
            amount = input1 * 2  # Assuming each plate costs $2
            if input2 == "circle" or input2 == "square":
                message = "Thank you for your order! Your order will be placed soon."
            else:
                message = f"Sorry! Plates of shape {input2} are not available, please select from the above choices."
        except Exception as e:
            message = f"Error processing your order: {str(e)}"
    return render_template("dashboard.html", amount=amount, message=message)
if __name__ == "_main_":
    app.run(debug=True)
