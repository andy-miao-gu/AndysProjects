import io
import base64
import matplotlib.pyplot as plt
from flask import Flask, render_template, make_response

app = Flask(__name__)

# Function to generate a Matplotlib bar chart
def generate_bar_chart():
    data = [5, 10, 15, 20, 25]
    labels = ['A', 'B', 'C', 'D', 'E']
    
    plt.figure(figsize=(8, 4))
    plt.bar(labels, data)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Bar Chart')
    
    # Convert the plot to a base64-encoded PNG image
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_data = base64.b64encode(img_buffer.read()).decode('utf-8')
    plt.close()
    
    return img_data

# Function to generate a Matplotlib line chart
def generate_line_chart():
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 25, 15, 30]
    
    plt.figure(figsize=(8, 4))
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Chart')
    
    # Convert the plot to a base64-encoded PNG image
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='jpeg')
    img_buffer.seek(0)
    img_data = base64.b64encode(img_buffer.read()).decode('utf-8')
    plt.close()
    
    return img_data

@app.route('/')
def index():
    bar_chart = generate_bar_chart()
    line_chart = generate_line_chart()
    
    return render_template('index.html', bar_chart=bar_chart, line_chart=line_chart)

if __name__ == '__main__':
    app.run(debug=True)
