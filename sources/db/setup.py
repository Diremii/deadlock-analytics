# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    setup.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas <humontas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 04:37:28 by humontas          #+#    #+#              #
#    Updated: 2026/09/02 16:18:47 by humontas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import psycopg2
from psycopg2 import sql


def create_database_if_not_exists(dbname, user, password, host):
	conn = psycopg2.connect(dbname="postgres", 
							user=user, 
							password=password, 
							host=host)
	conn.autocommit = True
	cur = conn.cursor()
	cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (dbname,))

	exists = cur.fetchone()
	if not exists:
		cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(dbname)))
		print(f"Database '{dbname}' created. ✅")
	else:
		print(f"Database '{dbname}' already exists. ✅")

	cur.close()
	conn.close()

def run_schema(dbname, user, password, host, schema_path="../database/schema.sql"):
	conn = psycopg2.connect(dbname=dbname, 
							user=user, 
							password=password, 
							host=host)
	cur = conn.cursor()
	
	with open(schema_path, "r") as f:
		schema = f.read()
	
	cur.execute(schema)
	conn.commit()
	print("Schema applied. ✅")
	
	cur.close()
	conn.close()