#!/usr/bin/env python3
"""
Metro TV & Appliances - HTML Header Generator
Creates uniform headers for service portal HTML pages
"""

from datetime import datetime


def get_metro_tv_styles():
    """Returns the standard Metro TV & Appliances CSS styles"""
    return """        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Times New Roman', serif;
            color: #000000;
            background-color: #F5F0E8;
            min-height: 100vh;
            padding: 30px;
            line-height: 1.6;
        }

        .header {
            background-color: #B71C1C;
            color: #FFFFFF;
            padding: 30px;
            text-align: center;
            border-radius: 8px;
            margin-bottom: 40px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }

        .header h1 {
            font-size: 42pt;
            font-weight: bold;
            margin-bottom: 10px;
            font-family: 'Times New Roman', serif;
        }

        .header p {
            font-size: 20pt;
            font-family: 'Times New Roman', serif;
        }

        .container {
            max-width: 1600px;
            margin: 0 auto;
        }

        .section-card {
            background-color: #FFFFFF;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            margin-bottom: 40px;
        }

        .section-title {
            font-size: 28pt;
            color: #000000;
            margin-bottom: 30px;
            font-weight: bold;
            font-family: 'Times New Roman', serif;
            border-bottom: 3px solid #B71C1C;
            padding-bottom: 10px;
        }

        .button-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 25px;
        }

        .service-button {
            min-height: 120px;
            font-size: 18pt;
            font-family: 'Times New Roman', serif;
            font-weight: normal;
            background-color: #B71C1C;
            color: #FFFFFF;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .service-button:hover {
            background-color: #8B0000;
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }

        .service-button:active {
            background-color: #6D0000;
            transform: translateY(0);
        }

        .info-banner {
            background-color: #FFF3E0;
            border-left: 6px solid #B71C1C;
            padding: 25px;
            margin-bottom: 40px;
            border-radius: 4px;
        }

        .info-banner p {
            font-size: 18pt;
            color: #000000;
            font-family: 'Times New Roman', serif;
            margin: 0;
        }

        .footer {
            text-align: center;
            margin-top: 50px;
            padding: 30px;
            background-color: #FFFFFF;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }

        .footer p {
            font-size: 16pt;
            color: #000000;
            font-family: 'Times New Roman', serif;
            margin: 8px 0;
        }

        .footer .version {
            font-weight: bold;
            color: #B71C1C;
        }

        @media (max-width: 1024px) {
            .button-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 768px) {
            .button-grid {
                grid-template-columns: 1fr;
            }
        }"""


def get_html_head(title, additional_styles=""):
    """
    Generate HTML head section with Metro TV styling

    Args:
        title: Page title
        additional_styles: Any additional CSS styles specific to this page

    Returns:
        HTML head section as string
    """
    styles = get_metro_tv_styles()
    if additional_styles:
        styles += f"\n\n{additional_styles}"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
{styles}
    </style>
</head>"""


def get_header(title, subtitle):
    """
    Generate Metro TV header banner

    Args:
        title: Main header title (e.g., "METRO TV & APPLIANCES")
        subtitle: Subtitle text (e.g., "Service Portal")

    Returns:
        HTML header section as string
    """
    return f"""        <!-- Header -->
        <div class="header">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>"""


def get_footer(version="1.2"):
    """
    Generate Metro TV footer

    Args:
        version: Version number for the portal

    Returns:
        HTML footer section as string
    """
    current_date = datetime.now().strftime("%B %Y")

    return f"""        <!-- Footer -->
        <div class="footer">
            <p class="version">Metro TV & Appliances Service Portal v{version}</p>
            <p>Last Updated: {current_date}</p>
            <p style="font-size: 14pt; margin-top: 15px;">For assistance, contact your supervisor or IT support.</p>
        </div>"""


def generate_complete_page(page_title, header_title, header_subtitle, content, version="1.2", additional_styles=""):
    """
    Generate a complete HTML page with uniform Metro TV styling

    Args:
        page_title: Title for the <title> tag
        header_title: Main header text
        header_subtitle: Subtitle for header
        content: Body content (HTML string)
        version: Portal version number
        additional_styles: Additional CSS styles if needed

    Returns:
        Complete HTML page as string
    """
    head = get_html_head(page_title, additional_styles)
    header = get_header(header_title, header_subtitle)
    footer = get_footer(version)

    return f"""{head}
<body>
    <div class="container">
{header}

{content}

{footer}
    </div>
</body>
</html>"""


def main():
    """Example usage of the header generator"""

    # Example: Create a simple page
    content = """        <!-- Info Banner -->
        <div class="info-banner">
            <p><strong>Example Page:</strong> This page was generated using the uniform header script.</p>
        </div>

        <!-- Example Section -->
        <div class="section-card">
            <h2 class="section-title">EXAMPLE SECTION</h2>
            <div class="button-grid">
                <button class="service-button" onclick="alert('Button clicked!')">
                    Example Button 1
                </button>
                <button class="service-button" onclick="alert('Button clicked!')">
                    Example Button 2
                </button>
                <button class="service-button" onclick="alert('Button clicked!')">
                    Example Button 3
                </button>
            </div>
        </div>"""

    # Generate the page
    html_page = generate_complete_page(
        page_title="Example Page - Metro TV & Appliances",
        header_title="METRO TV & APPLIANCES",
        header_subtitle="Example Page",
        content=content,
        version="1.2"
    )

    # Write to file
    with open("example_page.html", "w", encoding="utf-8") as f:
        f.write(html_page)

    print("✓ Generated example_page.html")
    print("\nUsage Examples:")
    print("-" * 60)
    print("1. Import and use functions:")
    print("   from generate_headers import generate_complete_page")
    print()
    print("2. Generate a custom page:")
    print("   html = generate_complete_page(")
    print("       page_title='My Page',")
    print("       header_title='METRO TV & APPLIANCES',")
    print("       header_subtitle='My Custom Page',")
    print("       content='<div>Your content here</div>'")
    print("   )")
    print()
    print("3. Save to file:")
    print("   with open('my_page.html', 'w') as f:")
    print("       f.write(html)")
    print("-" * 60)


if __name__ == "__main__":
    main()
