"""
    It is a public API for data access
"""
from data_access._class_universal_access import UniversalAccess


def read_data(link, work_dir=None):
    """
    Gets data from a storage
    Parameters
    ----------
    link: path to a data
    work_dir: local work dir for preliminary data manipulation

    Returns
    -------
    error, data
    """
    error, data = None, None
    try:
        handler = UniversalAccess(link, work_dir=work_dir).handler
        data = handler.read_data()
    except Exception as err:
        error = err
    return error, data


def put_data(link, data, work_dir=None):
    """
    Writes data to a storage
    Parameters
    ----------
    link: path to a data
    data: data to write
    work_dir: local work dir for preliminary data manipulation

    Returns
    -------
    error, data
    """
    error = None
    try:
        handler = UniversalAccess(link, work_dir=work_dir).handler
        handler.write_data(data)
    except Exception as err:
        error = err
    return error, data
