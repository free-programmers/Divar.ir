class TableNameNotProvidedError(ValueError):
    """
    when You Call BaseModel.SetTableName() without any parameters for table name this exception is thrown
    """
    pass
