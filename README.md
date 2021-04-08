# Breaking Bad Datasets

This repository consists of datasets which contain data from the Breaking Bad Universe (Breaking Bad + Better Call Saul) created by Vince Gilligan. The files have been created using data fetched from the *[Breaking Bad API](https://www.breakingbadapi.com/)* created by [Tim Biles](https://github.com/timbiles/Breaking-Bad--API). I did this activity as part of learning and exploring how APIs work. The script I used for carrying out the process can be found in this repository.

There are 4 datasets:

## 1.**Characters**

| Attribute  | Description                                      |
|------------|--------------------------------------------------|
| `id`         | Unique Id per character                          |
| `name`       | A character's full name                          |
| `birthday`   | A character's birthday                           |
| `occupation` | List of character's known occupation             |
| `img`        | Character's image                                |
| `status`     | Are they alive (or did Heisenberg get to them??) |
| `nickname`   | A known nickname they are referred as            |
| `appearance` | List of seasons that the character appeared in   |
| `portrayed`  | The actor / actress that portrayed the character |
| `category`   | Series that the character is involved with.      |

---

## 2. **Episodes**

| Attribute  | Description                                          |
|------------|------------------------------------------------------|
| `id`         | Unique ID per episode                                |
| `title`      | Title of the episode                                 |
| `season`     | Season that the episode belongs to                   |
| `episode`    | Episode number of it's season                        |
| `air_date`   |  Original air date of the episode                    |
| `characters` | Main characters that are associated with the episode |
| `series`     | Series that the episode belongs to                   |

---

## 3.**Quotes**

| Attribute | Description                      |
|-----------|----------------------------------|
| `id`        | Unique ID per quote              |
| `quote`     | The quote itself                 |
| `author`    | The originator of the quote      |
| `series`    | The series the quote was told in |

---

## 4.**Deaths**

| Attribute        | Description                                            |
|------------------|--------------------------------------------------------|
| `id`               | Unique ID per death                                    |
| `death`            | Name of deceased individual                            |
| `cause`            | How the character met their demise                     |
| `responsible`      | The person(s) responsible or affiliated with the death |
| `last_words`       | The famous last words!                                 |
| `season`           | The season the death occured in                        |
| `episode`          | The episode of the season                              |
| `number_of_deaths` | Number of deaths that occured for this instance        |

---

Feel free to add any missing data, just create an issue or a pull-request either on this repository or  [Tim's](https://github.com/timbiles/Breaking-Bad--API).
