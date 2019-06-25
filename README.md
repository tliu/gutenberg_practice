Spin up a REST API located at localhost:12345

| endpoint    | expected return |
| ----------- | --------------- |
| /book/\<id\>  | full text of book with id: \<id\> |
| /book/\<id\>/freq  | word frequency map, sorted alphabetically by word, one line per entry in the form "[word] [count]" |
| /word/\<word\> | occurences of \<word\> in all books |
| /word/\<word\>/best_book | title of book with most occurences of \<word\>, if there is a tie return the book with a longer title |
| /title/autocomplete/\<query\> | return all books that have a title starting with \<query\> (what we would use if we were making a title autocomplete box |
| /lang/\<language\>/books | list of book titles that have the specified language (eg. English), separated by newlines |
| /lang/\<language\>/authors | list of authors that have written at least one book in the specified language |
