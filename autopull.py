#!/usr/bin/python
import os
import subprocess
def main():
	repos = findRepos()

	for repo in repos:
		consolePull(repo)

def findRepos():
	repos = []

	for root, dir, files in os.walk("/home/centospac/Desktop/"):
		if '.git' in dir:
			#print root
			repos.append(root)

	return repos

def consolePull(path):
	os.system("cd /" + "&& cd " + path + "&& git pull origin master")
	
main()
