# IS-StuRa

IS-StuRa is a inventary database software with webui.

## Features

Add, remove, change, listing, and search of inventary.

## Require

* py27-django18
* sqlite3

# Datenbase Schema

## Inventary Table
* ID        (Primary Key)
* ID_typ    (Foreign Key typ)
* ID_location (Foreign Key location)
* ID_tbr    (Foreign Key time_between_replacement)
* ID_category (Foreign Key category)
* objectname
* vendor_id
* amount
* date_of_purchase
* single (Brutto)
* total (Brutto)
* fair_value (Brutto)

## Location Table
* ID
* location
    * Z 123
    * S 522
    * S 523
    * A 103
    * A 104
    * A 105
    * A 106
    * A 107
    * A 108
    * ...

## Typ Table
* ID
* typ
    * Scanner
    * Tisch
    * Stuhl
    * Switch
    * Server
    * Computer
    * ...

## time_between_replacement Table
* ID
* tbr (in year)
    * 0 (GWG; Kleininventar)
    * 3
    * 5
    * 7
    * 8
    * 10
    * 13
    * 14
    * ...

## Category Table
* ID
* category
    * Kleininventar (< 410 Euro Netto)
    * Buchinventar (> 410 Euro Netto)

# Format
* CSV
* Plain Text
