all:
	gcc  -o dht11  dht11.c -l wiringPi
so:
	gcc dht11.c -fPIC -shared -o libdht11.so -l wiringPi
clean:
	rm dht11 lib*
