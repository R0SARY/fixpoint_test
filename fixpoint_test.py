import re
import datetime
import glob
import argparse


def analyzeLogs():
	for file_name in glob.glob("var/log/httpd/*"):
		try:
			with open(file_name) as file:
				hostAccess = {}
				logs = []
				try:
					parser = argparse.ArgumentParser()
					parser.add_argument(
						"-t", "--time", help="format = YEAR/MONTH/DAY YAER/MONTH/DAY", action="store_true")
					args = parser.parse_args()
					for log in file.readlines():
						log = log.split()
						hostname = log[0]
						day, month, year, hour, minute, second = re.split("/|:", log[3][1:])
						logs.append([hostname, datetime.datetime(int(year), conversionMonth(month), int(day), int(hour), int(minute), int(second))])
					logs = sorted(logs, key=lambda x:x[1])
					if args.time:
						before_year, before_month, before_day, after_year, after_month, after_day = map(
							int, re.split(" |/", input("YEAR/MONTH/DAY YAER/MONTH/DAY: ")))
						before_date = datetime.datetime(before_year, before_month, before_day)
						after_date = datetime.datetime(after_year, after_month, after_day)
						before_index = 0
						after_index = 0
						for i in range(len(logs)):
							if before_date == 0 and before_date <= logs[i][1]:
								before_index = i
							elif after_date >= logs[i][1]:
								after_index = i
						logs = logs[before_index:after_index+1]
						
					for log in logs:
						if log[0] in hostAccess.keys():
							hostAccess[log[0]] += 1
						else:
							hostAccess[log[0]] = 1
					hostAccessDisplay(
						sorted(hostAccess.items(), key=lambda x: x[1], reverse=True))
					timeAccessDisplay(logs)
				except Exception as e:
					print(e)
		except OSError as e:
			print(e)


def conversionMonth(month):
	if month == "Jan":
		return 1
	if month == "Feb":
		return 2
	if month == "Mar":
		return 3
	if month == "Apr":
		return 4
	if month == "May":
		return 5
	if month == "Jun":
		return 6
	if month == "Jul":
		return 7
	if month == "Aug":
		return 8
	if month == "Sep":
		return 9
	if month == "Oct":
		return 10
	if month == "Nov":
		return 11
	if month == "Dec":
		return 12


def hostAccessDisplay(accesses):
	print()
	print("------ホスト名別のアクセス件数--------")
	for access in accesses:
		access = str(access)[1:-1].split(",")
		print("{}  {}件".format(access[0], access[1]))
	print("--------------------------------------")
	print()


def timeAccessDisplay(logs):
	print("\n--------時間ごとのアクセス数----------")
	count = 1
	for i in range(len(logs)):
		if i == len(logs)-1 or logs[i][1].date() != logs[i+1][1].date() or logs[i][1].hour != logs[i+1][1].hour:
			print("{}:{}  {}件".format(logs[i][1].date(), logs[i][1].hour, count))
			count = 0
		count += 1
	print("--------------------------------------\n")


if __name__ == "__main__":
	analyzeLogs()
