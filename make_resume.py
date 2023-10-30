import weasyprint

# Load the HTML file with the filled resume
# resume_html = 'rendered_resume.html'
resume_html = 'templates/1/index.html'


# Define the output PDF file path
output_pdf = 'resume.pdf'

# Calculate A4 paper size in inches
a4_width_in_inches = 8.27
a4_height_in_inches = 11.7

# Define custom margin values (adjust as needed)
top_margin = 0.10  # inches
bottom_margin = 0.10  # inches
left_margin = 0.10  # inches
right_margin = 0.10  # inches

# Create a WeasyPrint HTML object
resume_pdf = weasyprint.HTML(resume_html)

# Set the paper size and margins
resume_pdf.write_pdf(
    target=output_pdf,
    # stylesheets=['style.css'],
    stylesheets=['templates/1/styles.css'],

    presentational_hints=True,
    page_size=(f'{a4_width_in_inches}in', f'{a4_height_in_inches}in'),
    margin=(f'{top_margin}in', f'{right_margin}in', f'{bottom_margin}in', f'{left_margin}in')
)

print(f"PDF resume generated at {output_pdf}")
