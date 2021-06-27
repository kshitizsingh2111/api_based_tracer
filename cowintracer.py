import tkinter as tk
import requests


def getCovidData():
    api = "https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true"
    json_data = requests.get(api).json()
    active_cases = str(json_data['activeCases'])
    deaths = str(json_data['deaths'])
    new_cases = str(json_data['activeCasesNew'])
    previous_tests = str(json_data['previousDayTests'])
    recovered = str(json_data['recovered'])
    total_count = str(json_data['totalCases'])
    source = str(json_data['sourceUrl'])
    label.config(text = "Active Cases Count:- " + active_cases +
                      "\n" + "Death Count:- " + deaths +
                      "\n" + "New Cases:- " + new_cases +
                      "\n" + "Tests Count:- " + previous_tests +
                      "\n" + "Recovered:- " + recovered +
                      "\n" + "Total Patients :- " + total_count )


canvas = tk.Tk()
canvas.geometry("1000x500")
canvas.title("Indian Covid Tracer")

fo = ("Times", 25, "bold italic")

button = tk.Button(canvas, font = fo, text = "Get Report", command = getCovidData)
button.pack(pady = 30)
label = tk.Label(canvas, font = fo)
label.pack(pady = 30)
label2 = tk.Label(canvas, font = 10)
label2.pack()
getCovidData()
canvas.mainloop()