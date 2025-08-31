def test_mysql_connector_import():
    import mysql.connector
    assert mysql.connector.connect is not None, "MySQL Connector is not imported correctly."