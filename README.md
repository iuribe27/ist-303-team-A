# IST-303-Team-A-GroupProject
# Team Name:
Post-It Fo' Lyfe Crew
# Team Members:
Adam Trudgeon, Isabela Uribe, Mabel Hanken, Ted Chang
# Application Concept:
A virtual post-it note board that allows users to manage thoughts, notes, lists. Allows you to carry your post-it notes wherever you go!
# Stakeholders:
All users, including us! It's a public app.
# Instructions for Running the Application:
1. Install Virtual Environment by typing into Command Prompt: pip install virtualenv
2. Press Enter
3. Create virtual environment by typing into Command Prompt: virtualenv venv
4. Press Enter
5. Activate virtual environment by typing into Command Prompt: .\venv\Scripts\activate (For MacOS: source venv/bin/activate)
6. Press Enter
7. Clone Application repository by typing into Command Prompt: git clone https://github.com/iuribe27/ist-303-team-A.git
8. Press Enter
9. Change directory to cloned app folder by typing to Command Prompt: cd ist-303-team-A
10. Press Enter
11. Install requirement packages by typing into Command Prompt: pip install -r requirements.txt
12. Press Enter
13. Start a Python interpreter by typing into the Command Prompt: python (or python3 if you multiple versions of python)
14. Press Enter
15. Import the Database Object by typing into the interpreter: from postproject import db
16. Press Enter
17. Initialize the database by typing into the interpreter: db.create_all()
18. Press Enter
19. Exit the Interpreter by typing into the interpreter: exit()
20. Press Enter
21. Start the program by typing into Command Prompt: python run.py (or python3 if you multiple versions of python)
22. Press Enter
23. Copy & Paste local host http://127.0.0.1:5000/ into internet browser
24. That's it, you're running the app :)
## Tests:
In the applications root folder, run pytest
## Test Coverage:
In the applications root folder, run pytest --cov
# User Stories:
## 1. Account Creation & Login - 3 days
As a User, I can create an account and login.
## 2. Add a Profile Picture - 3 days
As a User, I can add a profile picture.
## 3. Create a Post-It - 5 days
As a User, I can create a new post-it.
## 4. Modifying a Post-It - 5 days
As a User, I can modify an existing post-it content and aesthetics.
## 5. Delete a Post-It - 5 days
As a User, I can delete a post-it.
## 6. Re-arranging a Post-It - 10 days
As a User, I can re-arrange post-its in any order
## 7. Creating a Board - 10 days
As a User, I can create a Board to group interests/topics
## 8. Board Collaboration - 14 days
As a User, I can share my board with friends.
# Decomposition of User Stories:
## 1. Account Creation & Login - 3 days
As a User, I can create an account and login.
- Create a 'Create an Account/Sign-Up' screen (Adam)
  - Include storage database for accounts
- Create a 'Login' screen (Adam)
- Create branding/background images (Mabel)
## 2. Add a Profile Picture - 2 days
As a User, I can add a profile picture.
- Create Upload functionality (Isabela)
- Change Picture functionality (Isabela)
- Have stock images for avatars (Isabela)
## 3. Create a Post-It - 4 days
As a User, I can create a new post-it.
- Create New Post-It functionality (Ted)
- Create Post-It Colors selectability (Ted)
- Create Text-Editing abilities / Font-style selections (Ted)
- Create 'Add to Board' button (Ted)
- Create last-modified and created-on timestamps (Ted)
## 4. Modifying a Post-It - 4 days
As a User, I can modify an existing post-it content and aesthetics.
- Create Edit functionality (Adam)
## 5. Delete a Post-It - 3 days
As a User, I can delete a post-it.
- Create delete/Trash can functionality (Mabel)
- Create 'Are you sure?' confirmation pop-up window? (Mabel)
## 6. Re-arranging a Post-It - 6 days
As a User, I can re-arrange post-its in any order
- Create the Select-And-Drag functionality (Isabela)
- Create Change Post-It Colors selectability (Adam)
- Create Change Text-Editing abilities / Font-style selections (Adam)
## 7. Board Collaboration - 4 days
As a User, I can share my board with friends.
- Create Share via Copy Link functionality (Mabel/Ted)

# Backlog for Future App Releases:
## Creating a Board - 6 days
As a User, I can create multiple Boards to group interests/topics
- Create a New Board functionality (Adam)
- Add Post-It Notes to Board functionality (Adam)
- Create Delete/Trash Can board functionality (Isabela)
- Create Board Themes functionality (Isabela)
- Create Search Post-It Note functionality (Adam/Isabela)
- Create Add tags functionality for searchablity (Ted)
- Create Change 'Add to Board' button (Adam)
- Create 'Invite Friends' functionality (Mabel/Ted)

# Milestone 1.0 (2 iterations) - 16 days (40 days at a 0.4 velocity):
## Iteration 1 (20 days)
1. Account Creation & Login
2. Add a Profile Picture
3. Create a Post-It
## Iteration 2 (20 days)
4. Modifying a Post-It
5. Delete a Post-It
# Milestone 2.0 (1 iteration) - 10 days (25 days at a 0.4 velocity):
## Iteration 1 (25 days)
6. Re-arranging a Post-It
7. Board Collaboration

# Burndown Progress Chart
To view click here https://1drv.ms/x/s!BEcHh6Oz5R4dg-Z1qyebkecY3OvNTA?e=uvL1eM
# Three Most Important Things We Learned About Software Development
1. Don't underestimate the complexity behind implementing simple features!
2. Plan, Plan, Plan! Have a project plan in place before writing code.
3. Testing! Always test your code and have someone else review it. 

