import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS testdb")
conn.database = "testdb"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS companies (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        phone_number VARCHAR(20),
        location VARCHAR(255),
        business_type VARCHAR(100)
    )
''')
companies_data = [
    ('Apple Inc.', '+1-800-275-2273', 'Cupertino, CA', 'Technology', 'inf'),
    ('Google LLC', '+1-650-253-0000', 'Mountain View, CA', 'Technology', 'inf'),
    ('Tesla, Inc.', '+1-888-518-3752', 'Palo Alto, CA', 'Automotive', 'inf'),
    ('Microsoft Corporation', '+1-800-642-7676', 'Redmond, WA', 'Technology', 'inf'),
    ('Amazon.com, Inc.', '+1-888-280-4331', 'Seattle, WA', 'E-commerce', 'inf'),
    ('The Coca-Cola Company', '+1-800-438-2653', 'Atlanta, GA', 'Beverages', 'inf'),
    ('Toyota Motor Corporation', '+81-565-23-1111', 'Toyota City, Aichi, Japan', 'Automotive', 'inf'),
    ('Samsung Electronics Co., Ltd.', '+82-2-2255-0114', 'Seoul, South Korea', 'Technology', 'inf'),
    ('Procter & Gamble Co.', '+1-513-983-1100', 'Cincinnati, OH', 'Consumer Goods', 'inf'),
    ('Facebook, Inc.', '+1-650-543-4800', 'Menlo Park, CA', 'Technology', 'inf'),
    ('Alphabet Inc. (Google)', '+1-650-253-0000', 'Mountain View, CA', 'Technology', 'inf'),
    ('Microsoft Corporation', '+1-800-642-7676', 'Redmond, WA', 'Technology', 'inf'),
    ('Intel Corporation', '+1-408-765-8080', 'Santa Clara, CA', 'Technology', 'inf'),
    ('Oracle Corporation', '+1-650-506-7000', 'Redwood City, CA', 'Technology', 'inf'),
    ('IBM (International Business Machines)', '+1-914-499-1900', 'Armonk, NY', 'Technology', 'inf'),
    ('Walmart Inc.', '+1-800-925-6278', 'Bentonville, AR', 'Retail', 'inf'),
    ('General Electric Company', '+1-617-443-3000', 'Boston, MA', 'Conglomerate', 'inf'),
    ('Ford Motor Company', '+1-800-392-3673', 'Dearborn, MI', 'Automotive', 'inf'),
    ('Sony Corporation', '+81-3-6748-2111', 'Tokyo, Japan', 'Technology', 'inf'),
    ('The Walt Disney Company', '+1-818-560-1000', 'Burbank, CA', 'Entertainment', 'inf'),
    ('Boeing Company', '+1-312-544-2000', 'Chicago, IL', 'Aerospace', 'inf'),
    ('Johnson & Johnson', '+1-800-526-3967', 'New Brunswick, NJ', 'Pharmaceutical', 'inf'),
    ('Nestle S.A.', '+41-21-924-1111', 'Vevey, Switzerland', 'Food and Beverage', 'inf'),
    ('Vodafone Group PLC', '+44-1635-33251', 'London, UK', 'Telecommunications', 'inf'),
    ('BMW AG', '+49-89-3820-0', 'Munich, Germany', 'Automotive', 'inf'),
    ('Nike, Inc.', '+1-503-671-6453', 'Beaverton, OR', 'Apparel', 'inf'),
    ('Lockheed Martin Corporation', '+1-301-897-6000', 'Bethesda, MD', 'Aerospace', 'inf'),
    ('McDonald\'s Corporation', '+1-630-623-3000', 'Chicago, IL', 'Fast Food', 'inf'),
    ('Accenture plc', '+1-312-842-5012', 'Dublin, Ireland', 'Consulting', 'inf'),
    ('Cisco Systems, Inc.', '+1-408-526-4000', 'San Jose, CA', 'Networking', 'inf'),
    ('Pfizer Inc.', '+1-212-733-2323', 'New York, NY', 'Pharmaceutical', 'inf'),
    ('Siemens AG', '+49-89-636-00', 'Munich, Germany', 'Engineering', 'inf'),
    ('The Home Depot, Inc.', '+1-770-433-8211', 'Atlanta, GA', 'Retail', 'inf')
]

cursor.executemany('''
    INSERT INTO companies (name, phone_number, location, business_type, resources)
    VALUES (%s, %s, %s, %s, %s)
''', companies_data)
conn.commit()
conn.close()

print("Companies data has been added to the MySQL database.")
