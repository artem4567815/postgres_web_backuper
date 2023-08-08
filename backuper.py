from os import system, remove
from pyminizip import compress

class Backuper:
    def do_back_up(self, path, db, schema, filename):
        system(f"pg_dump -U postgres -w -F plain -c -n {schema} {db} > {path}{filename}")

    def create_archive(self, file_name, password, archive_name):
        infile = file_name
        outfile = archive_name
        password = password
        compress_lvl = 5

        # compressing file
        compress(infile, None, outfile, password, compress_lvl)

    def create(self, out_file_name, db, schema, pasw):
        self.out = out_file_name
        self.db = db
        self.schema = schema
        self.pasw = pasw
        self.do_back_up("", self.db, self.schema, "backup.sql")
        self.create_archive("backup.sql", self.pasw, self.out)
        remove("backup.sql")
