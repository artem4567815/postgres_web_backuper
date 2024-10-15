from methods import add_to_delete
from models import *
from config import *
from tools import *
from datetime import datetime, timedelta


def make_backup(modes, files=True, databases=True):

    if databases:
        print("backuping dbs:")

        targets = Schema.query.all()

        freq_delete = [(f"{target.database}_{target.schema}", target.delete_days) for target in targets if target.delete_days]
        objects = [(target.database, target.schema) for target in targets if target.mode in modes]
        tools = [Backuper(PG_USER, PG_PASSWORD, PG_HOST, PG_PORT), Archiver(ZIP_PASSWORD), S3Uploader(S3_REGION, S3_access_key_id, S3_secret_access_key, S3_bucket, DEBUG)]

        for tool in tools:
            print(objects, tool.__class__)
            objects = list(map(tool.apply, objects))

        add_to_delete(objects, freq_delete)

    if files:
        print("backuping files:")

        targets_direct = Directory.query.all()

        objects = [target_direct.path for target_direct in targets_direct if target_direct.mode in modes]
        freq_delete = [(target.path.split("/")[-1], target.delete_days) for target in targets_direct if target.delete_days]
        tools = [Archiver(ZIP_PASSWORD), S3Uploader(S3_REGION, S3_access_key_id, S3_secret_access_key, S3_bucket, DEBUG)]

        for tool in tools:
            print(objects, tool.__class__)
            objects = [object for object in list(map(tool.apply, objects)) if object]

        add_to_delete(objects, freq_delete)


def delete_backup():
        print("deleting...")

        targets = Deleting.query.all()

        objects = [(target.backups_name, target.delete_days) for target in targets]
        tool = S3Uploader(S3_REGION, S3_access_key_id, S3_secret_access_key, S3_bucket, DEBUG)
        today = datetime.today().strftime("%Y-%m-%d")
        today = datetime.strptime(today, "%Y-%m-%d")

        for object in objects:
            if datetime.strptime(object[1], "%Y-%m-%d") <= today:
                record = Deleting.query.filter_by(backups_name=object[0], delete_days=object[1]).first()
                tool.delete(object[0])
                try:
                    db.session.delete(record)
                    db.session.commit()
                except Exception as e:
                    print("error:", e)
