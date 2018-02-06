import pytest
from hamcrest import assert_that, is_, contains_string, matches_regexp, equal_to

from text_paste import get_random_paste, create_paste, get_paste, get_paste_id

PASTE_KEYS = ['created', 'hits', 'hits_updated', 'lang', 'lang_code',
              'name', 'paste', 'pid', 'raw', 'snipurl', 'title', 'url']


class TestGetRandomPaste:

    def setup(self):
        self.random_paste = get_random_paste()

    def test_get_random_paste_keys(self):
        PASTE_KEYS = ['created', 'hits', 'hits_updated', 'lang', 'lang_code',
                      'name', 'paste', 'pid', 'raw', 'snipurl', 'title', 'url']
        paste_keys = sorted(self.random_paste.keys())
        assert_that(paste_keys, is_(PASTE_KEYS))

    def test_get_random_paste_link(self):
        paste_url = self.random_paste['url']
        assert_that(paste_url, contains_string('http://text-share.com/view/'))


class TestGetCreatePaste:
    def setup(self):
        self.paste_test = 'ABC aaa bbb ccc'
        self.paste_title = 'title'
        self.paste_name = 'myname'
        self.paste_private = 0
        self.paste_lang = 'Text'
        self.paste_url = create_paste(text=self.paste_test,
                                      title=self.paste_title,
                                      name=self.paste_name,
                                      private= self.paste_lang,
                                      lang= self.paste_lang)
        self.paste_id = get_paste_id(self.paste_url)

    def test_create_paste(self):
        assert_that(self.paste_url, contains_string('http://text-share.com/view/'))

    def test_get_paste_id(self):
        assert_that(self.paste_id, matches_regexp("[a-zA-Z0-9_]{8}"))

    def test_get_paste(self):
        paste = get_paste(self.paste_id)
        assert_that(paste['raw'], equal_to(self.paste_test))
        assert_that(paste['title'], equal_to(self.paste_title))
        assert_that(paste['name'], equal_to(self.paste_name))
        assert_that(paste['lang_code'], equal_to(self.paste_lang))