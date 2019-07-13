# function to get weather response

def weather_response(location, api):
		import urllib.request
		req=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+location+'&APPID='+api).read().decode("utf-8")  #the content in the website is being returned as string
		return req
#  used for checking
#  print(weather_response("Delhi","2ab136be1543b5789451a5994364c0d3"))
	

# function to check for valid response 
def has_error(location,json):
		indexName = json.find('name')
		indexComma = json.find(',',indexName,)
		nameCity=json[indexName+7:indexComma-1]
		if(nameCity==location):
			return "False"
		else:
			return "True"


def getDate(n):
		import datetime
		dateToday=datetime.date.today()
		dateAhead=datetime.timedelta(days=int(n))
		# it returns the date for which we need to find the forecast
		return  str(dateToday+dateAhead)



# function to get attributes on nth day
def get_temperature (json, n,t):
	# we add the date and the time with a space in between
	indexDateAndTime=json.find(getDate(n) + ' '+t)
	# as starting 400 previous from index of date and time we get our required temp
	indexTemp=json.find('"temp"',indexDateAndTime-400,indexDateAndTime)
	# as after temperature there is always a comma
	indexComma=json.find(',',indexTemp,)
	# we get the temperature of the particular date and time
	return float(json[indexTemp+7:indexComma])
#  used for testing
#  print(get_temperature(weather_response("Delhi","2ab136be1543b5789451a5994364c0d3"),1,'06:00:00'))



def get_humidity(json, n,t):
	indexDateAndTime=json.find(getDate(n) + ' ' + t) 			#same logic as temperature
	indexHumidity=json.find('humidity',indexDateAndTime-300,indexDateAndTime)
	indexComma=json.find(',',indexHumidity,)
	return float(json[indexHumidity+10:indexComma])

def get_pressure(json, n,t):									#same logic as temperature
	indexDateAndTime=json.find(getDate(n) +' ' +t)
	indexPressure =json.find('pressure',indexDateAndTime-350,indexDateAndTime)
	indexComma = json.find(',',indexPressure,)
	return float(json[indexPressure+10:indexComma])

	

def get_wind(json, n,t):                       #same logic as temperature
	indexDateAndTime=json.find(getDate(n) + ' '+t)
	indexWind=json.find('wind',indexDateAndTime-350,indexDateAndTime)
	indexComma=json.find(',',indexWind,)
	return float(json[indexWind+15:indexComma])
	

	
	
def get_sealevel(json, n,t):                   #same logic as temperature
	indexDateAndTime=json.find(getDate(n) +' ' +t)
	indexSea=json.find('sea_level',indexDateAndTime-400,indexDateAndTime)
	indexComma=json.find(',',indexSea,)
	return float(json[indexSea+11:indexComma])
	




