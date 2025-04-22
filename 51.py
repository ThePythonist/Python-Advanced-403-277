def generate_html():
    title = input("Enter a title: ")
    h1 = input("Enter a header: ")
    p = input("Enter a paragraph: ")
    li = input("Enter a li: ")
    link = input("Enter a link(example.com): ")
    link_name = input("Enter a link name: ")
    file_name = input("Enter a file name: ")

    html_content = f"""
    <!DOCTYPE html>
    <html >
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
    </head>
    <body>
        <h1>{h1}</h1>
        <p>{p}</p>
        <ul>
            <li>{li}</li>
        </ul>
        <a href="https://www.{link}">{link_name}</a>
    </body>
    </html>
    """

    with open(f"{file_name}.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    print("Done")

generate_html()