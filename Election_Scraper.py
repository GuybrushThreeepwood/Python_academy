#!/usr/bin/env python3
# -*- coding: iso-8859-15 -*-
"""
author: Ekaterina Voropaeva
"""

from bs4 import BeautifulSoup

import requests
import csv
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)


def write_csv(file, data):
    with open(file + ".csv", "w", newline="") as csv_file:

        header = data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=header)

        try:
            writer.writeheader()
            writer.writerows(data)
        except csv.Error as e:
            sys.exit(f"CSV Error: {e}")


def check_arguments(bad_urls, base_url, argv):
    if len(argv) == 3:

        try:
            url = str(argv[1])
            csv_file = str(argv[2])

            if (base_url not in url) or url in bad_urls:
                sys.exit("Not valid URL")
            else:
                return url, csv_file

        except ValueError:
            sys.exit("Incorrect type of arguments")
    else:
        sys.exit("Incorrect number of arguments")


def get_soup(url):
    try:
        page = requests.get(url)
        return BeautifulSoup(page.text, "html.parser")

    except requests.exceptions.ConnectionError as e:
        sys.exit(f"Something went wrong: {e}")


def norm_int(string):
    try:
        return int(string.replace("\xa0", ""))
    except ValueError as e:
        sys.exit(f"Incorrect value provided: {e}")


def get_municipal_info(url, municipal):
    soup = get_soup(url)

    municipal["registered"] = norm_int(soup.find("td", {"headers": "sa2"}).text)
    municipal["envelopes"] = norm_int(soup.find("td", {"headers": "sa3"}).text)
    municipal["valid"] = norm_int(soup.find("td", {"headers": "sa6"}).text)

    tables = soup.find_all("table", {"class": "table"})[1:]

    for table in tables:

        parties = table.find_all("tr")[2:]

        for party in parties:
            party_name = party.td.findNext("td").text

            if party_name == "-":
                continue
            municipal[party_name] = norm_int(party.td.findNext("td").findNext("td").text)


def get_data(url):
    municipal_list = []
    soup = get_soup(url)
    tables = soup.find_all("table", {"class": "table"})

    for table in tables:

        municipal_rows = table.find_all("tr")[2:]

        for row in municipal_rows:

            # skip empty rows
            if row.find("td").text == "-":
                continue

            mun_tmp = {
                "code": "",
                "name": "",
                "registered": 0,
                "envelopes": 0,
                "valid": 0,
            }

            municipal_url = BASE_URL + row.find("a")["href"]

            mun_tmp["code"] = row.find("a").text
            mun_tmp["name"] = row.a.findNext("td").text

            # get municipality info
            get_municipal_info(municipal_url, mun_tmp)

            municipal_list.append(mun_tmp)

    return municipal_list


if __name__ == "__main__":
    INVALID_URLS = [
        "https://volby.cz/pls/ps2017nss/ps36?xjazyk=CZ",
        "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ",
    ]
    BASE_URL = "https://volby.cz/pls/ps2017nss/"
    URL, CSV_FILE = check_arguments(INVALID_URLS, BASE_URL, sys.argv)
    data = get_data(URL)
    write_csv(CSV_FILE, data)
