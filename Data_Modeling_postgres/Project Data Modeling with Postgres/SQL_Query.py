
# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"


# CREATE TABLES

"""
Fact Table:

songplays - records in log data associated with song plays i.e. records with page NextSong
    songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

Dimension Tables:

    users - users in the app
        user_id, first_name, last_name, gender, level
    songs - songs in music database
        song_id, title, artist_id, year, duration
    artists - artists in music database
        artist_id, name, location, latitude, longitude
    time - timestamps of records in songplays broken down into specific units
        start_time, hour, day, week, month, year, weekday
"""

songplays = ("""
             create table if not exists songplays(
             songplay_id serial constraint songplay_pk PRIMARY KEY,
             start_time bigint not null,
             user_id int not null,
             level varchar,
             song_id varchar,
             artist_id varchar,
             session_id int,
             location varchar,
             user_agent text
             );
             """)
users =("""
        create table if not exists users(
            user_id int constraint users_pk primary key,
            first_name varchar,
            last_name varchar,
            gender char(1),
            level varchar not null
        );
        """)
songs = ("""
         create table if not exists songs(
            song_id varchar constraint songs_pk primary key, 
            title varchar, 
            artist_id varchar, 
            year int, 
            duration numeric
         );
         """)
artists = ("""
           create table if not exists artists(
               artist_id varchar constraint artist_pk primary key, 
               name varchar, 
               location varchar,
               latitude float(9), 
               longitude float(9)
           );
           """)

time = ("""
        create table if not exists time(
                start_time bigint constraint time_pk PRIMARY KEY,
                hour int,
                day int,
                week int,
                month int,
                year int,
                weekday int
        );
        """)

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (
    start_time,
    user_id,
    level,
    song_id,
    artist_id,
    session_id,
    location,
    user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users (
    user_id,
    first_name,
    last_name,
    gender,
    level) VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO songs (
    song_id,
    title,
    artist_id,
    year,
    duration) VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (
    artist_id,
    name,
    location,
    latitude,
    longitude) VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time (
    start_time,
    hour,
    day,
    week,
    month,
    year,
    weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING;
""")
# FIND SONGS

song_select = ("""
    SELECT song_id, artists.artist_id
    FROM songs JOIN artists ON songs.artist_id = artists.artist_id
    WHERE songs.title = %s
    AND artists.name = %s
    AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplays, users, songs, artists, time]
# 
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
# 