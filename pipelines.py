import os
import sys
import json
import grequests
from datetime import datetime

org = None
vcs = None
token = os.getenv("CIRCLE_TOKEN")
projects = []
url = 'https://circleci.com/api/v2/project/{}/{}/{}/pipeline'

# Parse date format
def parse_time(date):
    return datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')

def get_pipelines(projects):
    global org, vcs, token

    if (org and vcs):
        print('Calling API endpoints:')

        for project in projects:
            print(url.format(vcs, org, project))

        # grouped requests
        rs = (grequests.get(url.format(vcs, org, project.strip()),
                            auth=(token + '', '')) for project in projects)

        # output format
        output = 'Project: {}, Branch: {}, Date: {}, Number: {}, State: {}'

        for response in grequests.map(rs):
            json = response.json()

            for item in json['items']:
                print(output.format(item['project_slug'], item['vcs']['branch'],
                                    parse_time(item['created_at']), item['number'], item['state']))

def main(args):
    global org, vcs

    org = args[2]
    vcs = 'gh' if len(args) <= 3 else args[3]

    with open(args[1]) as f:
        get_pipelines(f.readlines())
        f.close()

if __name__ == "__main__":
    main(sys.argv)
