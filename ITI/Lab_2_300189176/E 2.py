tem = input('What is the temperature? ')

if float(tem) >= 80.0:
    activity = 'The recomanded activity is Swimming'
elif 60.0 <= float(tem) <= 80.0:
    activity = 'The recomanded activity is Soccer'
elif 40.0 <= float(tem) <= 60.0:
    activity = 'The recomanded activity is Volleyball'
elif float(tem) < 40.0:
    activity = 'The recomanded activity is Skying'

print(activity)
