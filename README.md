# build and run rabbit mq docker
docker build -t moove/mqtt-broker
docker run -d -p 5672:5672 -p 1883:1883 -p 15672:15672 moovel/mqtt-broker

# login to rabbitmq
## open ui
url: http://<docker-ip>:15672/
with username: 'admin' and password:'2YOXrBEDy6BP'

## create user 'moovel'
and set password to '123'
add sufficient permissions. e.g. full permission ;)

# start receiver run config
# start sender run config