import csv


class Backup:

    def __init__(self, account_id, client):
        self.account_id = account_id
        self.client = client

    def list_recovery_points_with_tags(self):

        try:
            response = self.client.list_recovery_points_by_backup_vault(
                BackupVaultName='Default',
            )

            size = len(response['RecoveryPoints'])
            data_file = []

            for i in range(size):
                resource_arn = response['RecoveryPoints'][i]['RecoveryPointArn']
                tags = self.client.list_tags(
                    ResourceArn=resource_arn

                )

                tag = tags['Tags']
                resource_type = response['RecoveryPoints'][i]['ResourceType']
                backup_size = response['RecoveryPoints'][i]['BackupSizeInBytes']
                creation_date = str(
                    response['RecoveryPoints'][i]['CreationDate'].date())
                completion_date = str(
                    response['RecoveryPoints'][i]['CompletionDate'].date())

                tag_size = len(tag)

                if tag_size == 0:
                    row = [creation_date, completion_date, resource_arn,
                           resource_type, backup_size, " ", " "]
                    data_file.append(row)
                else:
                    for i in range(tag_size):
                        row = [creation_date, completion_date, resource_arn, resource_type, backup_size,
                               list(tag.keys())[i], list(tag.values())[i]]
                        data_file.append(row)

            self.write_to_csv(data_file)
            print("Complete writing csv file")

        except NameError:
            print("Error listing recovery point with tags")

    def get_tags(self):

        response = self.client.list_recovery_points_by_backup_vault(
            BackupVaultName='Default',
        )

        size = len(response['RecoveryPoints'])
        tags_list = []

        for i in range(size):
            resource_arn = response['RecoveryPoints'][i]['RecoveryPointArn']
            tags = self.client.list_tags(
                ResourceArn=resource_arn

            )
            if tags['Tags'] != {}:
                for key in list(tags['Tags'].keys()):
                    if key not in tags_list:
                        tags_list.append(key)

        return tags_list

    def write_to_csv(self, data_file):
        csv_file = open('/tmp/csv_file.csv', 'w')
        csv_writer = csv.writer(csv_file)

        header = ["CreationDate", "CompletionDate", "ResourceArn", "ResourceType",
                  "BackupSize", "TagKey", "TagValue"]
        csv_writer.writerow(header)
        csv_writer.writerows(data_file)

        csv_file.close()
