from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
"""
give our repos to staff
"""
import os
from github import (
    Github
)

def main():
    user = os.environ['GITHUB_USER']
    pw = os.environ['GITHUB_PASSWORD']

    github = Github(login_or_token=user, password=pw)
    orga = github.get_organization('makinacorpus')
    teams = orga.get_teams()
    repos = [r for r in orga.get_repos()]
    staff = [team for team in teams if team.name == 'staff'][0]
    already_in_staff = [r.name for r in staff.get_repos()]
    [staff.add_to_repos(r) for r in repos if not r.name in already_in_staff]
    print("done")
