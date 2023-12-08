<br>

Systems: An Exploration

<br>

### Notes

Set-up:

* Dockerfile
* requirements.txt

Extend the base image in the Dockerfile via

```shell
docker build -t systems .
```

Subsequently, a container/instance of the image `systems` may be used as a development environment via the command

```shell
docker run --rm -i -t -p 127.0.0.1:10000:8888 -w /app --mount type=bind,src="$(pwd)",target=/app systems
```

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
