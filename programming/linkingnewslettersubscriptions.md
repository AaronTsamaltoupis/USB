table1: contacts

| user_id | first_name | last_name | email                 |
|---------|------------|-----------|-----------------------|
| 1       | John       | Smith     | jsmith@huh.com        |
| 2       | Paul       | McCartney | paul@beatles.com      |
| 3       | Bill       | Murray    | gopher@caddyshack.com |


table2: newsletter
| newsletter_id | name           | desciption          |
|---------------|----------------|---------------------|
| 1             | goodies to go  | html newsletter     |
| 2             | Design goodies | web& graphic design |


relating the two tables:
which user is subscribed to which newsletter?

table3: contact_newsletter_link

| user_id | newsletter_id |
|---------|---------------|
| 1       | 2             |
| 2       | 1             |
| 2       | 2             |
| 3       | 1             |

if one user is subscribed to several newspapers his name has to appear in several rows
