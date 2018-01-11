# text-share
### Wrapper for [text-share.com](http://text-share.com/)

You can use python functions to paste text on the [text-share.com](http://text-share.com/)

### Examples

## How to install


**Install pre-conditions (Ubuntu):**

Execute following commands in a terminal:
```
$ sudo apt-get install git
$ sudo apt-get install python-pip
$ sudo pip install virtualenv .venv
$ sudo pip install --upgrade pip
```


Execute following commands in the terminal:
```
$ git clone https://github.com/Turivniy/my_git.git
$ cd my_git
$ virtualenv .venv
$ . .venv/bin/activate
$ pip install -U pip
$ pip install -r requirements.txt
```


Paste text:
```python
$ python
>>> from text_paste import create_paste
>>> text_to_paste = 'This is my very first paste'
>>> paste_url = create_paste(text_to_paste)
>>> print(paste_url)

http://text-share.com/view/xxxxxxxx
```
Where `xxxxxxxx` in the `paste_url` it's **`id`** of you paste


More advanced paste example with `title`, `name`, `lang` etc.:
```python
>>> from text_paste import create_paste
>>> text_to_paste = 'This is my very first paste'
>>> paste_url = create_paste(text_to_paste,
                             title='my title',
                             name='my name',
                             private=0,
                             lang='Text')
>>> print(paste_url)

http://text-share.com/view/yyyyyyyy
```
Now you paste will be contained `title`, `name`, `lang` and everybody will have access to it.


Possible paste options you can get like this or on the [text-share.com](http://text-share.com/api) page:
```python
>>> from text_paste import create_paste
>>> help(create_paste)

create_paste(text, **kwargs)
    text='your paste text'
    The paste content. Required.

    title='title'
    Title for the paste.

    name='name'
    The author's name.

    private=1
    Make paste private.

    lang='language'
    Use get_list_available_languages() method

    expire='minutes'
    Set paste expiration.

    reply='pasteid'
    Reply to existing paste.
```


You can get paste by paste **`id`**:
```python
>>> from text_paste import get_paste
>>> paste_url = get_paste(pasteid='xxxxxx')
```


It's possible to get `id` from posted paste:
```python
>>> from text_paste import create_paste, get_paste_id, get_paste_raw_text
>>> text_to_paste = 'This is my very first paste'
>>> paste_url = create_paste(text_to_paste)
>>> print(paste_url)

http://text-share.com/view/xxxxxxxx

>>> paste_id = get_paste_id(paste_url)
>>> paste_text = get_paste_raw_text(paste_id)
>>> print(paste_text)

This is my very first paste
```