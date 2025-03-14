"""
String Assignment. (This can be tricky so feel free to watch solution so we can do it together)
- Ask the user how many days until their birthday
- Using the print()function. Print an approx. number of weeks until their birthday
- 1 week is = to 7 days.
"""

days_before_birthday = input(f"How many days before you birthday?")
weeks_until_birhday = int(days_before_birthday) / 7
print(f"There are {weeks_until_birhday:.0f} weeks until your birthday")