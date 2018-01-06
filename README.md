# dandelion
Automatically search and collect all songs from a playlist on Amazon digital music.

## Etymology
Named after [Dandelion](http://witcher.wikia.com/wiki/Dandelion), the minstrel from the The Witcher novels. 

> Dandelion is constantly short on money, often even owing to his friend Geralt, and keeps complaining that an artist's work should be better paid.

## Goal
This small Python program was written to "export" my Spotify playlists to DRM-free music, without having to manually search for each song seperately.

## Prerequisites

- python3
- selenium

## Usage and output
I have provided a sample csv that you can use to test the program. The CSV contains the title, artist and album name of all songs from my playlist "Kukeleku".

```
$ python
>>> import dandelion
>>> driver = dandelion.get_driver()
```
Selenium will start a (non-headless) instance of Chrome.
Go to amazon.co.uk and log in.
Note that if you want to use .de or .com, you'll have to change the URLs in the code by hand.
```
>>> songs = dandelion.load_playlist("sample_playlist_kukeleku.csv")
>>> dandelion.test(driver, songs, 10)
Unable to add "Jewel - Bombay Bicycle Club" to cart
No results for "For What It's Worth (India Dub) DJ Drez, Joey Lugassy Jahta Beat: The Lotus Memoirs"
```
The `test` function will try to add the first 10 songs of the playlist to your Amazon MP3 cart. The program wil display an error message if a song can't be found or added to your cart. 

