import random

VOOR = [ 'Jayden', 'Sem', 'Luuk', 'Thijs', 'Daan', 'Milan', 'Jesse', 'Lucas', 'Levi', 'Stijn', 'Thomas', 'Lars', 'Tygo', 'Ruben', 'Tim', 'Finn', 'Thijmen', 'Tom', 'Bram', 'Julian', 'Noah', 'Sven', 'Keano', 'Justin', 'Max', 'Nick', 'Dylan', 'Tijn', 'Gijs', 'Damian', 'Mees', 'Niels', 'Ryan', 'Luca', 'Teun', 'Sam', 'Roan', 'Cas', 'Dylano', 'Stan', 'Quinten', 'Daniel', 'Koen', 'Robin', 'Jason', 'Dani', 'Jamie', 'Timo', 'Hugo', 'Jasper', 'Nout', 'Mats', 'Ties', 'Mike', 'Bas', 'Dean', 'Floris', 'Kay', 'Liam', 'Jurre', 'Matthijs', 'Mick', 'Rick', 'David', 'Hidde', 'Kyan', 'Pim', 'Joey', 'Olivier', 'Joep', 'Mika', 'Dion', 'Guus', 'Jelle', 'Joris', 'Joshua', 'Marijn', 'Rens', 'Aaron', 'Pepijn', 'Colin', 'Chris', 'Bryan', 'Willem', 'Jens', 'Job', 'Niek', 'Giovanni', 'Nathan', 'Jordy', 'Tristan', 'Twan', 'Wesley', 'Quinn', 'Aiden', 'Bjorn', 'Sepp', 'Vince', 'Bart', 'Julius', 'Casper', 'Mohamed', 'Samuel', 'Tobias', 'Boaz', 'Pieter', 'Siem', 'Wessel', 'Stef', 'Jesper', 'Sander', 'Simon', 'Youri', 'Alexander', 'Beau', 'Joost', 'Kevin', 'Yannick', 'Benjamin', 'Jan', 'Valentijn', 'Jonathan', 'Mark', 'Jim', 'Jort', 'Maarten', 'Fabian', 'Ian', 'Rafael', 'Diego', 'Leon', 'Mart', 'Michael', 'Rayan', 'Sil', 'Kick', 'Christian', 'Fedde', 'Jelte', 'Kenji', 'Maurits', 'Philip', 'Stefan', 'Abel', 'Morris', 'Senna', 'Brandon', 'Giel', 'Jack', 'Jari', 'Jay', 'Jeremy', 'Mitchel', 'Owen', 'Viggo', 'Jacob', 'Jonas', 'Loek', 'Duncan', 'Jairo', 'Laurens', 'Maxim', 'Oscar', 'Arda', 'Dinand', 'Joel', 'Jorn', 'Lenn', 'Martijn', 'Tije', 'Wouter', 'Xander', 'Berend', 'Dirk', 'Melle', 'Sebastiaan', 'Xavi', 'Dennis', 'Nigel', 'Sami', 'Adam', 'Boris', 'Brent', 'Davey', 'Jarno', 'Storm', 'Anthony', 'Florian', 'Gabriel', 'Lorenzo', 'Milo', 'Raf', 'Seth', 'Sten', 'Ben', 'Danny', 'Jochem', 'Kees', 'Senne', 'Amir', 'Sophie', 'Lotte', 'Emma', 'Julia', 'Sara', 'Lynn', 'Noa', 'Lisa', 'Esmee', 'Lieke', 'Tess', 'Sanne', 'Maud', 'Zoe', 'Naomi', 'Nikki', 'Evi', 'Amy', 'Floor', 'Anouk', 'Eva', 'Myrthe', 'Fleur', 'Jasmijn', 'Isa', 'Amber', 'Britt', 'Femke', 'Anna', 'Isabel', 'Noor', 'Roos', 'Anne', 'Fay', 'Indy', 'Luna', 'Demi', 'Mila', 'Iris', 'Senna', 'Laura', 'Romy', 'Elise', 'Nina', 'Feline', 'Yara', 'Benthe', 'Danique', 'Kayleigh', 'Lois', 'Marit', 'Nora', 'Eline', 'Nienke', 'Rosalie', 'Tessa', 'Hannah', 'Sterre', 'Charlotte', 'Fenna', 'Karlijn', 'Robin', 'Lindsey', 'Elin', 'Liz', 'Jade', 'Bo', 'Caitlin', 'Lara', 'Merel', 'Alicia', 'Liv', 'Meike', 'Fenne', 'Guusje', 'Ilse', 'Isabella', 'Jenna', 'Vera', 'Suze', 'Jill', 'Lisanne', 'Pien', 'Renske', 'Kyara', 'Quinty', 'Emily', 'Aniek', 'Elisa', 'Fiene', 'Frederique', 'Jaylinn', 'Saar', 'Shania', 'Julie', 'Puck', 'Linde', 'Madelief', 'Merle', 'Rosanne', 'Valerie', 'Jente', 'Josephine', 'Milou', 'Sofia', 'Mara', 'Chayenne', 'Dewi', 'Rosa', 'Sienna', 'Tara', 'Kiki', 'Melissa', 'Yfke', 'Juul', 'Megan', 'Olivia', 'Chloe', 'Kyra', 'Lily', 'Alyssa', 'Kim', 'Suus', 'Thirza', 'Yasmine', 'Aimee', 'Daphne', 'Jet', 'Jinte', 'Lola', 'Isis', 'Jesslyn', 'Juliette', 'Maartje', 'Chelsea', 'Imke', 'Jayda', 'Silke', 'Hailey', 'Veerle', 'Destiny', 'Gwen', 'Jennifer', 'Jessie', 'Selina', 'Cato', 'Janne', 'Maaike', 'Nova', 'Amelie', 'Lise', 'Michelle', 'Azra', 'Dana', 'Lenthe', 'Lina', 'Louise', 'Suzanne', 'Annabel', 'Fabienne', 'Fien', 'Florine', 'Kate', 'Kimberly', 'Minke', 'Ninthe', 'Bregje', 'Esther', 'Felicia', 'Joy', 'Mette', 'Willemijn', 'Ashley', 'Dominique', 'Lea', 'Liselotte', 'Livia', 'Noelle', 'Annemijn', 'Emilie', 'Jaydee', 'Joelle', 'Charissa', 'Ella', 'Famke', 'Leila', 'Lieve', 'Mare', 'Angel', 'Diede', 'Elena', 'Lianne', 'Lorena', 'Nena', 'Nika', 'Pleun', 'Rachel', 'Roosmarijn', 'Carmen', 'Evelien' ]
ACHTER = [ 'Aalmoes', 'Aangeenbrug', 'Aanhaanen', 'Aanstoot', 'Den Aantrekker', 'Aapkes', 'Aardappel', 'Aardoom', 'Achtsteribbe', 'Achttienribbe', 'Advocaat', 'Agterberg of Achterberg', 'Van Agteren', 'Al', 'Alderliefste', 'Aldus', 'Alias', 'Almekinders', 'Althanning ook genaamd Oude Hannink', 'Amen', 'Amor', 'Amour', 'Antenne', 'Appelbrij', 'Appeljan', 'Appelmelk', 'Arnold Bik', 'Avondrood', 'Avontuur', 'Ba', 'Baanvinger', 'Baartmans', 'Baartscheer', 'Van Baasbank', 'De Baat', 'Bah', 'Bakvis', 'Balkenende', 'Ballast', 'Van Ballegooijen', 'Ballemaker', 'Balneger', 'Balnikker', 'Bangert', 'Van Bedaf', 'Beentjes', 'Beerepoot', 'Beestheer', 'Beestman', 'Beffers', 'Beffies', 'Behagel', 'Bello', 'Van Beneden', 'Beneken genaamd Kolmer', 'Bengel', 'Van Bergenhenegouwen', 'Bestebreur', 'Bestebreurtje', 'Den Besten', 'Bezuur', 'Bierdrager', 'Bierenbroodspot', 'Bierhaalder', 'Biersteker', 'Bijlebijl', 'Bijnagte', 'Bijtjes', 'Billekens', 'Billen', 'Biltjes', 'Blaam', 'Blauwendraat', 'Blauwijkel', 'Blekxtoon', 'Blij', 'Blijboom', 'Blijleven', 'Bloed', 'Bloedjes', 'Blom', 'Bloot', 'Bloothoofd', 'Blotevogel', 'Bod', 'Boedeltje', 'Boef', 'Boekenoogen', 'Boeljon', 'Boelrijk', 'Boereboom', 'Boerenbeker', 'Boerendans', 'Boerenfijn', 'Boerhoop', 'Boerjan', 'Boerkoel', 'Boerleider', 'Boerlijst', 'Boer Rookhuizen', 'Boerstoel', 'Boertje', 'Boertjes', 'Boetekees', 'Bollemaat', 'Bolwijn', 'Bonkestooter', 'Bontekoe', 'Bonthond', 'Boompaal', 'Boomsluiter', 'Boonemmer', 'Booster', 'Borghuis ook genaamd op de Borg', 'Borsjes', 'Borstlap', 'Bosklopper', 'Boterenbrood', 'Botjes', 'Botschuijver', 'Boven', 'Braadbaart', 'De Braak', 'In de Braak', 'Braakensiek', 'Braakman', 'Brandjes', 'Brandligt', 'Braspenning', 'Bratvogel', 'Bravenboer', 'Breekpot', 'Briefjes', 'Brillemans', 'Broekmaat', 'Broertjes', 'Brommer', 'Brood', 'Broodwinner', 'Brookhuis geboren Scholten', 'Bruinstroop', 'Bruinvis', 'Brummelman', 'Buddenboehmer', 'Bulder', 'Van Bulderen', 'Busemeijer genaamd Lagemann', 'Buskoop', 'Christ', 'Ciggaar', 'De Cocq van Delwijnen', 'Cortlever', 'Cortvriend', 'Crebolder meergenaamd Krijbolder', 'Cretz of Kretz', 'Cupido', 'Van Cutsem', 'Daantje', 'Das', 'Dat', 'Demper', 'Der Weduwen', 'Dertien', 'Dierickx of Diriks', 'Dijkhuijs vroeger Oude Breuijl', 'Dikkeboom', 'Dikken', 'Den Dikkenboer', 'Dingeldein', 'Dingemans', 'Dirkse ook genaamd van den Heuvel', 'Disco', 'Dito', 'Dodenbier', 'Dodenhuis', 'Doetjes', 'Doing', 'Dom', 'Dondergoor', 'Donderwinkel', 'Donkerwolke', 'De Dood', 'Doodkorte', 'Dooijes', 'Doosje', 'Dootjes', 'Draafsel', 'Drektraan', 'Drentje', 'Drijfhout', 'Drillenburg ook genaamd Lelijveld', 'Drinkwater', 'Dronkers', 'Drooglever', 'Drop', 'Druif', 'Drupsteen', 'Duijfjes', 'Duistermaat', 'Duizendkunst', 'Duizendstraal', 'Dunnebier', 'Dunnewind', 'Duurentijdt', 'Duurkoop', 'Duvekot', 'Duyvendak', 'Ebbelinghaus ook wel genaamd Wirxel', 'Edelschaap', 'Eelzak', 'Eendebak', 'Van Eenennaam', 'Efdee', 'Ego', 'Eigenbrood', 'Eigenraam', 'Eijbaard', 'Eijgenrook', 'Eitjes', 'Van Ekeris', 'Ellen bijgenaamd Otten', 'Elsjan of Wipper', 'Emmer', 'Engelaar', 'Engelblik', 'Engelfriet', 'Engeltjes', 'Erwteman', 'Evenblij', 'Evendik', 'Evenwel', 'Feikes zich noemende Feikes de Groot', 'Fiedeldeij', 'Fijnebuik', 'Fijnvandraat', 'Fladderak', 'Flapper', 'Fles', 'Flik', 'Flippo', 'Flissebaalje', 'Franje', 'Froentjes', 'Funke genaamd Kaiser', 'Funke genaamd Kuepper', 'Funnekotter', 'Gaarkeuken', 'Galekop', 'Ganzeboom', 'Ganzeman', 'Ganzevles', 'Gay', 'Geenjaar', 'Geilvoet', 'Geldmaker', 'Geldtelder', 'Gering', 'Gerrits bijgenaamd Pik', 'Geselschap', 'Geugjes', 'Gijselaar', 'Van Ginderen', 'Gips', 'Van Gisteren', 'Gladpootjes', 'Gmelig zich noemende en schrijvende Meijling', 'Godhelp', 'Goedegebuur', 'Goedegebuure', 'Goedewaagen', 'Goedkoop', 'Goeijenbier', 'De Goeje', 'Goetgeluk', 'Goethart', 'Gootjes', 'Gorgel', 'Gortzak', 'Goudeketting', 'Goudmijn', 'Goudschaal', 'Gouwetor', 'Grasmaijer', 'Gresnicht', 'Grijns', 'Van der Grijspaarde', 'Groentjes', 'Grootendorst', 'Groothuesheidkamp', 'Grootjes', 'Grootkop', 'Grote Ganseij', 'Grote Punt', 'Gruwel', 'Haanappel', 'Haanepen', 'Haantjes', 'Haasen', 'Haasjes', 'Hagmolen of ten Have', 'Hakbijl', 'Hakkenhaar', 'Halfhuid', 'Halfmouw', 'Halfwerk', 'Hamerslag', 'Handjes', 'Hangjas', 'Hardendood', 'Hardeveld ook genaamd Kleuver', 'Haring ook genaamd Brugger', 'Harpenslager', 'Hartelust', 'Hartlief', 'Hateboer', 'Haverslag', 'Hawinkels', 'Hazeloop', 'Hazewindus', 'De Heer', 'De Heer Kloots', 'Heertje', 'Heetebrij', 'Hekwolter of Hekhuis', 'Helleganger', 'Hemelrijk', 'Hendriksen of Hendriks', 'Hendriks, ook wel genaamd Modderkolk', 'Hengstmengel', 'Hennevanger', 'Herklots', 'Herman de Groot', 'Hetebrij', 'Heuker of Hoek', 'Hieltjes', 'Hintjes', 'Hobbel', 'Hobbelt', 'Hoeboer', 'Hoedjes', 'Hoefeijzers', 'Hoefnagel', 'Hoenderboom', 'Hoenderdos', 'Hoendervanger', 'Hoentjen', 'Hoepelman', 'Hoette zich noemende en schrijvende Hoette', 'Hoezee', 'Hoezoo', 'Hogervorst', 'Hommel', 'Hommes', 'Honderd', 'Honderdmark', 'Hondtong', 'Hoogerwoord', 'Hooijkaas', 'Hoppezak', 'Hork', 'Houtepen', 'Houvast', 'Huilmand', 'Huisjes', 'Hummel', 'Hup', 'Hupkes', 'Huppelschoten', 'Huppes', 'Hutjes', 'Van Hylckama Vlieg', 'Ie', 'Ietswaard', 'IJanse', 'IJdel', 'Ijdema', 'IJisberg', 'IJkel', 'IJnzonides', 'IJsebaart', 'IJspeerd', 'IJzerdraat', 'Indeweij Gerlings', 'Ineke', 'Jabroer', 'Jacobus (meergenaamd van der Zande)', 'Janclaes', 'Jansen of Lorkeers', 'Jansen ook genaamd Lorkeers', 'Jeuken', 'Jeukendrup', 'Jokker', 'Jongeneel', 'Jongenengel', 'Jongenotter', 'Jordaan', 'Kaasbergen', 'Kaasenbrood', 'Kaashoek', 'Kaasjager', 'Kaaskooper', 'Kaasschieter', 'Kaffka genaamd Dengler', 'Kalfsvel', 'Van de Kandelaar', 'Kanis', 'Kastje', 'De Kater', 'Katje', 'Kattenberg', 'Kattenpoel Oude Heerink', 'Kattenwinkel', 'Kattestaart', 'Kattevilder', 'Keereweer', 'Kelderhans', 'Kersjes', 'Keukenschrijver', 'De Keus', 'Keuterman', 'Keuvelaar', 'Kieken', 'Kijk in de Vegt', 'Der Kinderen', 'Kisjes', 'Kivik of Beernink', 'Klaasboer', 'Kladder', 'Klapmuts', 'Kleerebezem', 'Kleinekorte', 'Kleingeld', 'Kleinleugenmors', 'Kleinpenning', 'Kleintjes', 'Kleuters', 'Klinkhamer', 'Klontje', 'Klooken', 'Kloote', 'Klootwijk', 'Kloters', 'Klots', 'Kluifhoofd', 'Klungel', 'Knevelbaard', 'Knijpinga', 'Knipper', 'Knoflook', 'Knollema', 'Knorren', 'Knorringa', 'Knots', 'Knuf', 'Knuppel', 'De Koe', 'Koedoder', 'Koedood', 'Koekebakker', 'Koekenbier', 'Koekkelkoren', 'Koekoek', 'Koeman', 'Koeslag', 'Koetje', 'Koffijberg', 'Kogeldans', 'Kohlberg ook wel genaamd Meijer', 'Kolder', 'Komduur', 'Komkommer', 'Komtebedde', 'Konijnenbelt', 'Koopziek', 'Kootje', 'Koperdraad', 'Koper ook geschreven Jansen', 'Koppendraaier', 'Koreneef', 'Kornalijnslijper', 'Korrelboom', 'Kortekaas', 'Kortlang', 'Kortleven', 'Kots', 'Kouthoofd', 'Kraaijenvanger', 'Kraak', 'Kracht', 'Kregel', 'Krenten', 'Kreukniet', 'Kroeseklaas', 'Kroeskop', 'Kromhout', 'Krooshoop', 'Krottje', 'Kruijshaar', 'Kruimelaar', 'Kuiken', 'Kuiltjes', 'Kuitenbrouwer', 'Kuners of Koenders', 'Kutschruiter', 'Kutterik', 'Kuttschreuter', 'Kwaadgras', 'De Kwaadsteniet', 'Kwaaitaal', 'Kwaak', 'Kwakernaak', 'Kwakkel', 'Kwakkelstein', 'Kwakman', 'Kwekkeboom', 'Lachniet', 'Lampenscherf', 'Lamslag', 'De Lange Boom', 'Lastdrager', 'Leeflang', 'Leeuwenkuijl', 'Leffef', 'Legerstee', 'Leijenaar', 'Lestestuiver', 'Van Leuteren', 'Liedermooij', 'Liefbroer', 'Liefhebber', 'Liefjes', 'Lievegoed', 'Van Lievenoogen', 'Lighaam', 'Ligtlijf', 'Lijk', 'Lijkedijk', 'Lijklama', 'Lim,zich noemende en schrijvende Theuvenet', 'Lipjes', 'Lipplaa', 'Lokkerbol', 'Lol', 'Lozekoot', 'Lutje Beerenbroek', 'Lutjeboer', 'Maagdelijn', 'Maandag', 'Maatje', 'Maatjes', 'Maliepaard', 'Mallekoote', 'Maller', 'De Man', 'Mandjes', 'Manneken', 'Manvis', 'Marchee genaamd Bratengeijer', 'Mars', 'Marsman', 'Meeboer', 'Meelkop', 'Meerdinkveldboom', 'Melief', 'Meliefste', 'Mens', 'Metgod', 'Mieremet', 'Miezelmoe', 'Miezerus', 'Mijnheer', 'Mijnhout', 'Mijnlieff', 'Mikmak', 'Miljoen', 'Mistrate of Haarhuis', 'Modderman', 'Moederzoon', 'Moes', 'Mokkelenkate', 'Mokkenstorm', 'Mollevanger', 'Monster', 'Mooijweer', 'Moorthaemer', 'Mostertman', 'Mug', 'Muijshondt', 'Muileboom', 'Von Muralt zich noemende en schrijvende de Muralt', 'Mutsaars', 'Naaktgeboren', 'De Naamloze', 'Naatje', 'Nagelkerken', 'Nagtglas', 'Nattekaas', 'Neefjes', 'Neet', 'Negenman', 'Neger', 'Netjes', 'Neukermans', 'Niemendal', 'De Nies', 'Niesman', 'Niezen', 'Nigten', 'Niks', 'Nooitgedagt', 'Nota', 'Notebaart', 'Nugter', 'Ockeloen', 'Oeyen', 'Van Oldenbarneveld genaamd Witte Tullingh', 'Oldereuver of Briel', 'Olijhoek', 'Van Onlangs', 'Onverwagt', 'Oogjes', 'Oonk', 'Oorlog', 'Oortjes', 'Oostvogel', 'Openneer', 'Opstelten', 'Oranjeboom', 'Ossebaard', 'Ossenkoppele', 'Ossentjuk', 'Oudbier', 'Van Oudenallen', 'Oudgenoeg', 'Oudwater', 'Ouwejan', 'Ouweltjes', 'Paalman', 'Paalvast', 'Paardehaar', 'Padje', 'Palingdood', 'Pampiermole', 'Pannebakker', 'Pannekoek', 'Panneman', 'Pap', 'Papegaaij', 'Papjes', 'Pappelendam', 'Pappot', 'Pasmooij', 'Paterstuk', 'Patimah ook genaamd Patimah Ningsih', 'Pekelharing', 'Peperwortel', 'Peperzak', 'Persoon', 'Pickup', 'Piekeboer', 'Pielkenrood', 'Pielstroom', 'Pieltjes', 'Piepenbroek', 'Pieperiet', 'Pierneef', 'Piest', 'Pieterman', 'Pijpers', 'Pik', 'Pikkemaat', 'Pil', 'Pisman', 'Plaatje', 'Plaisier', 'Plas', 'Platje', 'Platjes', 'Platvoet', 'Plemp van Duiveland', 'Plezier', 'Plomp', 'Plugboer', 'Plukhooij', 'Plukkel', 'Poen', 'Van Poepele', 'Poepjes', 'Poerstamper', 'Poese', 'Poessenauw', 'Poestkoke', 'Poggenklaas', 'Pooijer', 'Pootjes', 'Potappel', 'Potjewijd', 'Potvlieger', 'Profijt', 'Prul', 'Prummel', 'Pufflijk', 'Pulleman', 'Quaaden', 'Quaedvlieg', 'Quaink', 'Quak', 'Quakkelaar', 'De Quay', 'Raar', 'Raket', 'Ramspek', 'Ratelband', 'Rebel', 'De Redelijkheid', 'Van Reet', 'Regtop', 'Rhuggenaath', 'Te Riet ook genaamd Scholten', 'Rijfkogel', 'Rijkelijkhuizen', 'Rijnbende', 'Rijstenbil', 'Ringeling', 'Ringenaldus', 'Riool', 'Roe of Rohe', 'Roerdinkveldboom', 'Rolffs of Roelofs', 'Rommel', 'Roodnat', 'Roofthooft', 'Rookmaker', 'Roos zich noemende en schrijvende Lindgreen', 'Rotgans', 'Rothuizen', 'Rotteveel', 'Rougoor', 'Rozijn', 'Ruimschotel', 'Rukkers', 'Rups', 'Rutten bij- of meergenaamd Verbeek', 'Satoor de Rootas', 'De Schaapmeester', 'Schaapsmeerders', 'Schaepkens', 'Schat', 'Scheerooren', 'Scheiuit', 'Schele', 'Schendstok', 'Scheurkogel', 'Scheurwater', 'Schiettekatte', 'Schijvenschuurder', 'Schimmel', 'Schipaanboord', 'Schoijer', 'Schoof geboren Hollmann', 'Schoonejongen', 'Schoonheid', 'Schotanus', 'Schraal', 'Schreeuwer', 'Schrotenboer', 'Schuddebeurs', 'Schuddeboom', 'Schummelketel', 'Schutrups', 'Seintje', 'Sestig', 'Van Seuren', 'Siebum', 'Siervogel', 'Sikkel', 'Simons of Simonse', 'Sinaasappel', 'Sint Nicolaas', 'Sip', 'Sizoo', 'Slaap', 'Slabbertje', 'Slagboom', 'Slaper', 'Slapman', 'Slappendel', 'Slettenhaar', 'Smakman', 'Snaaijer', 'Snaphaan', 'Snaterse', 'Sneeuwloper', 'Snijdoodt', 'Snijtsever', 'Snitsevorg', 'Snuverink ook Lansink', 'Soddemann genaamd Keute', 'Soepboer', 'Soepnel', 'Soetebier', 'Soetekouw', 'Sollewijn Gelpke', 'Sombekke', 'Sommeling', 'Sondaar', 'Sopjes', 'Sorgdrager', 'Spaargaren', 'Spaarkogel', 'Spaarwater', 'Speelpenning', 'Spinnewijn', 'Spitsbaard', 'Spook', 'Spruyt', 'Staartjes', 'Steeds', 'Sterkendries', 'Stikkelorum', 'Stillebroer', 'Stinkens', 'Stoeltje', 'Stoelwinder', 'Stofregen', 'Stokebrook', 'Stokje', 'Stokvis', 'Stoorvogel', 'Stortenbeker', 'Stouthamer', 'Stouthart', 'Van de Straat', 'Stuitje', 'Stukje', 'Van Suffelen', 'Suikerbuik', 'Sukkel', 'Sul', 'Swets', 'Tanja', 'Tatje', 'Teijema', 'Theeboom', 'Ten Thije ook genoemd Boonkkamp', 'Thoutenhoofd', 'Tienpond', 'Tientjes', 'Tietjens', 'Tijdgaat', 'Tijdgat', 'Tijdmeter', 'Tiktak', 'Titshof', 'Van Tittelboom', 'Toet', 'Toetenel', 'Toeter', 'Tonbreeker', 'Treurniet', 'Trispel', 'Trompetter', 'Trouborst', 'Tuitel', 'Tweesap', 'Udo de Haes', 'Uijen', 'Uijenkruijer', 'Uijttenbroek', 'Uithuisje', 'Uitjes', 'Uitslag', 'Uitvlugt', 'Vaderloos', 'Varkevisser', 'Vastbinder', 'Vastenavond', 'Vastmaar', 'Veefkind', 'Veldpaus', 'Vennegoor of Hesselink', 'Vereenooghe', 'Verreck', 'Vetsuypens', 'Vettevogel', 'Viehoff geboren Maag', 'Vierendeel', 'Viergever', 'Vierkant', 'Vijftigschild', 'Vijfvinkel', 'Vijfwinkel', 'Vingerling', 'Visbeen', 'Vischjager', 'Vischschoonmaker', 'Vischschraper', 'Visje', 'Vissie', 'Vixseboxse', 'De Vlieg', 'Vliegendehond', 'Vliegenthart', 'Vlinkervleugel', 'Vloo', 'Vogelvanger', 'Volle bijgenaamd Roman', 'Vollenbroek', 'Vondeling', 'Voorbij', 'Voordewind', 'Voorraad', 'Voort ook Minkmaat', 'Voorzanger', 'De Vos van Steenwijk genaamd van Essen', 'Vriendje', 'Vrijvogel', 'Vroegindeweij', 'Vroegop', 'Vroegrijk', 'Vrolijk', 'Vuurpijl', 'Wafelbakker', 'Toe Water', 'Waterdrinker', 'Waterlander', 'Weerstand', 'Weesie', 'Wegloop', 'Welbedagt', 'Welles', 'Weltevreden', 'Wermenbol', 'Wientjes', 'Wigt', 'Wijfje', 'Wijkniet', 'Wijnhamer', 'Wijnman', 'Wijnstijn', 'Wijntje', 'Wildeboer', 'Willems of Brilman', 'Wip', 'Wispelweij', 'Wissink ook Geerdink', 'Witbaard', 'Withaar bijgenaamd de Jong', 'Witjes', 'Wittebol', 'Wittebrood', 'Wolff de Beer', 'Wolfskeel', 'Wolzak', 'Wormgoor', 'Wormmeester', 'Wortelboer', 'Wttewaall van Stoetwegen', 'Wurm', 'Zagwijn', 'Zak', 'Zandboer', 'Zandleven', 'Zeeboer', 'Zeldenrijk', 'Zeldenrust', 'Zeldenthuis', 'Zemel', 'Van Zessen', 'Zeuren', 'Ziekenoppasser', 'Zieltjes', 'Ziepzeerder', 'Zievinger', 'Zijtregtop', 'Zoekende', 'Zoetelief', 'Zoetemelk', 'Zomermaand', 'Zomerplaag', 'Zondergeld', 'Zonderland', 'Zonderman', 'Zondervan', 'Zonderzorg', 'Zonligt', 'Zoontjes', 'Zootjes', 'Zoutenbier', 'Zuinig', 'Zuur', 'Zuurbier', 'Zwartebol', 'Zweep', 'Zwetsloot' ]

###############################################################################
# Markov Name model
# A random name generator, by Peter Corbett
# http://www.pick.ucam.org/~ptc24/mchain.html
# This script is hereby entered into the public domain
###############################################################################
class Mdict:
    def __init__(self):
        self.d = {}
    def __getitem__(self, key):
        if key in self.d:
            return self.d[key]
        else:
            raise KeyError(key)
    def add_key(self, prefix, suffix):
        if prefix in self.d:
            self.d[prefix].append(suffix)
        else:
            self.d[prefix] = [suffix]
    def get_suffix(self,prefix):
        l = self[prefix]
        return random.choice(l)  

class MName:
    """
    A name from a Markov chain
    """
    def __init__(self, chainlen = 2, voorachter = 'voor'):
        """
        Building the dictionary
        """
        if chainlen > 10 or chainlen < 1:
            print "Chain length must be between 1 and 10, inclusive"
            sys.exit(0)
    
        self.mcd = Mdict()
        oldnames = []
        self.chainlen = chainlen

	if (voorachter == "achter"):
		PLACES = ACHTER
	else:
		PLACES = VOOR
    
        for l in PLACES:
            l = l.strip()
            oldnames.append(l)
            s = " " * chainlen + l
            for n in range(0,len(l)):
                self.mcd.add_key(s[n:n+chainlen], s[n+chainlen])
            self.mcd.add_key(s[len(l):len(l)+chainlen], "\n")
    
    def New(self):
        """
        New name from the Markov chain
        """
        prefix = " " * self.chainlen
        name = ""
        suffix = ""
        while True:
            suffix = self.mcd.get_suffix(prefix)
            if suffix == "\n" or len(name) > 9:
                break
            else:
                name = name + suffix
                prefix = prefix[1:] + suffix
        return name.capitalize()  