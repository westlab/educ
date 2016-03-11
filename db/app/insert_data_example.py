# Sample for SQL generation from data.csv
# You can follow this example and should write
# the rest of code to insert data to database

INSERT_TMP="""\
INSERT INTO users (name, bday, age, state)
VALUES
{}
"""

def convert_values(data):
    """
    Convert list into VALUES format

    (name, bday, age, state)
    """
    return '("{}", "{}", {}, "{}")'.format(*data)

def get_data():
    with open('./data.csv') as f:
        for line in f:
            yield line.strip().split(',')

sql = INSERT_TMP.format(",\n".join(convert_values(d) for d in get_data()))

"""
example of output

INSERT INTO users (name, bday, age, state)
VALUES
("Bettye Purdy", "2001-05-21", 15, "Maine"),
("Mrs. Elisabeth Wilderman MD", "1999-01-21", 17, "Pennsylvania"),
("Edgar Kreiger", "1973-11-11", 43, "Vermont"),
("Saverio McCullough", "2007-10-13", 9, "Idaho"),
...
"""
