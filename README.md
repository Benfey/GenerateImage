<!-- ABOUT THE PROJECT -->
## About The Project

The purpose of this project is to generate images of specific dimensions and sizes to facilitate the testing process.
This is done by filling the image with garbage metadata to hit the target file size.

### Built With

* [Piexif](https://piexif.readthedocs.io/en/latest/)
* [Pillow](https://pillow.readthedocs.io/en/stable/)
* [Numpy](https://numpy.org/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Poetry
  ```sh
  # osx / linux / bashonwindows install instructions
  curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

  # windows powershell install instructions
  (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
  ```

### Installing dependencies

* To install the dependencies
  ```sh
  poetry install
  ```

<!-- USAGE EXAMPLES -->
## Usage

`image.py` takes four parameters:
1. width (int)
2. height (int)
3. magnitude (float)
4. factor (str)

  ```sh
  poetry run python image.py 1920 1080 3 mb
  ```

This will output a 1920x1080 image of roughly 3 MB in size.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- CONTACT -->
## Contact

Anton Benfey - anton.benfey@gmail.com

Project Link: [https://github.com/Benfey/GenerateImage](https://github.com/Benfey/GenerateImage)
