from unittest import TestCase

from sqlalchemy.orm import sessionmaker
from pyramid.config import Configurator
from zope.sqlalchemy import ZopeTransactionExtension

class TestSqlalchemy(TestCase):

    def _make_config(self):
        return Configurator(settings={"sqlalchemy.url": "sqlite://"})

    def test_configure(self):
        config = self._make_config()
        config.include("megalith.sqlalchemy")
        self.assertIsInstance(config.registry.database_maker, sessionmaker)

    def test_configure_without_zope_tm(self):
        config = self._make_config()
        config.include("megalith.sqlalchemy.without_zope_tm")
        # fixme how to test TM not added