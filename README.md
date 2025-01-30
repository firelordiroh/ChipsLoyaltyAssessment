# Chips Loyalty Backend Technical Assessment
This is a simple backend API for a social media application, built using Django and Django REST Framework. The API allows users to:
- Create a user
- Create a post
- Comment on a post from different users (or your own)

Follow these steps to set up and run the project locally.

Prerequisites
Before getting started, make sure you have the following installed:
- Python 3.8+
- pip (Python's package installer)
- Git (for cloning the repository)

Installation/Usage:
 1. Clone the Repository
 2. Create the virtual environment and activate the virtual environment
 3. Install the neccessary packages
 4. Start the development server (should be http://127.0.0.1:8000/)
 5. Once you've run the development server with the code you can :
    - POST request to (http://127.0.0.1:8000/api/users) to Create your new user(s)
    - POST request to (http://127.0.0.1:8000/api/posts/) to Create your new post(s)
    - POST request to (http://127.0.0.1:8000/api/comments/) to Create your new comment(s)
   
(Note you can visit the link to do it there as well)
Notes:
- Data persistence: The data will be stored in the db.sqlite3 file, and it will persist across server restarts unless the file is deleted
- Future Endeavors: You can modify the data model or views as needed to add additional functionality (maybe add a like button)
