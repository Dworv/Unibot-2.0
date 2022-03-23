
members_create = '''
CREATE TABLE IF NOT EXISTS "members" (
	"user_id"	INTEGER NOT NULL,
	"rank"	TEXT NOT NULL,
	"name"	TEXT NOT NULL,
	"youtube"	TEXT
)
'''.removeprefix('\n')

applications_create = '''
CREATE TABLE IF NOT EXISTS "applications" (
    "application_id"	INTEGER NOT NULL,
    "applicant_id"	INTEGER NOT NULL,
    "review_msg_id"    INTEGER NOT NULL,
    "status"	INTEGER NOT NULL,
    "url"    TEXT NOT NULL
)
'''.removeprefix('\n')