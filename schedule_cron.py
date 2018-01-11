from crontab import CronTab

my_cron = CronTab(user='Gokul')

job = my_cron.new(command='python /home/Gokul/Documents/crypdate/crypto_update.py', comment='crypto_update')

job.hour.every(1)
my_cron.write()


# for job in my_cron:
#     print job
#     my_cron.remove(job)
#     my_cron.write()