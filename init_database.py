from rich import print
from base import Base
from connection import engine
from models import Book

Base.metadata.create_all(bind=engine)
print("[green]database create succ[/green]")
