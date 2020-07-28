"""
TODO : make each query a string
"""

query = """
SELECT CustomerId, LastName 
FROM customers
WHERE State = 'CA';
"""


# -- who are our customers? (59)
query = """
SELECT
	CustomerId
	,FirstName
	,LastName
FROM customers;
"""

# -- which customers are from the US? (13) 
query = """
SELECT
	CustomerId
	,FirstName
	,LastName
FROM customers
WHERE Country = "USA";
"""

# -- example of ORDER BY (16)
query = """
SELECT 
	*
FROM customers
WHERE Country in ("USA", "United Kingdom")
ORDER BY Country ASC, State DESC; -- ASC is the default
"""


# --can I have a list of email address for all customers who live in the US?
# -- 59 rows (one per customer)
# -- 13 rows (one per customer, only those in the US)
query = """
SELECT
	CustomerId
	,FirstName
	,LastName
	,Email
	,Country
FROM customers
WHERE Country = "USA";
"""

# -- how many customers do we have?
query = """
SELECT
	count(*) as customer_count -- counts number of rows (59)
	,count(CustomerId) as customer_count2 -- counts number of rows (59)
	,count(DISTINCT CustomerId) as customer_count_3 ---> counts actual unique values
FROM customers;
"""

# -- how many customers are from the US?
query = """
SELECT
	count(DISTINCT CustomerId)
FROM customers
WHERE Country = "USA";
"""


# -- how many customers in each country?
query = """
SELECT 
	Country
	,count(distinct CustomerId) as customer_count ---> (59)
FROM customers
GROUP BY Country;
"""

#-- which 5 countries have the most customers? (makes a nice chart)
query = """
SELECT 
	Country
	,count(distinct CustomerId) as customer_count ---> (59)
FROM customers
GROUP BY Country
ORDER BY customer_count DESC
LIMIT 5;
"""

#-- on average, how many customers in each country?
query = """
SELECT AVG(customer_count) --> (2.45)
FROM (
	SELECT
		Country
		,COUNT(DISTINCT CustomerId) as customer_count -- > 59
	FROM customers
	GROUP BY Country
) subq;
"""

# -- Multi-Table SQL
# -- for each album, what is the name of the artist
# -- 347 rows (row per album)
query = """
SELECT
	albums.AlbumId
	,albums.Title
	,artists.Name
FROM albums
JOIN artists ON albums.ArtistId = artists.ArtistId;
"""

# -- for each artist,
# -- how many albums?
# -- and how many tracks?
# -- row per artist (275)
# -- row per artist (204???)
bay_query = """
SELECT
	artists.ArtistId
	,artists.Name
	,count(DISTINCT albums.AlbumId) as AlbumCount
	,count(DISTINCT tracks.TrackId) as TrackCount
FROM artists
JOIN albums ON artists.ArtistId = albums.ArtistId
JOIN tracks ON tracks.AlbumId = albums.AlbumId
GROUP BY artists.ArtistId;
""" 


# -- for each artist,
# -- how many albums?
# -- and how many tracks?
# -- row per artist (275)

analyze_ba_query = """
SELECT
	artists.ArtistId
	,artists.Name as ArtistName
	,albums.AlbumId
	,tracks.TrackId
FROM artists
LEFT JOIN albums ON artists.ArtistId = albums.ArtistId
LEFT JOIN tracks ON  albums.AlbumId = tracks.AlbumId;
"""


# -- for each artist,
# -- how many albums?
# -- and how many tracks?
# -- row per artist (275)
# -- row per artist (204???)
fixed_bad_query = """
SELECT
	artists.ArtistId
	,artists.Name
	,count(DISTINCT albums.AlbumId) as AlbumCount
	,count(DISTINCT tracks.TrackId) as TrackCount
FROM artists
LEFT JOIN albums ON artists.ArtistId = albums.ArtistId
LEFT JOIN tracks ON  albums.AlbumId = tracks.AlbumId
GROUP BY artists.ArtistId;
"""



