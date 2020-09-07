import requests
import json
import msvcrt as m
from os import system


def connectApi():
    url = "https://disease.sh/v2/countries/"
    content = requests.get(url).text
    content = json.loads(content)
    return content


def menu():
    countries = connectApi()
    system("cls")
    while(True):
        print("2020 Yılı Covid-19 Pandemisi Bilgileri".center(50,"*"))
        selection = int(input("1)Ülke Ülke Pandemi Verileri\n2)Top 10 Ülkeler\n3)Çıkış\nSeçiminiz: "))
        if selection == 1:
            pandemicData(countries)
            backtoMenu()
        elif selection == 2:
            top10(countries)
            backtoMenu()
        elif selection == 3:
            exit()
        else:
            print("Lütfen Geçerli Bir Değer Giriniz")

def pandemicData(countries):
    system("cls")
    ulke = input("Detaylarını Öğrenmek İstediğiniz Ülke (Turkey, UK): ")
    for country in countries:
            if ulke == country['country']:
                print(f"Ülke: {country['country']}\nToplam {country['cases']} Vaka,{country['deaths']} Ölüm, {country['recovered']} İyileşen, {country['tests']} Test\nSon 24 Saatte {country['todayCases']} Vaka, {country['todayDeaths']} Ölüm, {country['todayRecovered']} İyileşen")


def backtoMenu():
    print("Ana Menüye Dönmek İçin Herhangi Bir Tuşa Basınız")
    m.getch()
    menu()   

def top10(countries):
    system("cls")
    print("Toplam".center(21, "*"))
    print("1) Vaka Sayısı\n2) Ölüm Sayısı\n3) İyileşen Sayısı\n4) Test Sayısı\n")
    print("Son 24 Saatte".center(21, "*"))
    print("5) Vaka Sayısı\n6) Ölüm Sayısı\n7) İyileşen Sayısı")
    selection = int(input("Seçiminiz:"))
    if selection == 1:
        print(top10cases(countries))


def top10cases(countries):
    cases = []
    for case in countries:
        cases.append(case['cases'])
    cases.sort()
    cases.reverse()
    return cases
    


menu()