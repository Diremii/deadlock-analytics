# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    matches.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas <humontas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 11:17:10 by humontas          #+#    #+#              #
#    Updated: 2026/09/06 12:31:29 by humontas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from psycopg2.extras import execute_values

def insert_matches(cur, data):
	cur.execute("SELECT id FROM items")
	valid_item_ids = {row[0] for row in cur.fetchall()}

	matches_rows = []
	picks_rows = []
	items_rows = []

	for player in data:
		matches_rows.append((player["match_id"], player["start_time"]))
		picks_rows.append((player["match_id"], player["hero_id"], player["won"]))
		for item_id in player["items.item_id"]:
			if item_id in valid_item_ids:
				items_rows.append((player["match_id"], player["hero_id"], item_id))

	execute_values(cur, "INSERT INTO matches (match_id, start_time) VALUES %s ON CONFLICT DO NOTHING", matches_rows)
	execute_values(cur, "INSERT INTO match_picks (match_id, hero_id, won) VALUES %s ON CONFLICT DO NOTHING", picks_rows)
	execute_values(cur, "INSERT INTO match_items (match_id, hero_id, item_id) VALUES %s ON CONFLICT DO NOTHING", items_rows)