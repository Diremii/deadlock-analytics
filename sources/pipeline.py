# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pipeline.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas <humontas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/05 14:30:39 by humontas          #+#    #+#              #
#    Updated: 2026/09/06 12:55:48 by humontas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

from dotenv import load_dotenv

from db.setup import create_database_if_not_exists, run_schema
from db.connection import get_connection
from db.heroes import insert_heroes
from db.items import insert_items
from db.matches import insert_matches
from api.heroes import get_heroes
from api.items import get_items
from api.matches import get_matches_for_period
from utils import get_date_range


def ingest_data(get_function, insert_function, table_name, cur):
	print(f"=== DATABASE ({table_name} TABLE) ===")
	data = get_function()
	print(f"{table_name} recovered successfully. ✅")
	data = insert_function(cur, data)
	print(f"{table_name} sent to the database successfully. ✅\n")

def run_pipeline():
	load_dotenv()
	dbname = os.environ["PGDATABASE"]
	user = os.environ["PGUSER"]
	password = os.environ["PGPASSWORD"]
	host = os.environ["PGHOST"]
	login = (dbname, user, password, host)

	start_date, end_date = get_date_range()

	create_database_if_not_exists(*login)
	run_schema(*login)
	conn, cur = get_connection(*login)
	print("Connection to the database success. ✅\n")

	ingest_data(get_heroes, insert_heroes, "HEROES", cur)
	ingest_data(get_items, insert_items, "ITEMS", cur)
	ingest_data(lambda: get_matches_for_period(start_date, end_date), insert_matches, "MATCHES", cur)

	conn.commit()
	cur.close()
	conn.close()