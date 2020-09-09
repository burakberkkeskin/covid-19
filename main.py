import requests
import json
from os import system


def connectApi():
    url1 = "https://disease.sh/v2/countries/"
    url2 = "https://google.com"
    timeout = 5
    try:
	    request = requests.get(url2, timeout=timeout)
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("İnternet Bağlantınızı Kontrol Edip Tekrar Deneyiniz")
        exit()

    try:
	    request = requests.get(url1, timeout=timeout)
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("Api ile Bağlantıda Bir Sorun Oluştu. Lütfen Tekrar Deneyiniz.")
        exit()

    content = requests.get(url1).text
    content = json.loads(content)
    return content


def menu(countries):
    system("cls")
    while(True):
        print("2020 Yılı Covid-19 Pandemisi Bilgileri".center(50,"*"))
        selection = int(input("1)Ülke Ülke Pandemi Verileri\n2)Top 10 Ülkeler\n3)Çıkış\nSeçiminiz: "))
        if selection == 1:
            pandemicData(countries)
            backtoMenu(countries)
        elif selection == 2:
            top10(countries)
            backtoMenu(countries)
        elif selection == 3:
            exit()
        else:
            print("Lütfen Geçerli Bir Değer Giriniz")

def pandemicData(countries):
    system("cls")
    ulke = input("Detaylarını Öğrenmek İstediğiniz Ülke (Turkey, UK): ")
    ulke = ulke.capitalize()
    for country in countries:
            if ulke == country['country']:
                print(f"Ülke: {country['country']}\nToplam {country['cases']} Vaka,{country['deaths']} Ölüm, {country['recovered']} İyileşen, {country['tests']} Test\nBugün Gerçekleşen {country['todayCases']} Vaka, {country['todayDeaths']} Ölüm, {country['todayRecovered']} İyileşen")


def backtoMenu(countries):
    while(True):
        selection = input("Ana Menüye Dönmek İçin 'M' Tuşuna Basınız: ")
        selection = selection.upper()
        if  selection == 'M':
            menu(countries)

def top10(countries):
    system("cls")
    while(True):
        print("Toplam".center(21, "*"))
        print("1) Vaka Sayısı\n2) Ölüm Sayısı\n3) İyileşen Sayısı\n4) Test Sayısı\n")
        print("Son 24 Saatte".center(21, "*"))
        print("5) Vaka Sayısı\n6) Ölüm Sayısı\n7) İyileşen Sayısı\n\n8)Çıkış")
        selection = int(input("Seçiminiz:"))
        if selection == 1:
            top10Cases(countries)
            break
        elif selection == 2:
            top10Deaths(countries)
            break
        elif selection == 3:
            top10Recovered(countries)
            break
        elif selection == 4:
            top10Tests(countries)
            break
        elif selection == 5:
            top10TodayCases(countries)
            break
        elif selection == 6:
            top10TodayDeaths(countries)
            break
        elif selection == 7:
            top10TodayRecovered(countries)
            break
        elif selection == 8:
            backtoMenu(countries)
        else:
            print("Yanlış Seçim Yaptınız")


def top10func(countries, subject):
    system("cls")
    cases = []
    for country in countries:
        cases.append([country[subject], country['country']])
        cases.sort()
        cases.reverse()
    return cases


def top10Cases(countries):
    cases = top10func(countries, 'cases')
    for i in range(10):
        print(f"Top {i+1} Ülke: {cases[i][1]}, Vaka Sayısı: {cases[i][0]}\n")


def top10Deaths(countries):
    cases = top10func(countries, 'deaths')
    for i in range(10):
        print(f"Top {i+1} Ülke: {cases[i][1]}, Ölüm Sayısı: {cases[i][0]}\n")


def top10Recovered(countries):
    cases = top10func(countries, 'recovered')
    for i in range(10):
        print(f"Top {i+1} Ülke: {cases[i][1]}, İyileşen Sayısı: {cases[i][0]}\n")


def top10Tests(countries):
    cases = top10func(countries, 'tests')
    for i in range(10):
        print(f"Top {i+1} Ülke: {cases[i][1]}, Test Sayısı: {cases[i][0]}\n")


def top10TodayCases(countries):
    cases = top10func(countries, 'todayCases')
    for i in range(10):
        print(f"Top {i+1} Ülke: {cases[i][1]}, Vaka Sayısı: {cases[i][0]}\n")


def top10TodayDeaths(countries):
    cases = top10func(countries, 'todayDeaths')
    for i in range(10):
        print(f"Top {i+1} Ülke: {cases[i][1]}, Ölüm Sayısı: {cases[i][0]}\n")


def top10TodayRecovered(countries):
    cases = top10func(countries, 'todayRecovered')
    for i in range(10):
        print(f"Top {i+1} Ülke: {cases[i][1]}, Ölüm Sayısı: {cases[i][0]}\n")

countries = connectApi()
menu(countries)
