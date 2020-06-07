from models import UsageMaster
settings.configure()

record = UsageMaster(genrei = "Entertainment")
record.save()
