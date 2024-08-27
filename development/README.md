<br>

Systems: An Exploration

<br>

## Notes

Foremost, set-up the development environment scriits:

* Dockerfile
* requirements.txt

Hence, extend the base image in Dockerfile via command

```shell
docker build . --file .devcontainer/Dockerfile --tag transcribe
```

It names the new image `transcribe`.  Subsequently, a container/instance of the image `transcribe` may be used as a
development environment via the command:


> docker run [--rm](https://docs.docker.com/engine/reference/commandline/run/#:~:text=a%20container%20exits-,%2D%2Drm,-Automatically%20remove%20the) [-i](https://docs.docker.com/engine/reference/commandline/run/#:~:text=and%20reaps%20processes-,%2D%2Dinteractive,-%2C%20%2Di) [-t](https://docs.docker.com/get-started/02_our_app/#:~:text=Finally%2C%20the-,%2Dt,-flag%20tags%20your) [-p](https://docs.docker.com/engine/reference/commandline/run/#:~:text=%2D%2Dpublish%20%2C-,%2Dp,-Publish%20a%20container%E2%80%99s) 127.0.0.1:10000:8888 -w /app --mount \
&nbsp; &nbsp; type=bind,src="$(pwd)",target=/app transcribe

wherein   `-p 10000:8888` maps the host port `10000` to container port `8888`.  Note, the container's working environment,
i.e., -w, must be inline with this project's top directory.  View the name of the running instance ``transcribe`` via:

```shell
docker ps --all
```

<br>
<br>

## Development Environment

Developing within the running instance via independent development environment (IDE) tools.

<br>

### IntelliJ IDEA

Connect to the Docker [daemon](https://www.jetbrains.com/help/idea/docker.html#connect_to_docker)
* `Settings` $\rightarrow$ `Build, Execution, Deployment` $\rightarrow$ `Docker` $\rightarrow$ WSL: `operating system`
* `View` $\rightarrow$ `Tool Window` $\rightarrow$ `Services` <br> Within the `Containers` section connect to the running instance of interest, or ascertain connection to the running instance of interest.

<br>

### VS Code

For Visual Studio Code container attachment instructions study [Attach Container](https://code.visualstudio.com/docs/devcontainers/attach-container).

<br>
<br>

## SPHINX

Initialize `sphinx` documentation settings

```shell
mkdir docs && cd docs && sphinx-quickstart && cd ..
```

Hence

```shell
sphinx-build -E -b html docs/source docs/build/html
```

Themes

* https://github.com/revitron/revitron-sphinx-theme


<br>
<br>

## References

* https://www.tabulator.info/docs/5.5/data#import
* https://www.tabulator.info/docs/5.5/install
* https://www.sphinx-doc.org/en/master/
* https://sphinx-themes.readthedocs.io/en/latest/sample-sites/sphinx-rtd-theme/
* https://sphinx-design.readthedocs.io/en/latest/index.html
* https://myst-parser.readthedocs.io/en/latest/index.html
* https://pradyunsg.me/furo/
* https://myst-parser.readthedocs.io/en/latest/configuration.html
* https://www.sphinx-doc.org/en/master/usage/extensions/math.html#module-sphinx.ext.mathjax
* https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#math-shortcuts
* https://www.sphinx-doc.org/en/master/usage/extensions/index.html
  * https://github.com/yoloseem/awesome-sphinxdoc?tab=readme-ov-file


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
