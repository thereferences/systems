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


> docker run [--rm](https://docs.docker.com/engine/reference/commandline/run/#:~:text=a%20container%20exits-,%2D%2Drm,-Automatically%20remove%20the) [-i](https://docs.docker.com/engine/reference/commandline/run/#:~:text=and%20reaps%20processes-,%2D%2Dinteractive,-%2C%20%2Di) [-t](https://docs.docker.com/get-started/02_our_app/#:~:text=Finally%2C%20the-,%2Dt,-flag%20tags%20your) [-p](https://docs.docker.com/engine/reference/commandline/run/#:~:text=%2D%2Dpublish%20%2C-,%2Dp,-Publish%20a%20container%E2%80%99s) 127.0.0.1:10000:8888 -w /app --mount \
    type=bind,src="$(pwd)",target=/app systems

wherein   `-p 10000:8888` maps the host port `1000` to container port `8888`.  Note, the container's working environment, i.e., -w, must be inline with this project's top directory.  View the name of the running instance ``systems`` via

```shell
docker ps --all
```

<br>
<br>

## Development Environment

Developing within the running instance via independent development environment (IDE) tools.

### IntelliJ IDEA

Connect to the Docker [daemon](https://www.jetbrains.com/help/idea/docker.html#connect_to_docker)
* `Settings` $\rightarrow$ `Build, Execution, Deployment` $\rightarrow$ `Docker` $\rightarrow$ WSL: `operating system`
* `View` $\rightarrow$ `Tool Window` $\rightarrow$ `Services` <br> Within the `Containers` section connect to the running instance of interest, or ascertain connection to the running instance of interest.

<br>

### VS Code

For Visual Studio Code container attachment instructions study [Attach Container](https://code.visualstudio.com/docs/devcontainers/attach-container.


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
