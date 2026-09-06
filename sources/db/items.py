# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    items.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas <humontas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 04:13:30 by humontas          #+#    #+#              #
#    Updated: 2026/08/17 04:23:30 by humontas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def insert_items(cur, data):
	for item in data:
		cur.execute(
			"INSERT INTO items (id, name, tier, cost, slot_type) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING",
			(item["id"], item["name"], item["tier"], item["cost"], item["slot_type"])
		)