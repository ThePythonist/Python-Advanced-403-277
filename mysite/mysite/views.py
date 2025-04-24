from django.http import HttpResponse


def homeView(request):
    people = [
        {"name": "meysam", "job": "frontend dev", "age": 31},
        {"name": "arian", "job": "backend dev", "age": 24},
        {"name": "kiana", "job": "devops engineer", "age": 23},
    ]

    table = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Tailwind CSS Table</title>
      <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="">

      <div class="container mx-auto p-6">
        <h2 class="text-2xl font-semibold text-center mb-4">People Information Table</h2>
        <table class="table-auto border-collapse border border-gray-300 w-full bg-white shadow-lg rounded-lg text-center">
          <thead>
            <tr class="bg-[#0ac2c5]">
              <th class="border border-gray-300 px-4 py-2 hover:bg-[#009c9f]">Name</th>
              <th class="border border-gray-300 px-4 py-2 hover:bg-[#009c9f]">Job</th>
              <th class="border border-gray-300 px-4 py-2 hover:bg-[#009c9f]">Age</th>
            </tr>
          </thead>
          <tbody>
    """
    for i in people:
        table += f"""
            <tr>
              <td class="border border-gray-300 px-4 py-2">{i['name']}</td>
              <td class="border border-gray-300 px-4 py-2">{i['job']}</td>
              <td class="border border-gray-300 px-4 py-2">{i['age']}</td>
            </tr>
        """

    table += """
          </tbody>
        </table>
      </div>

    </body>
    </html>
    """

    return HttpResponse(table)
