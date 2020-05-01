# Get-Pipelines
This python script allows [CircleCI](https://circleci.com( users to fetch all of their pipeline projects that are included within a script. Modify the script's output to best fit your needs!

# Get your CircleCI Token
You will need a CircleCI API token to run this script. Create one [here](https://app.circleci.com/settings/user/tokens)!

# Requirements
[grequests](https://github.com/spyoungtech/grequests)

# Running

Store your projects within a text file, with each project name separated by a new line. 

`python3 pipelines.py projects.txt organization-name ?vcs`

The vcs parameter will default to 'gh'. Provide 'bb' for Bitbucket projects
