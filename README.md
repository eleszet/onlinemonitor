# onlinemonitor - project for practice reason

my first 
- oop/python project 
- postgres docker https://hub.docker.com/_/postgres
-- start postgres with this command: docker run -p 5432:5432 --name myP -e POSTGRES_PASSWORD=postgres -d postgres
- git
- runs with https://pypi.org/project/psycopg2/ (pip install psycopg2)

feature
- add hosts to a table
- run ping in threads and see avg ms of the last x minutes (including missed pings)
note
- not tested on linux yet

todo
- add config file instead of hardcoded connection parameter
- add verbose mode to let script run in service mode