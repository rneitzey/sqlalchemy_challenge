first_row_measurement = session.query(Measurement).first()
first_row_measurement.__dict__

inspector = inspect(engine)
inspector.get_table_names()