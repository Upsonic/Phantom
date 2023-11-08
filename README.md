# Upsonic Phantom

The cloud python encryption for your applications ! Control everything from one place and distribute all clients without effort.



## Installation
You can install Upsonic by pip3:

```console
pip3 install upsonic_phantom
```


# Implementing
In this point you can use any Upsonic Cloud.

```python
from upsonic import Upsonic_Cloud
cloud = Upsonic_Cloud("YOUR_CLOUD_KEY")


from upsonic_phantom import Upsonic_Phantom
phantom = Upsonic_Phantom(cloud, "YOUR_ENCRYPTION_KEY")

def my_function():
    return "Hello world"


phantom.register(my_function)
phantom.use("my_function")()

```

```
$ Hello world
```


## Contributing
Contributions to Upsonic Phantom are welcome! If you have any suggestions or find a bug, please open an issue on the GitHub repository. If you want to contribute code, please fork the repository and create a pull request.

## License
Upsonic Phantom is released under the MIT License.

<h2 align="center">
    Contributors
</h2>
<p align="center">
    Thank you for your contribution!
</p>
<p align="center">
    <a href="https://github.com/Upsonic/Upsonic-Phantom/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Upsonic/Upsonic-Phantom" />
    </a>
</p>
