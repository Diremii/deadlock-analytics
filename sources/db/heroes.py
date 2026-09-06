# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    insert_heroes.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas <humontas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 04:04:10 by humontas          #+#    #+#              #
#    Updated: 2026/08/17 04:04:10 by humontas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def insert_heroes(cur, data):
	for hero in data:
		cur.execute(
			"INSERT INTO heroes (id, name) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING",
			(hero["id"], hero["name"])
		)