#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Name : whl Package Update Tool(whl packages only)
Author: DarkRix
Version: 3.6_pythonista3
"""

import json, sys, argparse
from io import StringIO as io
from os import chdir as cd, getcwd as pwd
from pip._internal.cli.main import main as pip
from time import sleep, time as ti

currentdir = pwd()
backup_stdout = sys.stdout
backup_stderr = sys.stderr

def pip_json():
	global JSON_pip_Data
	sys.stderr = io()
	with io() as jdata:
		sys.stdout = jdata
		pip(['list', '--outdated', '--format', 'json'])
		JSON_pip_Data = jdata.getvalue()
		sys.stdout = backup_stdout
		sys.stderr = backup_stderr

def List():
	start = ti()
	pip_json()
	Jdata = json.loads(JSON_pip_Data)
	print("\n########## Package List ##########\n")
	for i in range(len(Jdata)):
		Package_Name = Jdata[i]['name']
		File_Type = Jdata[i]['latest_filetype']
		if File_Type == 'wheel':
			print("  ◆ " + Package_Name + ' (Install Type: ' + File_Type + ')')
	print("\n##################################\n")
	elst = ti() - start
	print("\nElapsed Time:{0}".format(round(elst)) + "[sec]")

def Download():
	start = ti()
	pip_json()
	Jdata = json.loads(JSON_pip_Data)
	print("\n########## Package List ##########\n")
	for i in range(len(Jdata)):
		cd(currentdir)
		Package_Name = Jdata[i]['name']
		File_Type = Jdata[i]['latest_filetype']
		if File_Type == 'wheel':
			print("  ◆ " + Package_Name + ' (Install Type: ' + File_Type + ')')
	print("\n##################################\n")

	for i in range(int(len(Jdata))):
		cd(currentdir)
		Package_Name = Jdata[i]['name']
		File_Type = Jdata[i]['latest_filetype']

		if File_Type == 'sdist':
			Package_Name = """"""
		else:
			pass
		if Package_Name == '':
			pass
		else:
			sys.stderr = io()
			pip(['download','--no-deps', '--no-cache-dir', Package_Name])
			sys.stderr = backup_stderr
	elst = ti() - start
	print("\nElapsed Time:{0}".format(round(elst)) + "[sec]")
	print("All Wheel Packages Downloaded.")

def Update():
	start = ti()
	pip_json()
	Jdata = json.loads(JSON_pip_Data)
	print("\n########## Package List ##########\n")
	for i in range(len(Jdata)):
		cd(currentdir)
		Package_Name = Jdata[i]['name']
		File_Type = Jdata[i]['latest_filetype']
		if File_Type == 'wheel':
			print("  ◆ " + Package_Name + ' (Install Type: ' + File_Type + ')')
	print("\n##################################\n")
	for i in range(len(Jdata)):
		cd(currentdir)
		Package_Name = Jdata[i]['name']
		File_Type = Jdata[i]['latest_filetype']

		if File_Type == 'sdist':
			Package_Name = """"""
		else:
			pass
		if Package_Name == '':
			pass
		else:
			sys.stderr = io()
			pip(['install', '--upgrade','--no-deps', '--ignore-installed', Package_Name])
			sys.stderr = backup_stderr
			cd(currentdir)
	elst = ti() - start
	print("\nElapsed Time:{0}".format(round(elst)) + "[sec]")
	print("All Wheel Packages Updated.")

def main(argument):
	Ap = argparse.ArgumentParser()
	
	Ap.add_argument("-l", "--List", action="store_true", help="only listup update lists")
	Ap.add_argument("-d", "--Download", action="store_true", help="only download update packages")
	Ap.add_argument("-u", "--Update", action="store_true", help="only update packages")
	Ap.add_argument("-v", "--version", action="version", version="3.7", help="this script version")
	Ap.add_argument("list", nargs='?', help="only listup update lists")
	Ap.add_argument("download", nargs='?', help="only download update packages")
	Ap.add_argument("update", nargs='?', help="only update packages")
	Arguments = Ap.parse_args()

	if Arguments.List:
		List()
	elif Arguments.Download:
		Download()
	elif Arguments.Update:
		Update()
	elif Arguments.list == 'download' and Arguments.download == None:
		Download()
	elif Arguments.list == 'update' and Arguments.update == None:
		Update()
	elif Arguments.list == 'list':
		List()

if __name__ == '__main__':
	main(sys.argv[1:])