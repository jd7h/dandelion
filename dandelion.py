import csv
from selenium import webdriver

def load_playlist(filename):
    with open(filename, newline='') as infile:
        csvreader = csv.reader(infile, delimiter=",")
        songs = []
        csvreader.__next__()
        for row in csvreader:
            song = {}
            song['title'] = row[0].strip()
            song['artist'] = row[1].strip()
            song['album'] = row[2].strip()
            song['date_added'] = row[3].strip()
            print(song)
            songs.append(song)
        return songs

def get_driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1024,768)
    return driver

def search_amazon(driver,searchterm,verbose=False):
    if "digital-music" not in driver.current_url and "Digital-Music" not in driver.current_url and "dmusic" not in driver.current_url:
        digitalmusicurl = "https://www.amazon.co.uk/Digital-Music/b/ref=sd_allcat_k_music?ie=UTF8&node=77197031"
        driver.get(digitalmusicurl)
    #search
    searchbox = driver.find_element_by_id("twotabsearchtextbox")
    searchbox.clear()
    searchbox.send_keys(searchterm)
    searchbox.submit()
    #get results
    try:
        tracktable = driver.find_element_by_class_name("s-music-tracks-list-result")
        tracks = tracktable.find_elements_by_tag_name("tr")
        #print(searchterm, "found")
    except Exception as e:
        print(type(e),e)
        print("No results for \"" + searchterm + "\"")
        return []
    if(verbose):
        number_of_songs = len(tracks)
        i = 0
        print(number_of_songs, "search results")
        for track in tracks:
            t = track.text.split("\n")
            print(i, t[0], t[1], "(" + t[2] + ")")
    return tracks

def select_result(driver, tracks, n=0):
    if tracks == [] or n >= len(tracks):
        return
    track = tracks[n]
    try:
        track.find_element_by_class_name("s-music-cart-add-button-container")
        mp3cartbutton = track.find_element_by_class_name("s-music-cart-add-button-container")
        driver.execute_script("return arguments[0].scrollIntoView();", mp3cartbutton)
        mp3cartbutton.click()
    except Exception as e:
        print(type(e),e)
        print("Unable to add \"" + " - ".join(track.text.split("\n")[0:2]) + "\" to cart")
        return

def login(driver,email,password):
    emailbox = driver.find_element_by_id("ap_email")
    emailbox.send_keys(email)
    passwordbox = driver.find_element_by_id("ap_password")
    passwordbox.send_keys(password)
    passwordbox.submit()

def test(driver,songs,n=10):
    if songs == [] or n >= len(songs):
        n = len(songs)
    for song in songs[:n]:
        term = " ".join([song['title'],song['artist'],song['album']])
        tracks = search_amazon(driver, term)
        select_result(driver, tracks, 0)

def __main__(filename):
    pass
    '''
    usage:
    driver = get_driver()
    # log in at amazon website
    songs = load_playlist("sample_playlist_kukeleku.csv")
    test(driver, songs, 10)
    driver.get("https://www.amazon.co.uk/gp/dmusic/purchase/cartReview/")
    '''

    

