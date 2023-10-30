from jinja2 import Environment, FileSystemLoader
import json

# Load data from a JSON file
with open('sample.json', 'r') as file:
    data = json.load(file)

# Define the Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
# template = env.get_template('resume_template.html')
template = env.get_template('templates/1/index.html')


# Render the template with data
rendered_template = template.render(data)

# Save the rendered HTML to a file
with open('rendered_resume.html', 'w') as file:
    file.write(rendered_template)

print("Rendered resume HTML generated at rendered_resume.html")
