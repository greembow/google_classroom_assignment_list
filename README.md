# google_classroom_assignment_list
Hi, this is a simple program written in python to use the google classroom api to list out your assignments. Missing assignments are listed in big, scary red as well as have a prefix of `Late:` so they can be copied and pasted into something from your terminal.

## Installation:
- Clone the repo
- Follow the [Google Classroom API's Quickstart Guide](https://developers.google.com/classroom/quickstart/python#prerequisites) to install the required dependencies and create credentials for the API
- Place your `credentials.json` file in the root directory of the repo
- Run the program and authenticate with Google
- A `token.json` file should be created and your assignments will start to slowly list

## Issues:
- Assignments list slowly
- Shoddy code
- Archived classes show up in the list (this is a limitation of the API)

My response: I am a rust developer and made this in a very short period of time. Commits are welcome if you want to add new features/clean up my code!
