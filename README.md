# onlinemonitor - ptactive some python

my first project with
- oop/python 
- postgres docker https://hub.docker.com/_/postgres
-- start postgres with this command: docker run -p 5432:5432 --name myP -e POSTGRES_PASSWORD=postgres -d postgres
- postgres access via psycopg2 https://pypi.org/project/psycopg2/ (pip install psycopg2)
- git
- runs with https://pypi.org/project/psycopg2/ (pip install psycopg2)

feature
- add hosts to a table
- run ping in threads and see avg ms of the last x minutes (including missed pings)

note
- not tested on linux yet

todo
- add config file instead of hardcoded connection parameter
- add views to improve preformance db actions
- add verbose mode to let script run in service mode
- redesign consule output: only perform 1 select for all hosts to get results instead 1 select per host
-- change single select to grouped select
