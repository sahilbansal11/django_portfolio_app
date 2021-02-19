from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

projects = [
  {
    "id": 1,
    "name": "Balls Screensaver",
    "Languages": ["C++"],
    "Additional Libraries": [],
    "Description": "Displays random balls and terrain in 3D which can collide",
    "url": "https://www.github.com/myusername/project_1",
  },
  {
    "id": 2,
    "name": "AC Circuit Solver",
    "Languages": ["C++"],
    "Additional Libraries": ["Matrix Computation Library", "SVG Rendering"],
    "Description": """Given circuit as a text file input, render it on html page
                      and also show the current and voltage values.
                    """,
    "url": "https://www.github.com/myusername/project_2"
  },
  {
    "id": 3,
    "name": "Pockets Tanks Game",
    "Languages": ["JS"],
    "Additional Libraries": ["Canvas"],
    "Description": """A web based pocket tanks game for 2 users.
                      Shows a random terrain in the start of the game.
                      Has score system, fully working.
                    """,
    "url": "https://www.github.com/myusername/project_2"
  }
]


def index(request):
  return HttpResponse("<h1> Hello World </h1>")

def home(request):
  # render the home.html template for the request with the projects variable
  # context has to be a dictionary storing the variables to be passed to the template
  return render(request, 'my_projects/home.html', context=
                                                    {
                                                     "all_my_projects": projects,
                                                     }
                )

def project(request, id):
  id = int(id)
  # find the project details for this id
  project_details = ''
  name = ''
  for prj in projects:
    if (prj['id'] == id):
      project_details = prj
      name = prj['name']
  return render(request, 'my_projects/project.html', context=
                                                      {
                                                        "project_name": name,
                                                        "project_details": project_details
                                                      }
                )

