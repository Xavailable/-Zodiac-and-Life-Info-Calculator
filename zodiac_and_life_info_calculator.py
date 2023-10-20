import random
import time
import sys
from datetime import date

def main():
    print("This is a good day")
    time.sleep(1)
    dob = input("Please insert your Date of birth (yyyy-mm-dd): ")
    print(f"Your zodiac is {horoscope(dob)} \n\nAnd {life(dob)} \n\nYour lucky number is {lotto(dob)}")





def horoscope(dob):
    year, month, day = dob.split("-")
    birthdate = date(int(year), int(month), int(day))
    if date(int(year),3,21) < birthdate < date(int(year),4,19):
        return "Aries—March 21-April 19 Aries—March 21-April 19 Independent and strong‒willed, \nyou are a force to be reckoned with! You love nothing more than an exciting new goal to tackle, \nand you do your best work when you’re flying solo. Your passion and energy keep the rest of us on our toes!"
    if date(int(year),4,20) < birthdate < date(int(year),5,20):
        return "Taurus: April 20 – May 20 Taurus is an earth signand is most often associated with a stubborn nature. Its symbol is the bull and its members are considered to be resolute, and grounded – unafraid to take their time and quite resilient."
    if date(int(year),5,21) < birthdate < date(int(year),6,21):
        return "Gemini: May 21- June 21 Gemini is an air sign, with a symbol showing a pair of twins. Bearers of this sign are often curious and witty, as well as communicative and youthful – often filling their plates so busyness abounds."
    if date(int(year),6,22) < birthdate < date(int(year),7,22):
        return "Cancer: June 22- July 22 Cancer rounds out the four elements as a water sign, represented by the crab symbol. Cancers are said to be deeply emotional creatures, with high levels of sentimentality, compassion and loyalty."
    if date(int(year),7,23) < birthdate < date(int(year),8,22):
        return "Leo: July 23 – August 22 Ah, the lion. Another fire sign, represented by a symbol for the king (or queen) of the jungle, Leos are often thought to be dramatic, passionate and charismatic. They are the leaders of the pack, pushing forward with courage. "
    if date(int(year),8,23) < birthdate < date(int(year),9,22):
        return "Virgo: August 23 – September 22 Back in the earth element, Virgo, represented by the virgin or maiden symbol, is a deeply practical sign. Virgos are known to be analytical and detail-focused, which sometimes leads to perfectionism. They love to be of  help and have a fierce inner-critic."
    if date(int(year),9,23) < birthdate < date(int(year),10,23):
        return "Libra: September 23 – October 23 Libra is an air sign, represented by the symbol of the scales (yes, the same ones you see at a courthouse). Libras are known to be lovers – both romantic and artistic, with a propensity for indecision and struggling to commit, likely connected with their desire to maintain harmony and peace."
    if date(int(year),10,24) < birthdate < date(int(year),11,21):
        return "Scorpio: October 24 – November 21 Just like it sounds, the symbol for this water sign is a scorpion. Scorpios are known to be particularly mysterious and intense if not a bit difficult to know. They are deeply passionate and independent."
    if date(int(year),11,22) < birthdate < date(int(year),12,21):
        return "Sagittarius: November 22 – December 21 Sagittarius is a fire sign, and claims the symbol of the archer. They are known to be adventure and travel seekers, ruled by a free spirit and a playfulness. Forever seeking new wisdom, they are quite philosophicalas well."
    if date(int(year),12,22) < birthdate < date(int(year),1,19):
        return "Capricorn: December 22 – January 19 The final earth sign, the Capricorn is represented by the sea-goat. They are believed to be disciplined and dedicated, with ambitious goals and the patience to chip away at them. They’re a good shoulder to lean on, and thelast to leave the office."
    if date(int(year),1,20) < birthdate < date(int(year),2,18):
        return "Aquarius: January 20 – February 18 Despite the linguistic cues, Aquarius is an air and not a water sign. Its symbol, however, is the water bearer. They are forward thinkers, and thought to be incredibly truthful and intelligent -- their creative and intellectual energy unmatched in the Zodiac. "
    if date(int(year),2,19) < birthdate < date(int(year),3,20):
        return "Pisces: February 19 – March 20 The last of the water signs, the Pisces is symbolized by two fish – usually swimming in opposite directions. Pisces are known to be highly empathetic and intuitive, easily reading the emotions of others and very much ruled by their own. They are understanding and romantic and experience the world with a heightened sensitivity.  "

def life(dob):
    year, month, day = dob.split("-")
    birthdate = date(int(year), int(month), int(day))
    age = date.today().year - birthdate.year
    day_use = date.today() - birthdate
    estimate_dayleft = int(79.27*365) - day_use.days
    return (f"Your age is {age} years old \nIn Thailand Life expectancy (2020) is 79.27 years old \nso you already used {day_use.days:,} days and there are {estimate_dayleft:,} days left.")



def lotto(dob):
    random.seed(dob)
    return random.randint(1, 100)


if __name__ == "__main__":
    main()
