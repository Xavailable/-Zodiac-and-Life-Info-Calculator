from final_project import horoscope, life, lotto

def test_horoscope():
    assert horoscope("1988-04-28") == "Taurus: April 20 – May 20 Taurus is an earth signand is most often associated with a stubborn nature. Its symbol is the bull and its members are considered to be resolute, and grounded – unafraid to take their time and quite resilient."

def test_life():
    assert life("1988-04-28") == "Your age is 35 years old \nIn Thailand Life expectancy (2020) is 79.27 years old \nso you already used 12,958 days and there are 15,975 days left."

def test_lotto():
    assert lotto("pol") == 72
