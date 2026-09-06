# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    items.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas <humontas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 04:12:07 by humontas          #+#    #+#              #
#    Updated: 2026/09/06 12:56:57 by humontas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from api.client import query_deadlock_api


def get_items():
	return query_deadlock_api("SELECT id, name, tier, cost, slot_type " \
							  "FROM items " \
							  "WHERE type = 'upgrade'")