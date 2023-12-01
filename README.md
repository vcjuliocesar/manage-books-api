# manage-books-api

 Welcome to the **manage-books-api** repository! This is a simple guide to help you get started with settings up and running the project.
___

## Requirements
 
 * Python:3 :snake:

 * PIP:3 :snake:
 
 * Mongo

 ## Getting Started

Follow these steps to set up and run the project on your local machine:

### Clone the repository

```git
git clone git@github.com:vcjuliocesar/manage-books-api
```

**Create enviroment file:** rename .env.example by .env

add your enviroment variables

It is important that you have python and pip installed on your computer

**Create a Virtual Environment**

```sh
python3 -m venv env
```

**Activate the Virtual Environment: On macOS/Linux**

```sh
source env/bin/activate
```

**On Windows**

```sh
.\env\Scripts\activate
```

**Install dependencies**

```sh
pip3 install --no-cache-dir requirements.txt
```

**Run the project**

```
uvicorn src.app.main:app --reload
```

#### Happy Code! :smiley: