import requests
from bs4 import BeautifulSoup


print('Search Type')
print('1. in Lyrics')
print('2. in Artists')
#print('3. in Albums\n')

song_inp = input("Enter Type:")
if song_inp == '1':
    song_type = input("Enter the name of any song: ")
    page = requests.get('https://www.lyrics.com/lyrics/' + song_type + '&qtype=1')
    soup = BeautifulSoup(page.content, 'html.parser')
    scrapme = soup.find_all(class_='lyric-meta')
   
    
    try:
        print("1)")
        print("Song Title:",scrapme[0].find(class_="lyric-meta-title").get_text())
        print("Song Artist:",scrapme[0].find(class_="lyric-meta-album-artist").get_text())
        print("Song Album:",scrapme[0].find(class_="lyric-meta-album").get_text())
        print("Song Year:",scrapme[0].find(class_="lyric-meta-album-year").get_text())
        print('----------------------------------------------------------')

        print("2)")
        print("Song Title:",scrapme[1].find(class_="lyric-meta-title").get_text())
        print("Song Artist:",scrapme[1].find(class_="lyric-meta-album-artist").get_text())
        print("Song Album:",scrapme[1].find(class_="lyric-meta-album").get_text())    
        print("Song Year:",scrapme[1].find(class_="lyric-meta-album-year").get_text())
        print('----------------------------------------------------------')

        print("3)")
        print("Song Title:",scrapme[2].find(class_="lyric-meta-title").get_text())
        print("Song Artist:",scrapme[2].find(class_="lyric-meta-album-artist").get_text())
        print("Song Album:",scrapme[2].find(class_="lyric-meta-album").get_text())
        print('----------------------------------------------------------')

        print("4)")
        print("Song Title:",scrapme[3].find(class_="lyric-meta-title").get_text())
        print("Song Artist:",scrapme[3].find(class_="lyric-meta-album-artist").get_text())
        print("Song Album:",scrapme[3].find(class_="lyric-meta-album").get_text())
        print('----------------------------------------------------------')

        print("5)")
        print("Song Title:",scrapme[4].find(class_="lyric-meta-title").get_text())
        print("Song Artist:",scrapme[4].find(class_="lyric-meta-album-artist").get_text())
        print("Song Album:",scrapme[4].find(class_="lyric-meta-album").get_text())
        print('----------------------------------------------------------')

        print("6)")
        print("Song Title:",scrapme[5].find(class_="lyric-meta-title").get_text())
        print("Song Artist:",scrapme[5].find(class_="lyric-meta-album-artist").get_text())
        print("Song Album:",scrapme[5].find(class_="lyric-meta-album").get_text())
        print('----------------------------------------------------------')

        print("7)")
        print("Song Title:",scrapme[6].find(class_="lyric-meta-title").get_text())
        print("Song Artist:",scrapme[6].find(class_="lyric-meta-album-artist").get_text())
        print("Song Album:",scrapme[6].find(class_="lyric-meta-album").get_text())
        print('----------------------------------------------------------')

        print("8)")
        print("Song Title:",scrapme[7].find(class_="lyric-meta-title").get_text())
        print("Song Artist:",scrapme[7].find(class_="lyric-meta-album-artist").get_text())
        print("Song Album:",scrapme[7].find(class_="lyric-meta-album").get_text())
        print('----------------------------------------------------------')

        print("9)")
        print("Song Title:",scrapme[8].find(class_="lyric-meta-title").get_text())
        print("Song Artist:",scrapme[8].find(class_="lyric-meta-album-artist").get_text())
        print("Song Album:",scrapme[8].find(class_="lyric-meta-album").get_text())
        print('----------------------------------------------------------')

        print("10)")
        print("Song Title:",scrapme[9].find(class_="lyric-meta-title").get_text())
        print("Song Artist:",scrapme[9].find(class_="lyric-meta-album-artist").get_text())
        print("Song Album:",scrapme[9].find(class_="lyric-meta-album").get_text())
        print('----------------------------------------------------------')
    except:
        pass

    choose = input("Choose any of the match one: ")
    if choose == '1':
        b_one = scrapme[0].find("a").get('href')
        #print(b)
        new_val_1 = "https://www.lyrics.com"+b_one
        #print(new_val)
        first_req = requests.get(new_val)
        soup_1 = BeautifulSoup(first_req.content, 'html.parser')
        find_1 = soup_1.find(id="lyric-body-text")
        print(find_1.text)
        
    elif choose == '2':
        b_two = scrapme[1].find("a").get('href')
        new_val_2 = "https://www.lyrics.com"+b_two
        second_req = requests.get(new_val_2)
        soup_2 = BeautifulSoup(second_req.content, 'html.parser')
        find_2 = soup_2.find(id="lyric-body-text")
        print(find_2.text)
        
    elif choose == '3':
        b_three = scrapme[2].find("a").get('href')
        new_val_3 = "https://www.lyrics.com"+b_three
        third_req = requests.get(new_val_3)
        soup_3 = BeautifulSoup(third_req.content, 'html.parser')
        find_3 = soup_3.find(id="lyric-body-text")
        print(find_3.text)
        
    elif choose == '4':
        b_four = scrapme[3].find("a").get('href')
        new_val_4 = "https://www.lyrics.com"+b_four
        four_req = requests.get(new_val_4)
        soup_4 = BeautifulSoup(four_req.content, 'html.parser')
        find_4 = soup_4.find(id="lyric-body-text")
        print(find_4.text)
    elif choose == '5':
        b_five = scrapme[4].find("a").get('href')
        new_val_5 = "https://www.lyrics.com"+b_five
        five_req = requests.get(new_val_5)
        soup_5 = BeautifulSoup(five_req.content, 'html.parser')
        find_5 = soup_5.find(id="lyric-body-text")
        print(find_5.text)
    elif choose == '6':
        b_six = scrapme[5].find("a").get('href')
        new_val_6 = "https://www.lyrics.com"+b_six
        six_req = requests.get(new_val_6)
        soup_6 = BeautifulSoup(six_req.content, 'html.parser')
        find_6 = soup_6.find(id="lyric-body-text")
        print(find_6.text)
    elif choose == '7':
        b_seven = scrapme[6].find("a").get('href')
        new_val_7 = "https://www.lyrics.com"+b_seven
        seven_req = requests.get(new_val_7)
        soup_7 = BeautifulSoup(seven_req.content, 'html.parser')
        find_7 = soup_7.find(id="lyric-body-text")
        print(find_7.text)
    elif choose == '8':
        b_eight = scrapme[7].find("a").get('href')
        new_val_8 = "https://www.lyrics.com"+b_eight
        eight_req = requests.get(new_val_8)
        soup_8 = BeautifulSoup(eight_req.content, 'html.parser')
        find_8 = soup_8.find(id="lyric-body-text")
        print(find_6.text)
    elif choose == '9':
        b_nine = scrapme[8].find("a").get('href')
        new_val_9 = "https://www.lyrics.com"+b_nine
        nine_req = requests.get(new_val_9)
        soup_9 = BeautifulSoup(nine_req.content, 'html.parser')
        find_9 = soup_9.find(id="lyric-body-text")
        print(find_9.text)
    elif choose == '10':
        b_ten = scrapme[9].find("a").get('href')
        new_val_10 = "https://www.lyrics.com"+b_ten
        ten_req = requests.get(new_val_10)
        soup_10 = BeautifulSoup(ten_req.content, 'html.parser')
        find_10 = soup_10.find(id="lyric-body-text")
        print(find_10.text)
        

elif song_inp == '2':
    song_artist = input("Enter the name of any artist: ")
    page1 = requests.get('https://www.lyrics.com/serp.php?st=' + song_artist + '&qtype=2')
    soup2 = BeautifulSoup(page1.content, 'html.parser')
    scrapme1 = soup2.find_all(class_='tal')
    try:
        print("Search results for "+song_artist+" in artists")
        print('----------------------------------------------------------')
        print("Artist 1:",scrapme1[0].find(class_="name").get_text())
        print("Artist 2:",scrapme1[1].find(class_="name").get_text())
        print("Artist 3:",scrapme1[2].find(class_="name").get_text())
        print("Artist 4:",scrapme1[3].find(class_="name").get_text())
        print("Artist 5:",scrapme1[4].find(class_="name").get_text())
        
    except:
        pass
    choose1 = input("Choose any artist: ")
    if choose1 == '1':
        b1 = scrapme1[0].find("a").get('href')
        
        new_val1 = "https://www.lyrics.com/"+b1
        #print(new_val1)
        first_req1 = requests.get(new_val1)
        soup3 = BeautifulSoup(first_req1.content,'html.parser')
        
        letsgo0 = soup3.find(class_="tdata-ext")
        letsgo1 = letsgo0.find_all(class_="clearfix")

        try:
            print("Album:",letsgo1[0].find(class_="artist-album-label").get_text())
            print("Album:",letsgo1[1].find(class_="artist-album-label").get_text())
            print("Album:",letsgo1[2].find(class_="artist-album-label").get_text())
            print("Album:",letsgo1[3].find(class_="artist-album-label").get_text())
            print("Album:",letsgo1[4].find(class_="artist-album-label").get_text())
            print("Album:",letsgo1[5].find(class_="artist-album-label").get_text())
            print("Album:",letsgo1[6].find(class_="artist-album-label").get_text())
            print("Album:",letsgo1[7].find(class_="artist-album-label").get_text())
        except:
            pass
    elif choose1 == '2':
        b1_2 = scrapme1[1].find("a").get('href')
        
        new_val2 = "https://www.lyrics.com/"+b1_2
        #print(new_val1)
        first_req2 = requests.get(new_val2)
        soup_two = BeautifulSoup(first_req2.content,'html.parser')
        
        letsgo_2 = soup_two.find(class_="tdata-ext")
        letsgo2 = letsgo_2.find_all(class_="clearfix")

        try:
            print("Album:",letsgo2[0].find(class_="artist-album-label").get_text())
            print("Album:",letsgo2[1].find(class_="artist-album-label").get_text())
            print("Album:",letsgo2[2].find(class_="artist-album-label").get_text())
            print("Album:",letsgo2[3].find(class_="artist-album-label").get_text())
            print("Album:",letsgo2[4].find(class_="artist-album-label").get_text())
            print("Album:",letsgo2[5].find(class_="artist-album-label").get_text())
            print("Album:",letsgo2[6].find(class_="artist-album-label").get_text())
            print("Album:",letsgo2[7].find(class_="artist-album-label").get_text())
        except:
            pass

    elif choose1 == '3':
        b1_3 = scrapme1[2].find("a").get('href')
        
        new_val3 = "https://www.lyrics.com/"+b1_3
        #print(new_val1)
        first_req3 = requests.get(new_val3)
        soup_three = BeautifulSoup(first_req3.content,'html.parser')
        
        letsgo_3 = soup_three.find(class_="tdata-ext")
        letsgo3 = letsgo_3.find_all(class_="clearfix")

        try:
            print("Album:",letsgo3[0].find(class_="artist-album-label").get_text())
            print("Album:",letsgo3[1].find(class_="artist-album-label").get_text())
            print("Album:",letsgo3[2].find(class_="artist-album-label").get_text())
            print("Album:",letsgo3[3].find(class_="artist-album-label").get_text())
            print("Album:",letsgo3[4].find(class_="artist-album-label").get_text())
            print("Album:",letsgo3[5].find(class_="artist-album-label").get_text())
            print("Album:",letsgo3[6].find(class_="artist-album-label").get_text())
            print("Album:",letsgo3[7].find(class_="artist-album-label").get_text())
        except:
            pass
    elif choose1 == '4':
        b1_4 = scrapme1[3].find("a").get('href')
        
        new_val4 = "https://www.lyrics.com/"+b1_4
        #print(new_val1)
        first_req4 = requests.get(new_val4)
        soup_four = BeautifulSoup(first_req4.content,'html.parser')
        
        letsgo_4 = soup_four.find(class_="tdata-ext")
        letsgo4 = letsgo_4.find_all(class_="clearfix")

        try:
            print("Album:",letsgo4[0].find(class_="artist-album-label").get_text())
            print("Album:",letsgo4[1].find(class_="artist-album-label").get_text())
            print("Album:",letsgo4[2].find(class_="artist-album-label").get_text())
            print("Album:",letsgo4[3].find(class_="artist-album-label").get_text())
            print("Album:",letsgo4[4].find(class_="artist-album-label").get_text())
            print("Album:",letsgo4[5].find(class_="artist-album-label").get_text())
            print("Album:",letsgo4[6].find(class_="artist-album-label").get_text())
            print("Album:",letsgo4[7].find(class_="artist-album-label").get_text())
        except:
            pass
    elif choose1 == '5':
        b1_5 = scrapme1[4].find("a").get('href')
        
        new_val5 = "https://www.lyrics.com/"+b1_5
        #print(new_val1)
        first_req5 = requests.get(new_val5)
        soup_five = BeautifulSoup(first_req5.content,'html.parser')
        
        letsgo_5 = soup_five.find(class_="tdata-ext")
        letsgo5 = letsgo_5.find_all(class_="clearfix")

        try:
            print("Album:",letsgo5[0].find(class_="artist-album-label").get_text())
            print("Album:",letsgo5[1].find(class_="artist-album-label").get_text())
            print("Album:",letsgo5[2].find(class_="artist-album-label").get_text())
            print("Album:",letsgo5[3].find(class_="artist-album-label").get_text())
            print("Album:",letsgo5[4].find(class_="artist-album-label").get_text())
            print("Album:",letsgo5[5].find(class_="artist-album-label").get_text())
            print("Album:",letsgo5[6].find(class_="artist-album-label").get_text())
            print("Album:",letsgo5[7].find(class_="artist-album-label").get_text())
        except:
            pass
    
