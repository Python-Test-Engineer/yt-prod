## This simulates a LIVE production Postgres DB for development work

### It has its own network prod_network

PgAdmin, Adminer and Postgres services must all be on that network to communicate with each other.

### Only one service for each type of image

This avoids accidental confusion of using the prod url rather than the test url.

## Keep the database alive

Rather than destroying and recreating though development etc, the idea is that this DB add data volume remain at all times just like a live system. 

We can then replicate it to a test network to run tests.

Always keeping PROD as isolated from testing and development as possible.


## Combining multiple files

We have split Postgres, PgAdmin and Adminer into their separate files but ensure that they have the same network.

We can then run all three one at at time or in one line:

`docker compose -f docker-compose-postgres.yml -f docker-compose-pgadmin.yml -f docker-compose-adminer.yml up -d`

This is the same as all the information in `docker-compose-production.yml`.