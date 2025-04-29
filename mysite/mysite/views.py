from django.http import HttpResponse
import json


def read_file():
    with open("students.json", "r") as f:
        data = json.load(f)
    return data


def calculate(data):
    passed = ""
    failed = ""
    for i in data:
        grade = i["grade"]
        if grade >= 10:
            passed += f"""
<tr class="transition transform hover:scale-105 hover:shadow-lg duration-300">
  <td class="px-6 py-3 text-center border-b hover:bg-green-100 hover:text-green-800 transition-colors duration-300">{i['name']}</td>
  <td class="px-6 py-3 text-center border-b hover:bg-green-100 hover:text-green-800 transition-colors duration-300">{i['grade']}</td>
  <td class="px-6 py-3 text-center border-b hover:bg-green-100 hover:text-green-800 transition-colors duration-300">{i['major']}</td>
</tr>
"""
        else:
            failed += f"""
<tr class="transition transform hover:scale-105 hover:shadow-lg duration-300">
  <td class="px-6 py-3 text-center border-b hover:bg-red-100 hover:text-red-800 transition-colors duration-300">{i['name']}</td>
  <td class="px-6 py-3 text-center border-b hover:bg-red-100 hover:text-red-800 transition-colors duration-300">{i['grade']}</td>
  <td class="px-6 py-3 text-center border-b hover:bg-red-100 hover:text-red-800 transition-colors duration-300">{i['major']}</td>
</tr>"""

    return passed, failed


def table():
    data = read_file()
    passed, failed = calculate(data)
    body = """
       <!DOCTYPE html>
       <html lang="en">
       <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>Student Results</title>
         <script src="https://cdn.tailwindcss.com"></script>
       </head>
       <body class="bg-gray-100">
         <div class="container mx-auto p-6">
           <h1 class="text-4xl font-bold text-center mb-10 text-gray-800">Student Results</h1>

           <!-- Search Bar -->
           <div class="flex justify-center mb-6">
             <input type="text" id="search" placeholder="Search by name or major" class="p-2 border border-gray-300 rounded-lg shadow-lg w-1/3" oninput="filterResults()">
           </div>

           <!-- Accepted People Table -->
           <div class="mb-10">
             <h2 class="text-3xl font-semibold text-center text-[#28a745] mb-6">Accepted People</h2>
             <table class="table-auto border-collapse border border-gray-300 w-full bg-white shadow-lg rounded-lg text-center" id="passedTable">
               <thead>
                 <tr class="bg-[#28a745] text-white transition-colors duration-300">
                   <th class="border border-gray-300 px-4 py-2">Name</th>
                   <th class="border border-gray-300 px-4 py-2">Grade</th>
                   <th class="border border-gray-300 px-4 py-2">Major</th>
                 </tr>
               </thead>
               <tbody>
                 """ + passed + """
               </tbody>
             </table>
           </div>

           <!-- Rejected People Table -->
           <div>
             <h2 class="text-3xl font-semibold text-center text-[#dc3545] mb-6">Rejected People</h2>
             <table class="table-auto border-collapse border border-gray-300 w-full bg-white shadow-lg rounded-lg text-center" id="failedTable">
               <thead>
                 <tr class="bg-[#dc3545] text-white transition-colors duration-300">
                   <th class="border border-gray-300 px-4 py-2">Name</th>
                   <th class="border border-gray-300 px-4 py-2">Grade</th>
                   <th class="border border-gray-300 px-4 py-2">Major</th>
                 </tr>
               </thead>
               <tbody>
                 """ + failed + """
               </tbody>
             </table>
           </div>
         </div>

         <script>
           function filterResults() {
             let searchQuery = document.getElementById('search').value.toLowerCase();

             let passedRows = document.querySelectorAll('#passedTable tbody tr');
             passedRows.forEach(row => {
               let name = row.querySelector('td:nth-child(1)').textContent.toLowerCase();
               let major = row.querySelector('td:nth-child(3)').textContent.toLowerCase();
               if (name.includes(searchQuery) || major.includes(searchQuery)) {
                 row.style.display = '';
               } else {
                 row.style.display = 'none';
               }
             });

             let failedRows = document.querySelectorAll('#failedTable tbody tr');
             failedRows.forEach(row => {
               let name = row.querySelector('td:nth-child(1)').textContent.toLowerCase();
               let major = row.querySelector('td:nth-child(3)').textContent.toLowerCase();
               if (name.includes(searchQuery) || major.includes(searchQuery)) {
                 row.style.display = '';
               } else {
                 row.style.display = 'none';
               }
             });
           }
         </script>
       </body>
       </html>
       """

    return body


def resultsView(request):
    return HttpResponse(table())
