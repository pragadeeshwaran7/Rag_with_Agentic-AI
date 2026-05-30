import markdown2
import tempfile
import os
from weasyprint import HTML, CSS

def export_to_pdf(markdown_content: str) -> str:
    """
    Converts markdown question paper to PDF and returns the path to the saved file.
    """
    # Convert markdown to HTML
    html_body = markdown2.markdown(markdown_content)
    
    # Wrap in basic HTML structure with styling
    html_content = f"""
    <html>
    <head>
        <style>
            body {{ font-family: 'Times New Roman', Times, serif; margin: 40px; font-size: 14px; line-height: 1.6; }}
            h1 {{ text-align: center; font-size: 24px; text-transform: uppercase; }}
            h2 {{ text-align: center; font-size: 20px; text-decoration: underline; margin-top: 30px; }}
            h3 {{ font-size: 18px; margin-top: 25px; }}
            p, li {{ text-align: justify; }}
            .marks {{ float: right; font-weight: bold; }}
            .instructions {{ font-style: italic; margin-bottom: 20px; }}
        </style>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """
    
    # Save to a temporary file
    fd, path = tempfile.mkstemp(suffix=".pdf")
    os.close(fd)
    
    # Generate PDF
    HTML(string=html_content).write_pdf(path)
    
    return path
