from collections import defaultdict

class Table:
    def __init__(self, name: str):
        self.name = name
        self.data = {}
        self.indexes = {}
        self.auto_increment_id = 1

    def create_index(self,column_name: str):

        index = defaultdict(set)

        for record_id, record in self.data.items():

            if column_name in record:
                index[record[column_name]].add(record_id)
        
        self.indexes[column_name] = index

class IN_DB:
    def __init__(self, Tables: list[Table]):
        self.tables = {table.name: table for table in Tables}

    def insert(self, table_name: str, record: dict):

        if table_name not in self.tables:
            raise Exception("Table does not exist")

        table = self.tables[table_name]
        record_id = table.auto_increment_id
        table.data[record_id] = record
        table.auto_increment_id += 1

    def index(self, table_name: str, column_name: str):

        if table_name not in self.tables:
            raise Exception("Table does not exist")
        
        table = self.tables[table_name]
        table.create_index(column_name)

    def query(self, table_name: str, column_name: str, value, filter : dict = None, sort_by: str = None, limit: int = None):

        if table_name not in self.tables:
            raise Exception("Table does not exist") 
        
        table = self.tables[table_name]

        if column_name in table.indexes:
            record_ids = table.indexes[column_name].get(value, set())
            res = [table.data[record_id] for record_id in record_ids]

            res = self.apply_filter(res, filter)

        else:
            return [record for record in table.data.values() if record.get(column_name) == value]



        # if table_name not in self.tables:
        #     raise Exception("Table does not exist")

        # table = self.tables[table_name]
        # index = {}
        # for record_id, record in table.data.items():
        #     value = record.get(column_name)
        #     if value is not None:
        #         if value not in index:
        #             index[value] = []
        #         index[value].append(record_id)

        # table.indexes[column_name] = index