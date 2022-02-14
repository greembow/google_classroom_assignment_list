from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from colorama import Fore, Style

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly', 'https://www.googleapis.com/auth/classroom.coursework.me']


def main():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('./token.json'):
        try:
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        except ValueError:
            print('decode error!!!')
            quit()
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            try:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            except ValueError as e:
                print('Your credentials.json is missing or broken!')
                quit()
            except FileNotFoundError as e:
                print('File not found!')
                quit()
        # Save the credentials for the next run
        try:
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        except FileNotFoundError as e:
            print('File not found!')
            quit()
        except AttributeError as e:
            print('Attribute error!')
            quit()

    try:
        service = build('classroom', 'v1', credentials=creds)

        # Call the Classroom API
        results = service.courses().list().execute()
        courses = results.get('courses', [])

        if not courses: # if no courses are found
            print(Fore.RED+'No courses found')
            return # exit
        for course in courses: # for each course in the list
            print(course.get('name') + ':') # print the name of the course with a semicolon
            course_work_results=service.courses().courseWork().list(courseId=course.get('id')).execute() # get a list of the assignments
            for assignment in course_work_results['courseWork']: # for each assignment
                student_submissions = service.courses().courseWork().studentSubmissions().list(courseId=course.get('id'), courseWorkId=assignment['id']).execute() # get a list of student submissions, so we can check for if it is late/turned in
                for submission in student_submissions['studentSubmissions']: # for each submission (should only be one but this safeguards it)
                    if submission['state'] == 'CREATED': # if the state is CREATED it means not turned in
                        try: # classroom's api does not include the late parameter unless it is true, so abuse a try statement here
                            if submission['late']: # if the assignment is late
                                print(Fore.RED+'    Late: '+assignment['title']+Style.RESET_ALL) # print the assignment title in a scary colour
                        except: # when it fails because the assignment is not late
                            print('    '+assignment['title']) # print assignment name
            
    except HttpError as error: # oops
        print('An error occurred: %s' % error)

if __name__ == '__main__':
    main()
