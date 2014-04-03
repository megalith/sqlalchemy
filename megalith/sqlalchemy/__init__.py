import sys

from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

def db(request):
    maker = request.registry.database_maker
    session = maker()

    def cleanup(request):
        session.close()
    request.add_finished_callback(cleanup)

    return session

def _include(config, zope_tm=True):
    config.registry.database_engine = engine_from_config(config.registry.settings, prefix="sqlalchemy.")

    args = {}
    if zope_tm:
        try:
            from zope.sqlalchemy import ZopeTransactionExtension
            args["extension"] = ZopeTransactionExtension()
        except ImportError:
            sys.exit("megalith.sqlalchemy included, but ZopeTransactionExtension could not be imported.")

    config.registry.database_maker = sessionmaker(bind=config.registry.database_engine, **args)
    config.add_request_method(db, reify=True)

def includeme(config):
    _include(config, zope_tm=True)

def with_zope_tm(config):
    _include(config, zope_tm=True)

def without_zope_tm(config):
    _include(config, zope_tm=False)