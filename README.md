# google_classroom_assignment_list
Hi, this is a simple program written in python to use the google classroom api to list out your assignments. Missing assignments are listed in big, scary red as well as have a prefix of `Late:` so they can be copied and pasted into something from your terminal.

## Instructions:
1. Run `$ git clone https://github.com/greembow/google_classroom_assignment_list`
2. Go to [Google's Cloud Console](https://console.cloud.google.com/home)
   - **NOTE:** You will probably have to create your API credentials with a personal google account, as most school districts block creating API credentials
4. Create a new project
   1. Click the dropdown at the top
   2. Click `New Project`
   3. Set the project name to anything
4. Enable the Google Classroom API
   1. Click the dropdown at the top left
   2. Click `APIs & Services`
   3. Click `Library`
   4. Search for `Classroom`
   5. Click `Google Classroom API`
   6. Click `Enable`
5. Setup a OAuth Screen
   1. Click the dropdown at the top left
   2. Click `APIs & Services`
   3. Click `OAuth consent screen`
   4. Click `External`
   5. Click `Create`
   6. Fill out `App name`, `User support email`, and `Email addresses` (all required fields marked with a red asterisk
   7. Click `Save and Continue`
   8. Click `Save and Continue`
   9. Click `Add Users`
   10. Add your school email, or whatever email Google Classroom data will be retrieved from.
   11. Click `Add`
   12. Click `Save and Continue`
   13. Click `Back to Dashboard`
6. Get `credentials.json`
   1. Click the dropdown at the top left
   2. Click `APIs & Services`
   3. Click `Credentials`
   4. Click `Create Credentials` at the top
   5. Click `OAuth client ID`
   6. Click the `Application type` dropdown
   7. Click `Desktop app`
   8. Click `Create`
   9. Click `Download JSON` :warning: __WARNING:__ Do not share this token with anyone :warning:
7. Setup
   1. Save the `JSON` file to `google_classroom_assignment_list/`
   2. Rename the `JSON` file to `credentials.json`
8. Run the program
   1. Run `$ cd google_classroom_assignment_list/`
   2. Run `$ pip install -r requirements.txt`
   3. Run `$ python src/main.py`
   4. Click the Google account you added as a tester previously
   5. Click `Continue`
   6. Tick both boxes that appear
   7. Click `Continue`
9. A `token.json` file should be created and your assignments will start to slowly list
10. Watch in glory as you see the hundreds of missing assignments you have appear in one terminal window

## Issues:
- Assignments list slowly
- Shoddy code
- Archived classes show up in the list (this is a limitation of the API)

My response: I am a rust developer and made this in a very short period of time. Commits are welcome if you want to add new features/clean up my code!

## Other:
Thanks to [HenriHawk42](https://github.com/HenriHawk42) and [Frigyes06](https://github.com/Frigyes06) for testing this and providing feedback!
