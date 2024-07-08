import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm 

DATABASE_URL="postgresql://practice_owner:HN5Z3aOhJpcU@ep-still-wildflower-a5ggcrcb.us-east-2.aws.neon.tech/fast?sslmode=require"

engine=_sql.create_engine(DATABASE_URL)
SessionLocal=_orm.sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=_declarative.declarative_base()
