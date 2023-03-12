

users_create_table = (""" CREATE OR REPLACE TABLE users(
    userid integer not null,
    username char(8),
    firstname varchar(30),
    lastname varchar(30),
    city varchar(30),
    state char(2),
    email varchar(100),
    phone char(14),
    likesports boolean,
    liketheatre boolean,
    likeconcerts boolean,
    likejazz boolean,
    likeclasssical boolean,
    likeopera boolean,
    likerock boolean,
    likevegas boolean,
    likebroadway boolean,
    likemusicals boolean);""")

venue_create_table = (""" CREATE OR REPLACE TABLE venue(
    venueid integer not null,
    venuename varchar(100),
    venuecity varchar(30),
    venuestate char(2),
    venueseats integer);""")

category_create_table = (""" CREATE OR REPLACE TABLE category(
    catid integer not null,
    catgroup varchar(10),
    catname varchar(10),
    catdesc char(50));""")
    
date_create_table = ("""CREATE OR REPLACE TABLE date(
    dateid integer not null,
    caldate date not null,
    day character(3) not null,
    week integer not null,
    month character(5) not null,
    qtr character(5) not null,
    year integer not null,
    holiday boolean);""")
    
event_create_table = ("""CREATE OR REPLACE TABLE event(
    eventid integer not null,
    venueid integer not null,
    catid integer not null,
    dateid integer not null,
    eventname varchar(200),
    starttime TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP());""")
    
listing_create_table = ("""CREATE OR REPLACE TABLE listing(
    listid integer not null,
    sellerid integer not null,
    eventid integer not null,
    dateid integer not null,
    numtickets integer not null,
    priceperticket decimal(8,2),
    totalprice  decimal(8,2),
    listtime TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP());""")