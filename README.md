# ROK Ranking Scanner
Little tool to generate an excel `.csv` from top300 players in Rise of Kingdoms. (Home kingdom)

Tested with MEmu and Bluestacks 5.9.0+ (Remember to enable ADB)

> Tablet mode

> Tested with 1920 x 1080 resolution (360 DPI)

It will auto-skip player profiles which are not accessible, as for those who migrated, or banned accounts.

# It will scan

[ID, Name, Alliance, Power, Total Killpts, T1 Killpts, T2 Killpts, T3 Killpts, T4 Killpts, T5 Killpts, Highest Power, Victory, Defeat, Dead, Scout Times, Gathered rss, Sent rss, Help times]

The average scanning time per profile is 6-8 seconds, which results in an total average scanning time of 30-40 minutes for top300.

# Recommendations

- The scanning account should be allianceless to avoid rally notifications from covering the ID.

- Turn off the title notifications under game settings.

- While this tool runs through ADB and allows you to use the PC while scanning, you must keep in mind that the clipboard is being used to copy every players name accurately.

- DO NOT open or modify the excel file while the scan is running

# How it works

Essentially, this tool has 2 parts, one in charge of navigating through the menu while taking screenshots (main.py), and another one in charge of converting the screenshots to `.csv` data (reader.py).

The tool will connect to your android emulator (must have only 1 emulator running). It will navigate through the ranking menu, taking temporal screenshots of the relevant parts of each player profiles (3 pictures per player).

After the screenshots are taken, it will call the subprogram `reader.py` to convert those screenshots into data, to then write it in the spreadsheet file.

This happens once per player, so you should not try to open or modify the `.csv` file that is being generated until the scan finishes.

# How to use

Install [tesseract](https://github.com/UB-Mannheim/tesseract/wiki) and [adb server](https://adbinstaller.com/), and add them to [PATH](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)

Install the script requirements:
```python
pip install -r requirements.txt
```

Open the player ranking menu, and start the tool `py main.py`

Only available for Home Kingdom. You can run it in Lost Kingdom, but it will not take the player ID's correctly.

# Scanning example

![74eefc37b35f888deb8cf8dc173033ea (1)](https://user-images.githubusercontent.com/36737950/204095306-be7e079f-2415-48fe-90f6-9c2c2ba6df53.gif)

# Result example

![Excel_example](https://i.gyazo.com/47cf014201bb6a20b0a86c3841189a29.png)
