# Overview

This repository contains a script that visually formats simple tables in Asciidoc files into a more readable format.

The script allows you to render tables of the following type:

```adoc
|===
|Header 1        |Header 2        |Header 3

|Column 1, row 1                                                |Column 2, row 1 |Column 3, row 1

|Column 1, row 2|Column 2, row 2 |Column 3, row 2

|Column 1, row 3  |Column 2, row 3 |Column 3, row 3
|===
```

Into a more visualized view:

```adoc
|===
| Header 1        | Header 2        | Header 3       
| Column 1, row 1 | Column 2, row 1 | Column 3, row 1
| Column 1, row 2 | Column 2, row 2 | Column 3, row 2
| Column 1, row 3 | Column 2, row 3 | Column 3, row 3
|===
```

As a result, the script will create a file **output.adoc**, which will be a copy of the selected file, but with formatted tables.

> **Note**
> The contents in the **output.adoc** file are always overwritten after the script is run!

## How to use

Just run the script with the following command:

`python script.py`

At that, the console will display help. Or you can specify as an argument the file in which you want to format the tables:

`python script.py input.adoc`
