def search():                    #creating a function
    a=input("Enter a car company brand: ")
    a=a.lower()
    if a=="audi":
        print('''Audi AG is a German automobile manufacturer that designs, engineers,
        produces, markets and distributes luxury vehicles.
        Audi is a member of the Volkswagen Group 
        and has its roots at Ingolstadt, Bavaria, Germany. Audi
        -branded vehicles are produced in nine production facilities worldwide.''')
    elif a=="bmw":
        print('''Bayerische Motoren Werke AG, commonly referred to as BMW, is a German multinational
        company which produces luxury vehicles and motorcycles
        .The company was founded in 1916 as a manufacturer of aircraft engines, 
        which it produced from 1917 until 1918 and again from 1933 to 1945.''')                                   
    elif a=="bugatti":
        print('''Automobiles Ettore Bugatti was a French car manufacturer of high-performance
        automobiles, founded in 1909 in the then-German city of Molsheim, Alsace by the Italian-born 
        industrial designer Ettore Bugatti.
        The cars were known for their design beauty and for their many race victories.''')
    elif a=="ferrari":
        print('''Ferrari is an Italian luxury sports car manufacturer based in Maranello, Italy
        .Founded by Enzo Ferrari in 1939 out of Alfa Romeo's race division as Auto Avio Costruzioni,
        the company built its first car in 1940.''')
    elif a=="ford":
        print('''Ford Motor Company, commonly known as Ford, is an American multinational automaker 
        that has its main headquarters in Dearborn, 
        Michigan, a suburb of Detroit. It was founded by Henry Ford and incorporated on June 16, 1903. ''')
    elif a=="hyundai":
        print('''The Hyundai Motor Company, commonly known as Hyundai Motors
        ,is a South Korean multinational automotive manufacturer headquartered in Seoul.''')
    elif a=="kia":
        print('''Kia Motors Corporation, commonly known as 
        Kia Motors is a South Korean multinational automotive manufacturer headquartered in Seoul. 
        It is South Korea's second-largest automobile manufacturer following the 
        Hyundai Motor Company, with sales of over 2.8 million vehicles in 2019.''')
    elif a=="jaguar":
        print('''Jaguar is the luxury vehicle brand of Jaguar Land Rover,
        a British multinational car manufacturer with its 
        headquarters in Whitley, Coventry, England.''')
    elif a=="lamborghini":
        print('''Automobili Lamborghini S.p.A. is an Italian brand and manufacturer 
        of luxury sports cars and SUVs based in Sant'Agata Bolognese
        .The company is owned by the Volkswagen Group through its subsidiary Audi.''')
    elif a=="chevrolet":
        print('''Chevrolet, colloquially referred to as Chevy
        and formally the Chevrolet Division of General Motors Company,
        is an American automobile division of the American manufacturer General Motors.''')
    elif a=="fiat":
        print('''Fiat Automobiles S.p.A. is an Italian automobile manufacturer,
        a subsidiary of FCA Italy S.p.A., which is part of Fiat Chrysler Automobiles.''')
    elif a=="land rover":
        print('''Land Rover is a British brand of predominantly four-wheel drive
        ,off-road capable vehicles, that is owned by multinational car manufacturer Jaguar Land Rover,
        since 2008 a subsidiary of India's Tata Motors.JLR currently builds Land Rovers in Brazil,
        China, India, Slovakia, and the United Kingdom.''')
    elif a=="mercedes":
        print('''Mercedes-Benz is both a German automotive marque and, from late 2019 onwards,
        a subsidiary of Daimler AG. Mercedes-Benz is known for producing luxury vehicles and 
        commercial vehicles. The headquarters is in Stuttgart, Baden-Württemberg.
        The name first appeared in 1926 under Daimler-Benz.''') 
    elif a=="nissan":
        print('''The Nissan Motor Company, Ltd. trading as the Nissan Motor Corporation
        and usually shortened to Nissan, is a Japanese multinational automobile 
        manufacturer headquartered in Nishi-ku, Yokohama.''')   
    elif a=="porsche":
        print('''Dr.-Ing. h.c. F. Porsche AG, usually shortened to Porsche AG,
        is a German automobile manufacturer specializing in high-performance sports cars,
        SUVs and sedans.''')
    elif a=="renault":
        print('''Renault S.A.) is a French multinational automobile manufacturer established in 1899
        .The company produces a range of cars and vans, and in the past has manufactured trucks,
        tractors, tanks, buses/coaches, aircraft and aircraft engines, and autorail vehicles.''')
    elif a=="rolls royce":
        print('''Rolls-Royce Motor Cars Limited is a British luxury automobile maker
        .A wholly owned subsidiary of German group BMW, it was established in 1998 after
        BMW was licensed the rights to the Rolls-Royce brand .''')
    elif a=="maruti suzuki":
        print('''Maruti Suzuki India Limited, formerly known as Maruti Udyog Limited,
        is an automobile manufacturer in India. It is a 56.21% owned subsidiary
        of the Japanese automotive manufacturer Suzuki Motor Corporation.''')
    elif a=="tata motors":
        print('''Tata Motors Limited, formerly Tata Engineering and Locomotive Company,
        is an Indian multinational automotive 
        manufacturing company headquartered in Mumbai, Maharashtra, India. ''')
    elif a=="toyota":
        print('''Toyota Motor Corporation is a Japanese multinational automotive
        manufacturer headquartered in Toyota, Aichi, Japan.
        In 2017, Toyota's corporate structure consisted of 364,445 employees worldwide and,
        as of December 2019, was the tenth-largest company in the world by revenue.''')
    elif a=="volkswagen":
        print('''Volkswagen, shortened to VW, is a German automaker founded in 1937 by the German
        Labour Front, known for the iconic Beetle and headquartered in Wolfsburg. It is the flagship
        brand of the Volkswagen Group, the largest automaker by worldwide sales in 2016 and 2017''')
    elif a=="volvo":
        print('''Volvo Cars, stylized as VOLVO, is a Swedish luxury automobile marque.
        It is headquartered in Torslanda in Gothenburg, Sweden.
        The company manufactures and markets sport
        utility vehicles, station wagons, hatchbacks, sedans and compact executive sedans.''')
    elif a=="skoda":
        print('''ŠKODA AUTO, commonly called Škoda, is a Czech automobile manufacturer 
        founded in 1895 as Laurin & Klement and headquartered 
        in Mladá Boleslav, Czech Republic. In 1925 Laurin & Klement was 
        acquired by the industrial conglomerate Škoda Works, which itself became state owned in 1948''')
    else:
        print("found error")
search()   # calling the function
def call():
    n=int(input("type 1 to search again and type 2 to exit: "))
    if n==1:
        search()
    else:
        print("exiting the program in 3")     
        print("2")     
        print("1")     
call()