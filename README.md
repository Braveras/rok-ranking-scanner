# ROK Ranking Scanner
Little tool to generate an excel (.csv) from top300 players in Rise of Kingdoms. (Home kingdom)

Tested with MEmu and Bluestacks 5.9.0 (Remember to enable ADB)

> Tablet mode

> Tested with 1920 x 1080 resolution (360 DPI)

It will auto-skip players with a not accessible profile (users that migrated or banned accounts)
  (It will now skip 2 consecutive inaccessible profiles if found)

It will take:

[ID, Name, Alliance, Power, Total Killpts, T1 Killpts, T2 Killpts, T3 Killpts, T4 Killpts, T5 Killpts, Highest Power, Victory, Defeat, Dead, Scout Times, Gathered rss, Sent rss, Help times]

It is recommended that the scanning account is allianceless to avoid rally notifications from covering the ID.

It is also recommended to turn off the title notifications under game settings.

While this tool runs through ADB and allows you to use the PC while scanning, you must keep in mind that the clipboard is being used to copy every players name.

Average time per profile is 6-8 seconds, which results in an total average scanning time of 30-40 minutes for top300.

# How to use
Open the player ranking menu, and start the tool `py main.py`

# Example

![74eefc37b35f888deb8cf8dc173033ea (1)](https://user-images.githubusercontent.com/36737950/204095306-be7e079f-2415-48fe-90f6-9c2c2ba6df53.gif)


![Excel_example](https://i.gyazo.com/47cf014201bb6a20b0a86c3841189a29.png)
